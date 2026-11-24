# Making the detector sharper by training it against teachers

One sentence: two attempts to improve the detector by distilling from more than one teacher,
rather than by making the network bigger.

## The idea

Distillation trains a small model to imitate a larger or better-informed one. Here the
teachers are the same data seen at different smoothings and horizons, so the student is pushed
toward the shape rather than toward one particular definition of a turning point.

Two versions are in this folder.

| File | Idea |
|---|---|
| CBKD_GRUM.ipynb | conditional distillation with a second engine forecasting risk, so position size can respond to it |
| CBKD_GRUM_Dual.ipynb | multi-frequency distillation: two teachers at different horizons and a three-term loss |

## What to look at

The three-term loss in the dual version. The terms pull in different directions, and the
balance between them is where the results are won or lost. That weighting is also why this
stage was hard to iterate on.

## Result

Heavier to train than the baseline and harder to tune. It was a step on the way to the
cross-asset stage rather than a destination; the folder README explains why the line stopped.

## Running it

Colab with a GPU.

## Credit

The distillation view follows Fang, Chen, Zhong & Ma (2024).
