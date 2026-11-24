"""Dynamic mode decomposition forecast.

Given a window of daily returns, fit the least-squares linear operator that maps
one day's cross-section to the next, then apply it to the last cross-section.

The rank parameter is the whole story. With rank = min(n_tickers, window - 1) the
operator has as many degrees of freedom as the window has days, so it reproduces
the window exactly and forecasts nothing. Truncating the rank is what turns it
into a model.
"""
from __future__ import annotations

import numpy as np


def dmd_forecast(returns_window: np.ndarray, rank: int | None = None) -> np.ndarray:
    """Forecast the next cross-section.

    Parameters
    ----------
    returns_window : (n_days, n_tickers) array of daily log returns.
    rank : number of modes to keep. None means full rank (see the note above).
    """
    window = np.asarray(returns_window, dtype=float)
    mu = window.mean(axis=0)
    centered = window - mu

    x_d = centered[:-1].T          # (n_tickers, n_days - 1)
    y_d = centered[1:].T
    u, s, vt = np.linalg.svd(x_d, full_matrices=False)

    r = len(s) if rank is None else int(min(rank, len(s)))
    ur = u[:, :r]
    operator = ur.T @ y_d @ vt[:r].T @ np.diag(1.0 / np.maximum(s[:r], 1e-12))
    last = centered[-1]
    return ur @ (operator @ (ur.T @ last)) + mu
