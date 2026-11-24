# Synthetic market data with real crashes, using a convolutional network

One sentence: generate fake-but-plausible market histories that include crashes of realistic
size, so a strategy can be tested on bad days that never happened in the sample.

## The problem

Train a generative model on daily returns and it learns ordinary days well and extreme days
hardly at all, because extremes are rare and the model optimises for the average. The result
is synthetic data that looks smooth and is useless for stress testing, since the point of a
stress test is precisely the day the model never produces.

## The approach, in three parts

**1. Read the series with convolutions, not recurrence.** A temporal convolutional network
processes the whole window at once rather than step by step. For noisy financial returns that
is better: nothing gets washed out along long sequences, and no bias is given to the most
recent observations.

**2. Inject the extremes from a fitted distribution.** Fit a generalised Pareto distribution
(the standard tool for the size of rare events) to the historical tail, then sample shocks
from that fit. The crash is the right size because it was measured, not because someone chose
it.

**3. Let a discriminator decide which shocks to keep.** A Wasserstein GAN with a gradient
penalty scores candidate paths and rejects the ones that look synthetic. The penalty is faded
in gradually during training, because if you weight the tail heavily from the start the model
produces only extremes and never learns ordinary days.

## Result

A working research prototype. The notebook reports synthetic tail statistics against the
historical ones, and that comparison is the result: the generated paths reproduce the
frequency and the size of large moves rather than just the average.

## Running it

Colab with a GPU. The notebook mounts Google Drive and saves weights to
/content/drive/MyDrive/STSG_Models, so a local run needs those paths edited.

    pip install torch numpy pandas scipy matplotlib yfinance

## Credit

The encoder design follows Bai, Kolter & Koltun (2018) on temporal convolutional networks. The
adversarial training uses the Wasserstein objective of Arjovsky, Chintala & Bottou (2017) with
the gradient penalty of Gulrajani et al. (2017). Extreme-value injection follows Chang & Sapsis
(2025).
