# Cycles over a moving window

One sentence: decompose a price series into cycles with a Fourier transform, but redo the
decomposition as you move through time so the cycles are allowed to change.

## The idea

A fast Fourier transform (FFT) takes a series and reports how much of it is explained by
cycles of each length: a weekly rhythm, a monthly rhythm, a yearly one. Done once over the
whole history it assumes those rhythms never change, which is wrong for markets.

This project slides the window forward and recomputes, so you can see which cycles are
present at each point in time and how their strength drifts.

## The part worth reading

Reconstructing a series from its cycles produces something perfectly periodic, and therefore
obviously fake. The file applies a Gaussian fade-in and fade-out at the edges of each window,
which turns that reconstruction into something that behaves like a price path. If you wanted
to use Fourier output for scenario generation, that is the detail that makes it usable.

## Running it

    pip install numpy pandas scipy matplotlib sktime yfinance
    python "A Dynamic FFT Implementation on TSA.py"

## Result

A visualisation tool with one genuinely useful trick in it, the fade. Not a trading signal.
