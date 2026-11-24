# Online Portfolio Selection

Six projects about one question: if you had to rebalance a portfolio every day, what rule would
you use? Then two more that went elsewhere: a deep-learning turning-point detector, and a
forecast-based reversion strategy that failed.

Four of the first six are published methods reimplemented from the paper with one deliberate
change each. One is a machine-learning alternative. One is the shared plumbing.

## The projects

| Project | In one sentence | Outcome |
|---|---|---|
| [01-adaptive-robust-mean-reversion](<01-adaptive-robust-mean-reversion/README.md>) | buy what has fallen, with a defensive optimiser that survives a noisy estimate | works, the most stable of the four |
| [02-recursive-least-squares-exponential-gradient](<02-recursive-least-squares-exponential-gradient/README.md>) | predict tomorrow with a regression that updates itself, then drift money toward the winners | works, the simplest baseline |
| [03-recursive-ols-with-robust-optimisation](<03-recursive-ols-with-robust-optimisation/README.md>) | combine the forecast from 02 with the allocation from 01 | works, comparable to its parents |
| [04-adaptive-recursive-ols-ewma](<04-adaptive-recursive-ols-ewma/README.md>) | the hybrid with self-tuning parameters | did not work, worse than constant parameters |
| [05-xgboost-technical-signals](<05-xgboost-technical-signals/README.md>) | classify the market regime with boosted trees instead of optimising weights | superseded by a private model |
| [06-shared-tools](<06-shared-tools/README.md>) | price download and performance metrics used by all of the above | utilities |
| [07-extrema-detection-strategy](<07-extrema-detection-strategy/README.md>) | predict turning points in the Hang Seng Index with deep learning, in five stages | abandoned at the last stage |
| [08-dmd-reversion](<08-dmd-reversion/README.md>) | trade the gap between price and a model forecast, and expect reversion | did not work, and the folder explains why |

## The arc of 01 to 04

02 is the prediction half and 01 is the allocation half. 03 joins them, and 04 adds a
self-tuning layer that made everything worse.

That progression is the interesting part, and it goes the opposite way from what you would
expect: the simplest model is not the worst, and adding adaptivity to a weak signal mostly
adds noise.

## 07, a different kind of question

07 stops asking what to hold and asks when to be in the market at all, using a recurrent
network to spot turning points. It has its own README with the five stages, and it is the
largest single piece of work in this repository. Read
[05-engines](<07-extrema-detection-strategy/05-engines/README.md>) first.

## 08, the most complete negative result

08 starts from yet another premise: forget optimising weights, can the movement of prices be
forecast at all? It builds the full pipeline, tests it properly, and concludes no.

It is the most fully documented folder here: a notebook with saved outputs, a detailed README,
and a test suite. Read it for the diagnostic rather than the strategy.

## Running any of them

Each project README has the exact command. They are independent, with no shared install:

    pip install numpy pandas scipy yfinance matplotlib quantstats
    cd 01-adaptive-robust-mean-reversion
    python "Adaptive_Mean_Reversion_Trading_Algo_(Tsang_et_al).py"

## Credit

Tsang, Sit & Wong (2025) and Li, Zhang & Zheng (2026) are the two base models for 01 to 04; the
modifications are mine. 07 follows Fang et al. (2024) for the distillation stages. Full
citations are in the repository README. The framing of the group follows Li & Hoi (2014), whose survey is the standard entry point to this literature.
