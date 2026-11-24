# Recursive least squares with exponential-gradient allocation

One sentence: predict tomorrow's return with a regression that updates itself every day, then
shift money toward whatever it likes best, gradually rather than all at once.

## The idea

Two decisions have to be made every day: what you think each asset will return, and how much
of each to hold.

The forecast comes from a regression that is updated one observation at a time instead of
being refitted from scratch. That is cheap and it adapts slowly, which is usually what you
want for prices.

The allocation is an exponential-gradient rule: each asset's weight is nudged up when it
performs well and down when it does not, but never to zero and never to everything. That
keeps the portfolio diversified without a separate risk model.

## A note on the paper's title

The reference is titled around dynamic mode decomposition, but there is no DMD step in this
file. What is implemented is recursive multiple regression, updated with the Sherman-Morrison
identity, allocated by an exponential gradient. Worth knowing if you came here looking for
DMD.

## Result

Works, and it is the simplest of the four algorithms in this group. A good baseline before
looking at the two hybrid versions.

## Running it

    pip install numpy pandas yfinance
    python "Recursive_OLS_Algo_(Li_et_al).py"

## Credit

Li, J., Zhang, Y., & Zheng, X. (2026). Dynamic mode decomposition for online portfolio
selection task. European Journal of Operational Research, 328(1), 349-365.

The allocation rule is the multiplicative-updates scheme of Helmbold, Schapire, Singer &
Warmuth (1998), which is where the exponential gradient in online portfolio selection comes from.
