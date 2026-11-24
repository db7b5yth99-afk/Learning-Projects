# Adaptive recursive OLS with EWMA parameters

One sentence: the hybrid from project 03 with a self-tuning layer added, and the answer is
that the layer made it worse.

## The idea

Project 03 holds its parameters fixed. The obvious next step is to let them adapt: re-estimate
the lookback window and the risk-aversion coefficient from recent performance, so the model
follows the regime it is in.

That is the idea. It sounds right, and it is what a lot of practitioner writing recommends.

## Result: it did not work

Returns were worse than the constant-parameter hybrid, and worse than the plain mean-reversion
model, across the windows tested.

The likely reason is that the signal being adapted to is weak. When the thing you are
forecasting is close to noise, recent performance tells you more about luck than about the
next month, so the parameters drift toward whatever happened to work lately. Adaptivity helps
only when the underlying process genuinely changes, and this one mostly does not.

Kept in the repository because a clear negative result from a plausible idea is worth more
than another positive one, and because this failure mode is easy to fall into.

## Running it

    pip install numpy pandas scipy yfinance
    python "Adaptive_Recursive_OLS_(Hybrid).py"

## Credit

Li, Zhang & Zheng (2026) and Tsang, Sit & Wong (2025) for the two halves. The adaptive layer
is mine.
