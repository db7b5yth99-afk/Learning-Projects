# Extrema Detection Strategy

Detecting reversal zones, peaks and troughs, on the Hang Seng Index, and turning that into an
entry and exit rule. Built in five stages; the numbering is the order they were written.

Each folder is one stage with its own README and notebooks.

## Stages

| Stage | What it adds |
|---|---|
| [01-baseline-gru](<01-baseline-gru/README.md>) | a plain GRU on reversal-zone labels, to establish what the task can do at all |
| [02-uncertainty-sgld](<02-uncertainty-sgld/README.md>) | SGLD training, so the model reports how sure it is, not just what it thinks |
| [03-distillation-cbkd](<03-distillation-cbkd/README.md>) | distillation from two teachers, with a dual-engine risk forecast and a three-term loss |
| [04-cross-asset-fusion](<04-cross-asset-fusion/README.md>) | peer confirmation from the S&P 500 and the FTSE, strictly same-day aligned |
| [05-engines](<05-engines/README.md>) | end-to-end engines, ending with the one that sizes positions by uncertainty |

## Where to start

05-engines/Turning_Point_Analysing_Engine.ipynb. It is the only version that carries the
uncertainty signal all the way through to execution, and it is the closest this line of work
came to a working strategy.

For the idea at its simplest, 01-baseline-gru/GRU_Vanilla.ipynb.

## How the labels are built, and the caveat that comes with them

Targets come from a centered moving-average extrema scanner: a point is a peak or a trough
if it is the local extreme of a window centred on it. That uses future data by construction.

This is fine for the question the notebooks ask, which is whether a model can recognise a
shape once it has been told what shapes exist. It is not a tradeable label. Any pipeline that
turns these predictions into trades has to re-derive the labels causally and check that
performance survives, and this folder does not do that.

Treat the reported accuracy as an upper bound on what the features can express, not as an
expected return.

## Why it stopped

The cross-asset stage needs three markets aligned to the same trading day plus multi-frequency
feature extraction, and the training loop grows long enough that iteration stopped being
practical. It worked well enough to be interesting, and not well enough to justify the
compute.

## Running

Colab with a GPU. Each notebook installs talib and mplfinance at the top, downloads data with
yfinance, and writes checkpoints to Google Drive. Local runs need those paths edited.

    pip install torch numpy pandas scipy scikit-learn matplotlib seaborn quantstats talib yfinance mplfinance

## Credit

Fang, Chen, Zhong & Ma (2024) for the Bayesian knowledge distillation view that the
distillation stage follows.
