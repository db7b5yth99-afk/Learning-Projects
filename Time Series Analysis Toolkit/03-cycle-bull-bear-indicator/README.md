# Bull or bear, by cycle length

One sentence: for each lookback from one month to all history, print whether the index is in
the rising or falling part of its dominant cycle.

## What it does

For each period, download the S&P 500, take the log price, remove the long-run trend with a
spline, run an FFT on what is left, keep the strongest cycles, reconstruct, and look at which
way the reconstruction is pointing at the right-hand end. Print a plus for rising and a minus
for falling.

The point of the multiple periods is to see how the answer changes with the lens. A cycle
fitted to one month is mostly noise; a cycle fitted to thirty years is mostly trend.

## What it is not

Not a signal. The output flips depending on the window you choose, and the reconstruction is a
smooth curve that has no idea about tomorrow's news. It is a way of looking at a series, and
it is included because it is a clean, readable example of the technique.

## Running it

    pip install numpy pandas scipy matplotlib sktime yfinance
    python "Econ Trend Indicator (Fast Fourier).py"

## Result

Prints the table. Interpret with care.
