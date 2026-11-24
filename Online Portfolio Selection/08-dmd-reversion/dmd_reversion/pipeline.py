"""The whole pipeline: forecast, three thresholds, portfolio.

Reading order: synthetic.py (data), dmd.py (forecast), this file (everything else).
"""
from __future__ import annotations

import numpy as np

from dmd_reversion.dmd import dmd_forecast
from dmd_reversion.synthetic import make_market

WINDOW = 252        # sessions of history used by the forecast
HOLD = 20           # sessions a position is held
COST = 0.02         # round-trip cost
WIN = 0.05          # gross return needed to count as a win


def draw_thresholds(rng):
    """Two thresholds, drawn at random: coverage and minimum forecast."""
    coverage = float(np.exp(rng.uniform(np.log(0.01), np.log(0.20))))
    min_forecast = float(rng.uniform(0.002, 0.02))
    return coverage, min_forecast


def select(forecast, side, coverage, min_forecast):
    """Stock indices to trade on one day: those past the threshold, best first."""
    ok = forecast >= min_forecast if side == "long" else forecast <= -min_forecast
    idx = np.where(ok)[0]
    if idx.size == 0:
        return idx
    take = max(int(round(idx.size * coverage)), 1)
    return idx[np.argsort(-forecast[idx], kind="stable")[:take]]


def portfolio(returns, entries, hold=HOLD, cost=COST):
    """One position per stock; a second entry waits for the first to exit."""
    busy, keep = {}, []
    for day, stock in sorted(map(tuple, entries)):
        stock = int(stock)
        if stock in busy and day < busy[stock]:
            continue
        keep.append((int(day), stock))
        busy[stock] = int(day) + hold

    gross = np.array([returns[d:d + hold, s].sum() for d, s in keep
                      if d + hold <= len(returns)])
    if gross.size == 0:
        return {"trades": 0, "win": np.nan, "gross": np.nan, "net": np.nan}
    return {"trades": int(gross.size), "win": float(np.mean(gross > WIN)),
            "gross": float(gross.mean()), "net": float(gross.mean() - cost)}


def forward_returns(returns, hold=HOLD):
    """Forward holding-period return for every (day, stock)."""
    total = np.vstack([np.zeros((1, returns.shape[1])), np.cumsum(returns, axis=0)])
    out = np.full(returns.shape, np.nan)
    for t in range(len(returns) - hold):
        out[t] = total[t + hold] - total[t]
    return out


def run_variants(signal="none", quick=False, rank=20, seed=7):
    """Run close/open x long/short and return one row per variant."""
    n_days = 900 if quick else 1400
    step = 3 if quick else 1
    draws = 40 if quick else 120

    close_ret, open_ret, _ = make_market(n_tickers=150, n_days=n_days, seed=seed, signal=signal)
    rows = []

    for field, returns in (("close", close_ret), ("open", open_ret)):
        forecast = np.full_like(returns, np.nan)
        for t in range(WINDOW, n_days, step):
            forecast[t] = dmd_forecast(returns[t - WINDOW:t], rank=rank)
        fwd = forward_returns(returns)

        days = [t for t in range(WINDOW, n_days - HOLD)
                if np.all(np.isfinite(forecast[t])) and np.isfinite(fwd[t]).all()]
        val = [t for t in days if int(n_days * 0.55) <= t < int(n_days * 0.75)]
        test = [t for t in days if t >= int(n_days * 0.75)]

        def entries_on(day_list, side, thresholds):
            return [(t, s) for t in day_list
                    for s in select(forecast[t], side, *thresholds)]

        rng = np.random.default_rng(seed)
        best, best_net = (0.05, 0.01), -np.inf
        for _ in range(draws):
            thresholds = draw_thresholds(rng)
            result = portfolio(returns, entries_on(val, "long", thresholds))
            if result["trades"] >= 25 and np.isfinite(result["net"]) and result["net"] > best_net:
                best, best_net = thresholds, result["net"]

        for side in ("long", "short"):
            result = portfolio(returns, entries_on(test, side, best))
            rows.append({"variant": field + "_" + side, **result})
    return rows


def format_table(rows):
    """Plain-text table, used by both the CLI and the notebook."""
    lines = ["%-12s%8s%9s%10s%10s" % ("variant", "trades", "win", "gross", "net"),
             "-" * 49]
    for r in rows:
        lines.append("%-12s%8d%8.1f%%%9.2f%%%9.2f%%" % (
            r["variant"], r["trades"], 100 * r["win"], 100 * r["gross"], 100 * r["net"]))
    return "\n".join(lines)