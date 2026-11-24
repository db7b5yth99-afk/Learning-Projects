# Synthetic market data from an adversarial autoencoder

One sentence: the same stress-testing pipeline as its sibling, with a different network
architecture underneath and a longer, more thorough implementation.

## Why a different architecture

An adversarially regularised autoencoder compresses the data into a small latent code and
reconstructs it, and trains the code to follow a chosen prior rather than collapsing to a
handful of patterns. The idea comes from text generation, where the latent space has to
represent very different kinds of sentence without averaging them.

The hope when applied to returns is that the latent space stays expressive across regimes, so
a crash and a quiet week are not blended into the same mediocre day.

## What is inside

Data preparation, the autoencoder, the extreme-value tail engine, the adversarial training
loop, and a comparison of synthetic versus historical tail statistics. It is the longer of the
two notebooks in this folder.

## Result

A research prototype. The tail comparison is the result worth reading; the architecture is the
experiment.

## Running it

Colab with a GPU, same Drive paths as the sibling.

    pip install torch numpy pandas scipy matplotlib yfinance

## Credit

Zhao, Kim, Zhang, Rush & LeCun (2018) for the adversarially regularised autoencoder. Chang &
Sapsis (2025) for the extreme-value injection.
