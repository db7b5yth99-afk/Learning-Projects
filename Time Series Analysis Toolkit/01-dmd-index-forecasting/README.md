# Forecasting the S&P 500 with DMD

One sentence: a short experiment asking whether the way ETFs move together tells you anything
about where the S&P 500 closes tomorrow.

## The idea

Dynamic mode decomposition (DMD) is a linear method that learns how one day's cross-section
turns into the next. Give it a table where each column is a series and each row is a day, and
it finds the operator that advances the table by one step. Apply that operator to today and
you have tomorrow.

Here the columns are sector funds, smart-beta factor funds, and cross-asset macro series
(bonds, gold, dollar, oil), and the row being forecast is the S&P 500.

## What it shows

The forecast is far more sensitive to how many modes you keep than to which ETFs you include.
At full rank the operator simply memorises the window it was fitted on: the in-sample fit is
perfect and the out-of-sample forecast carries nothing. This is the same trap that shows up in
the bigger synthetic data project in this repository, and it is worth seeing in fifty lines.

## Running it

    pip install numpy pandas yfinance
    python "A DMD Approach for Index Prediction.py"

## Result

A teaching example, not a model. It is here because the failure is more instructive than most
successes.

## Credit

Dynamic mode decomposition is due to Schmid (2010), who introduced it for fluid flows, and the
formulation used here follows Tu et al. (2014).
