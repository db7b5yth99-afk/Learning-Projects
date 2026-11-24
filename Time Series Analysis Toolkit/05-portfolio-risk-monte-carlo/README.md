# The tail of a portfolio

One sentence: the same question as the single-stock project, asked of a whole portfolio.

## What it does

Simulates thousands of correlated price paths for every holding with geometric Brownian
motion, aggregates them into portfolio paths, and reports the distribution of the final value:
the expected outcome, the good and bad quantiles, and the probability of ending below a level
you care about.

## What it is good for

Position sizing and stop-loss decisions, which need a distribution rather than a point
forecast. It is fast and it is easy to explain to someone who has not seen a risk model before.

## Limitation

Geometric Brownian motion, so the tails are thin. If the left tail needs to be honest, the
single-stock simulation in the neighbouring folder is the better starting point. This file is
here as the simple version.

## Running it

    pip install numpy pandas matplotlib yfinance
    python "Portfolio Risk Monitor (GBM).py"

## Result

Works and is short. Treat the downside number as optimistic for anything with real tail risk.
