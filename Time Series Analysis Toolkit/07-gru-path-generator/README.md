# Can a plain GRU generate a market path?

One sentence: a test of whether a standard recurrent network can generate plausible return
paths, and the answer is that it cannot produce a regime change on its own.

## What it does

Trains a GRU (a recurrent network, the kind that reads a sequence one step at a time and keeps
a memory) to predict the next return from the recent past, then runs it recursively to
generate long paths. Two kinds of randomness are injected: normal noise added to the input,
and log-normal shocks multiplied into the output to force occasional regime changes.

## The finding

Without the injection, the generated paths look plausible in a chart and contain no crashes.
The network has learned to continue whatever momentum it sees and has no mechanism for
producing a break in behaviour, because breaks are rare and it was trained to minimise average
error.

The conclusion is written into the notebook, and it is the useful part: generating market data
is not a regression problem, it is a problem of getting the tail right. Injection is not a
hack, it is the modelling decision that matters.

That conclusion is what led to the extreme-event generators in projects 06 and in the
Extreme-Value-Aware folder.

## Running it

Colab with a GPU.

    pip install torch numpy pandas scipy matplotlib yfinance

## Result

A negative result with a clear mechanism. Worth reading for the conclusion even if you never
run it.
