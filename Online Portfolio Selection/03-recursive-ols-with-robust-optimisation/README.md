# Recursive least squares with robust optimisation

One sentence: take the forecast from project 02 and the defensive allocation from project 01,
and put them in the same program.

## The idea

The two previous projects each solved half of the problem. Project 02 is good at saying what
will happen but allocates naively. Project 01 allocates defensively but its signal is a simple
mean reversion.

The reasoning here is that the halves are complementary, not competing: the forecast is where
the return comes from and the robust objective is where the risk control comes from. So this
project runs the recursive forecast and feeds it into the robust optimiser.

## Result

Works, and performs comparably to its two parents. It is also the base that project 04
extends, which is where the useful negative result lives.

## Running it

    pip install numpy pandas scipy yfinance
    python "Robust_Optimized_Recursive_OLS_Trading_Algo_(Hybrid).py"

## Credit

Li, Zhang & Zheng (2026) for the prediction step, Tsang, Sit & Wong (2025) for the robust
allocation.
