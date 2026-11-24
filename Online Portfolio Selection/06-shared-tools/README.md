# Shared tools

One sentence: the two small utilities that every algorithm in this group needs, kept in one
place instead of copied five times.

## What is here

| File | What it does |
|---|---|
| data_ingestion.py | downloads daily prices for a list of tickers from Yahoo Finance and caches them to a CSV, so repeated runs do not hit the network |
| performance_analysis.py | turns a series of portfolio values into the standard performance numbers: annual return, volatility, Sharpe, Sortino, maximum drawdown and Calmar |

Both are plain functions, not a package. The usual pattern is to copy the file next to the
script that needs it.

## Why it is separate

Each of the five algorithms above needs the same two things. Keeping one copy means a fix to
the data download or to the metric definitions propagates, instead of being applied in one
project and forgotten in four.

## Running it

Nothing to run directly. Import or copy the functions:

    from data_ingestion import get_market_data
    from performance_analysis import calculate_metrics
