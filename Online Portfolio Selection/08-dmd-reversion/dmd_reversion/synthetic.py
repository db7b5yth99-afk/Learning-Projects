"""Synthetic market data.

Real data cannot be shipped with this repository, so the demo generates a small
panel that behaves like an equity cross-section: a market factor, sector factors
and idiosyncratic noise, plus an optional one-day reversal.

signal="none"      pure noise -- the model should find nothing
signal="reversal"  today's idiosyncratic move partly reverses tomorrow, which
                   gives the model a real, linear, next-day structure to find

Neither setting says anything about real markets. They exist so the demo can show
both outcomes: a pipeline that finds nothing, and a pipeline that finds something
and still loses to the cost.
"""
from __future__ import annotations

import numpy as np


def make_market(
    n_tickers: int = 150,
    n_days: int = 1400,
    n_sectors: int = 5,
    seed: int = 7,
    signal: str = "none",
    reversal: float = 0.35,
):
    """Return (close_returns, open_returns, sectors).

    Both return arrays are daily log returns of shape (n_days, n_tickers).
    """
    rng = np.random.default_rng(seed)
    sectors = rng.integers(0, n_sectors, n_tickers)

    market = rng.normal(0.0002, 0.008, n_days)
    sector = rng.normal(0.0, 0.006, (n_days, n_sectors))
    idio = rng.normal(0.0, 0.020, (n_days, n_tickers))

    if signal == "reversal":
        # tomorrow undoes a fraction of today's idiosyncratic move
        idio = idio.copy()
        idio[1:] -= reversal * idio[:-1]

    close_ret = market[:, None] + sector[:, sectors] + idio

    # split each day into an overnight gap and a session, so the open variants
    # have their own return series to work with
    gap = 0.30 * idio + rng.normal(0.0, 0.004, (n_days, n_tickers))
    session = close_ret - gap
    open_ret = gap + np.roll(session, 1, axis=0)
    open_ret[0] = gap[0]

    return (np.asarray(close_ret, dtype=float),
            np.asarray(open_ret, dtype=float),
            sectors)
