"""Diagnostics: is the forecast telling you anything at all?

Two questions matter more than the backtest:

1. Direction accuracy. Ignore the size of the forecast and ask whether its sign
   matches the realised sign. A number near 50 percent means the model has no
   directional content, whatever the backtest says.
2. Information coefficient. The cross-sectional rank correlation between the
   forecast and the realised return.
"""
from __future__ import annotations

import numpy as np


def sign_accuracy(predicted: np.ndarray, realized: np.ndarray) -> float:
    keep = np.isfinite(predicted) & np.isfinite(realized) & (realized != 0)
    if keep.sum() < 30:
        return float("nan")
    return float(np.mean(np.sign(predicted[keep]) == np.sign(realized[keep])))


def rank_ic(predicted: np.ndarray, realized: np.ndarray) -> float:
    keep = np.isfinite(predicted) & np.isfinite(realized)
    if keep.sum() < 30:
        return float("nan")
    a = _rank(predicted[keep])
    b = _rank(realized[keep])
    if a.std() == 0 or b.std() == 0:
        return float("nan")
    return float(np.corrcoef(a, b)[0, 1])


def _rank(x: np.ndarray) -> np.ndarray:
    return np.argsort(np.argsort(x)).astype(float)
