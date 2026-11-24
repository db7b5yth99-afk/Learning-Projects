# End-to-end engines, and the closest thing to a working strategy

One sentence: the stages assembled into something that actually trades, ending with the version
that sizes its positions by how confident the model is.

## What is here, in order

| File | What it is |
|---|---|
| GRU_Fusion_Extrema_Detection_Engine_Version_1.ipynb | first end-to-end assembly: data, labels, model, execution |
| GRU_Fusion_Extrema_Detection_Engine_Version_2.ipynb | second version, tidied and faster |
| Turning_Point_Analysing_Engine.ipynb | single-engine model with Bayesian uncertainty and adaptive execution |

## Read this one

Turning_Point_Analysing_Engine.ipynb.

It is the only version that carries the uncertainty from stage 02 all the way into position
sizing: take the trade when the model is confident, skip it when it is not. That was the whole
point of the uncertainty work, and this is where it is actually used.

## The honest summary

This is the closest the folder came to a working strategy, and it is not one. The labels are
built with future data, so the reported accuracy is an upper bound on what the features can
express, not an expected return. Turning it into something real would need causally derived
labels and a full out-of-sample test, which is exactly what the later work in this repository
does for other signals.

## Running it

Colab with a GPU.

## Credit

Uncertainty estimation follows Welling & Teh (2011); the distillation stages follow Fang et al.
(2024).
