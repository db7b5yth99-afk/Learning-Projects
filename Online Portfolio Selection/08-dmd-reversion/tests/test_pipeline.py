"""Tests for the DMD reversion demo.

    python tests/test_pipeline.py      # prints one line per check
    pytest tests/test_pipeline.py      # if you have pytest

The two interesting checks are the rank-interpolation condition and the
portfolio dedupe: those are where a silent bug would flatter every result.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from dmd_reversion.diagnostics import rank_ic, sign_accuracy
from dmd_reversion.dmd import dmd_forecast
from dmd_reversion.pipeline import COST, WIN, draw_thresholds, portfolio, select
from dmd_reversion.synthetic import make_market


def in_sample_r2(window, rank):
    """One-step in-sample R2 of the fitted operator."""
    centered = window - window.mean(axis=0)
    x_d, y_d = centered[:-1].T, centered[1:].T
    u, s, vt = np.linalg.svd(x_d, full_matrices=False)
    r = len(s) if rank is None else int(min(rank, len(s)))
    ur = u[:, :r]
    operator = ur.T @ y_d @ vt[:r].T @ np.diag(1.0 / np.maximum(s[:r], 1e-12))
    predicted = ur @ (operator @ (ur.T @ x_d))
    denom = np.sum((y_d - y_d.mean(axis=0)) ** 2)
    return float(1.0 - np.sum((y_d - predicted) ** 2) / denom)


# ---------------------------------------------------------------- forecast
def test_forecast_shape():
    window = np.random.default_rng(0).normal(size=(60, 25))
    assert dmd_forecast(window, rank=5).shape == (25,)


def test_full_rank_interpolates_when_names_exceed_days():
    """300 names, 99 transitions: full rank fits the window exactly."""
    window = np.random.default_rng(1).normal(size=(100, 300))
    assert in_sample_r2(window, None) > 0.999


def test_truncation_regularises():
    window = np.random.default_rng(1).normal(size=(100, 300))
    assert in_sample_r2(window, 2) < 0.90
    assert in_sample_r2(window, 5) < 0.98


def test_overdetermined_when_names_below_days():
    """25 names, 59 transitions: the same fit is regularised."""
    window = np.random.default_rng(1).normal(size=(60, 25))
    assert in_sample_r2(window, None) < 0.95


# ---------------------------------------------------------------- data
def test_market_shapes():
    close, openr, sectors = make_market(n_tickers=40, n_days=300)
    assert close.shape == (300, 40) and openr.shape == (300, 40)
    assert sectors.shape == (40,)


def test_reversal_signal_is_planted():
    def lag1(x):
        return float(np.corrcoef(x[:-1].ravel(), x[1:].ravel())[0, 1])

    clean, _, _ = make_market(n_tickers=60, n_days=800, signal="none")
    planted, _, _ = make_market(n_tickers=60, n_days=800, signal="reversal")
    assert lag1(clean) > -0.05
    assert lag1(planted) < -0.15


# ---------------------------------------------------------------- portfolio
def test_one_position_per_stock():
    returns = np.zeros((60, 2))
    entries = [(0, 0), (5, 0), (25, 0)]
    result = portfolio(returns, entries, hold=20, cost=0.0)
    assert result["trades"] == 2, result  # day 5 waits for the day-0 exit


def test_cost_is_charged():
    returns = np.zeros((40, 1))
    returns[:20, 0] = 0.001
    free = portfolio(returns, [(0, 0)], hold=20, cost=0.0)
    paid = portfolio(returns, [(0, 0)], hold=20, cost=COST)
    assert abs(free["gross"] - paid["gross"]) < 1e-12
    assert abs((free["net"] - paid["net"]) - COST) < 1e-12


def test_win_threshold():
    returns = np.zeros((40, 1))
    returns[:20, 0] = (WIN + 0.01) / 20      # just above the win threshold
    assert portfolio(returns, [(0, 0)], hold=20)["win"] == 1.0
    returns[:20, 0] = (WIN - 0.01) / 20      # just below it
    assert portfolio(returns, [(0, 0)], hold=20)["win"] == 0.0


# ---------------------------------------------------------------- thresholds
def test_thresholds_in_range():
    rng = np.random.default_rng(3)
    for _ in range(500):
        coverage, min_forecast = draw_thresholds(rng)
        assert 0.01 <= coverage <= 0.20
        assert 0.002 <= min_forecast <= 0.02


def test_select_respects_side_and_coverage():
    forecast = np.array([0.05, 0.04, -0.05, -0.04, 0.001])
    longs = select(forecast, "long", 0.5, 0.02)
    shorts = select(forecast, "short", 0.5, 0.02)
    assert set(longs.tolist()) <= {0, 1}
    assert set(shorts.tolist()) <= {2, 3}
    assert len(longs) == 1


# ---------------------------------------------------------------- diagnostics
def test_sign_accuracy_perfect():
    rng = np.random.default_rng(5)
    x = rng.normal(size=500)
    assert abs(sign_accuracy(x, x) - 1.0) < 1e-12


def test_sign_accuracy_on_noise_is_half():
    rng = np.random.default_rng(5)
    x, y = rng.normal(size=20000), rng.normal(size=20000)
    assert abs(sign_accuracy(x, y) - 0.5) < 0.02


def test_rank_ic_extremes():
    x = np.linspace(-1, 1, 200)
    assert abs(rank_ic(x, x) - 1.0) < 1e-9
    assert abs(rank_ic(x, -x) + 1.0) < 1e-9


def main() -> int:
    checks = [(n, f) for n, f in sorted(globals().items()) if n.startswith("test_") and callable(f)]
    failed = 0
    for name, fn in checks:
        try:
            fn()
            print(f"PASS  {name}")
        except AssertionError as exc:
            failed += 1
            print(f"FAIL  {name}: {exc}")
        except Exception as exc:  # noqa: BLE001
            failed += 1
            print(f"ERROR {name}: {type(exc).__name__}: {exc}")
    print(f"\n{len(checks) - failed}/{len(checks)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
