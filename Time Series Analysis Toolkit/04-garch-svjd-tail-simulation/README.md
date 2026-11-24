# The tail of a single stock

One sentence: simulate one equity's risk with two layers of volatility, so that the extremes
come out the right size instead of being smoothed away.

## The problem

The standard textbook model, geometric Brownian motion, assumes volatility is constant. Real
markets cluster: calm weeks follow calm weeks and violent weeks follow violent ones. A model
with constant volatility therefore produces too few extreme days, and for a small, illiquid
stock where a handful of days dominate the year, that error is large enough to make any risk
number meaningless.

## The approach

Two layers. A GARCH(1,1) process (a standard model in which today's volatility depends on
yesterday's shock and yesterday's volatility) sets the scale. On top of that, a jump diffusion
with stochastic volatility adds sudden discontinuous moves.

The output is a distribution of where the price could be, with the up and down quantiles that
a position-sizing decision actually needs.

## Running it

    pip install numpy pandas scipy matplotlib yfinance
    python "Equity Price Simulation (GARCH, SVJD).py"

## Result

Produces visibly fatter tails than geometric Brownian motion. The comparison between the two
is the point of the file.
