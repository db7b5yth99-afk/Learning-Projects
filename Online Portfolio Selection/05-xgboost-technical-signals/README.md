# XGBoost on technical signals

One sentence: a machine-learning alternative to the optimiser-based algorithms, which tries
to classify the market regime instead of solving for weights.

## The idea

The other four projects in this group decide what to hold by solving an optimisation problem.
This one takes a different route: compute a handful of standard technical indicators, turn
them into discrete states, and let a tree-based model learn which state tends to precede a
good or bad three-day stretch. The position then follows the predicted state.

XGBoost is gradient-boosted decision trees, a workhorse model for tabular data.

## The features

Volume, 5-day and 20-day moving averages, the relative strength index (a momentum oscillator
between 0 and 100), and the fast stochastic oscillator (where today's close sits inside its
recent range).

## Result

Superseded. A hybrid deep-learning plus Bayesian model inside the private repository gave
better results, so this line was not developed further. It is kept because the feature
engineering and the regime framing are still readable, and because it is the shortest example
of a supervised approach in this repository.

## Running it

The file was exported from a notebook and takes its dependencies from a pip line at the top.
Install those first, then run it as a script.

    pip install xgboost TA-Lib mplfinance scikit-learn yfinance
    python xgboost_discrete.py

## Credit

XGBoost is Chen & Guestrin (2016).
