# Extreme-Value-Aware Synthetic Data Generator for Stress Testing

Generative models for market data that keep the fat tails, so the output can be used for
stress testing instead of only for simulation.

## The problem

A generator trained on returns usually reproduces the body of the distribution and loses the
tails, which is exactly the part a stress test exists to probe. A model that cannot produce a
bad day is not a stress testing tool.

The approach in both projects below: fit the empirical tail with a generalised Pareto
distribution, sample extreme moves from that fit, and use a discriminator to decide whether
the resulting path still belongs to the historical manifold. The extreme is injected rather
than hoped for.

## Projects

| Folder | Encoder | What is different |
|---|---|---|
| [01-temporal-conv-autoencoder](<01-temporal-conv-autoencoder/README.md>) | causal TCN | no recurrence, so no recency bias and the high-frequency structure survives |
| [02-adversarial-autoencoder-generator](<02-adversarial-autoencoder-generator/README.md>) | ARAE | adversarial latent regularisation, so the latent space stays expressive across regimes |

Both share the same four phases: data, tail engine, generator, organiser. The first is the
shorter and better organised of the two; the second is the longer and more thorough.

## Running

Colab with a GPU. Both notebooks mount Google Drive and save weights to
/content/drive/MyDrive/STSG_Models, so a local run needs those paths edited first.

    pip install torch numpy pandas scipy matplotlib yfinance

## Credit

Zhao, Kim, Zhang, Rush & LeCun (2018) for the ARAE structure. Chang & Sapsis (2025) for
extreme event aware (η-) learning, which is the source of the EVT injection scheme.
