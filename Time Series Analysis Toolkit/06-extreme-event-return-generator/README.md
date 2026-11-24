# Generating returns that keep their extremes

One sentence: a generator of synthetic return paths that is explicitly built to produce
crashes and rallies of realistic size.

## The problem it answers

Train a generative model on returns and it will learn the ordinary days very well and the
extreme days hardly at all, because extremes are rare and the model optimises for the average.
The result is synthetic data that looks smooth and is useless for stress testing: the whole
point of a stress test is the day the model never generates.

## The approach

A network learns the structure of the return process in a semi-supervised way, and the
extreme moves are injected from a fitted tail distribution rather than left to the noise term.
Injecting from a fitted distribution means the size of the injected crash is calibrated to
history instead of being an arbitrary choice.

## Why it is here

This is the foundation for the Extreme-Value-Aware Synthetic Data Generator folder in this
repository, which takes the same idea and replaces the network with a modern architecture.
If you want the idea without the machinery, read this file first.

## Credit

Chang, K., & Sapsis, T. P. (2025). Extreme event aware (η-) learning. arXiv:2510.19161.
The original work is on event sequences; adapting it to a continuous time series is the part
that is mine.
