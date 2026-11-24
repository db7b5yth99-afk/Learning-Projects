# Baseline: a plain recurrent network

One sentence: find out what a simple model can do at this task before adding any machinery.

## What the task is

Given the recent history of the Hang Seng Index, say whether the current point is likely to
be a turning point (a local peak or trough). If that can be predicted, entries and exits can
be timed better than a fixed rule.

## What is here

A single sequential GRU (a recurrent network that reads the series one day at a time) trained
on labels produced by scanning the price for local extremes. Short notebook, no tricks.

## Why it matters

Every later stage in this folder claims to improve on something. This is that something. If
you only want to know whether the task is possible at all, this is the notebook that answers
it, and it is the fastest to run.

## The catch with the labels

The extremes are found with a centered moving average, which looks at days before and after the
point. That means the labels use future data. It is a legitimate way to teach a model to
recognise a shape, and it is not a tradeable signal; see the folder README for what that
implies for the numbers.

## Running it

Colab with a GPU.
