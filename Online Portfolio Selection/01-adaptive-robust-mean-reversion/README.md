# Adaptive robust mean reversion

One sentence: a portfolio strategy that buys what has fallen and expects it to come back,
with a defensive optimiser that keeps the position sane when the estimate is noisy.

## The idea

Mean reversion is the claim that a price which has moved far from its recent average tends
to move back. If that is true, you want to hold the assets that are currently cheap and
avoid the ones that are expensive.

The difficulty is that the signal is noisy. A naive optimiser will put everything into
whatever looks cheapest today, which is exactly how a portfolio blows up. This project
solves a robust version of the allocation problem instead: it assumes the estimate is wrong
by some amount and picks the weights that still work in that case. Trading costs enter the
objective directly, so the optimiser knows that rebalancing is not free.

## What I changed from the paper

The published model calibrates its parameters once over a fixed window. This version
re-estimates them with an exponentially weighted moving average, so recent weeks count more
than distant ones, and it allows the optimiser to become more aggressive when the reversion
signal has recently been working.

## Result

Runs end to end and produces a wealth curve and a performance table. Of the four algorithms in
this group it is the most stable, and the one to read first.

## Running it

    pip install numpy pandas scipy yfinance
    python "Adaptive_Mean_Reversion_Trading_Algo_(Tsang_et_al).py"

It downloads daily prices from Yahoo Finance, so it needs a network connection. The first run
takes a couple of minutes.

## Credit

Tsang, M. Y., Sit, T., & Wong, H. Y. (2025). Adaptive robust online portfolio selection.
European Journal of Operational Research, 321(1), 214-230.
