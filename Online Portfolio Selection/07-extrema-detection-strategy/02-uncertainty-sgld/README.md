# Teaching the model to say when it is unsure

One sentence: a version of the detector that outputs not only a prediction but also how
confident it is, which turns out to be the most useful idea in this whole folder.

## Why uncertainty

A normal network gives one number and no way to tell a confident call from a guess. For a
trading rule that difference is everything: if a signal is right 55 per cent of the time, it
is only worth acting on if the wrong 45 per cent can be recognised and skipped.

## How it works

The network is trained with stochastic gradient Langevin dynamics, which keeps sampling the
weights instead of settling on one set. Each sample is a slightly different model, so running
the same input through many of them gives a spread. A tight spread means the model agrees with
itself; a wide one means it does not.

That spread is the uncertainty estimate, and it costs nothing extra at prediction time.

## What is here

| File | What it is |
|---|---|
| SGLD_GRU_Extrema_Detection_Model.ipynb | the model and the uncertainty estimate |
| SGLD_GRU_Extrema_Detection_Model_Specification.pdf | the written design |

## Result

The uncertainty estimate does separate the good predictions from the bad ones, which is the
finding the later stages build on. The final engine in stage 05 sizes its positions with it.

## Running it

Colab with a GPU.

## Credit

Stochastic gradient Langevin dynamics is Welling & Teh (2011). Using it here as an uncertainty
estimate for trading is the part that is mine.
