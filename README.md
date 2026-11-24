# Learning Projects

Twenty-one small research projects in quantitative finance, time series analysis and generative
modelling, written between 2025 and 2026.

Every project lives in its own folder with a README that explains what it does, what it found
and how far it got. **You do not need to read any code to follow this repository.**

Most of it runs on public data from Yahoo Finance and was written on Google Colab, so a reader
with Python and an internet connection can run any of it.

## The three groups

| Group | Subject | Projects | How far it got |
|---|---|---|---|
| [Extreme-Value-Aware Synthetic Data Generator for Stress Testing](<Extreme-Value-Aware Synthetic Data Generator for Stress Testing/README.md>) | generating fake market histories that still contain real crashes | 2 | research prototype, working |
| [Online Portfolio Selection](<Online Portfolio Selection/README.md>) | algorithms that rebalance a portfolio every day, plus a turning-point detector | 12 | finished, with two honest negative results |
| [Time Series Analysis Toolkit](<Time Series Analysis Toolkit/README.md>) | small, single-question utilities | 7 | finished |

## How to read this repository

Start with a group README. Each has a table of its projects, one line each, so you can pick
what interests you and open only that folder.

Every project README follows the same shape:

1. **One sentence** saying what it is and whether it worked.
2. **The idea**, in plain language, with the jargon explained the first time it appears.
3. **The result**, in words rather than numbers.
4. **How to run it**, for anyone who wants to.

## If you only read four things

- **[Synthetic data with real crashes](<Extreme-Value-Aware Synthetic Data Generator for Stress Testing/01-temporal-conv-autoencoder/README.md>)** —
  the most ambitious project here: a generative model built specifically to produce crashes of
  the right size.
- **[DMD reversion](<Online Portfolio Selection/08-dmd-reversion/README.md>)** — the most
  complete negative result: a full pipeline, a diagnostic that killed it, and a clear
  explanation of the cost arithmetic that makes it hopeless.
- **[The adaptive parameter experiment that failed](<Online Portfolio Selection/04-adaptive-recursive-ols-ewma/README.md>)** —
  a plausible idea, a clear negative result, and the reason why it failed.
- **[Turning point engine](<Online Portfolio Selection/07-extrema-detection-strategy/05-engines/README.md>)** —
  the closest this repository came to a working trading strategy, and why it is not one.

## Notes

These are research notebooks and scripts, not a library. Some are hard-coded, some expect a
GPU, and none is maintained. Nothing here is investment advice.

Several of them are publicly releasable side products of larger private projects; access to
those is available on request.

## References

Methods used in this repository, alphabetical by first author. Each project README credits the
specific ones it relies on.

- Arjovsky, M., Chintala, S., & Bottou, L. (2017). Wasserstein GAN. arXiv:1701.07875.
  [paper](https://arxiv.org/abs/1701.07875)
- Bai, S., Kolter, J. Z., & Koltun, V. (2018). An Empirical Evaluation of Generic Convolutional
  and Recurrent Networks for Sequence Modeling. arXiv:1803.01271.
  [paper](https://arxiv.org/abs/1803.01271)
- Chang, K., & Sapsis, T. P. (2025). Extreme Event Aware (η-) Learning. arXiv:2510.19161.
  [paper](https://arxiv.org/abs/2510.19161)
- Chen, T., & Guestrin, C. (2016). XGBoost: A Scalable Tree Boosting System. Proceedings of the
  22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 785-794.
  [paper](https://doi.org/10.1145/2939672.2939785)
- Fang, L., Chen, Y., Zhong, W., & Ma, P. (2024). Bayesian Knowledge Distillation: A Bayesian
  Perspective of Distillation with Uncertainty Quantification. Proceedings of the 41st
  International Conference on Machine Learning, PMLR 235.
  [paper](https://proceedings.mlr.press/v235/fang24a.html)
- Gulrajani, I., Ahmed, F., Arjovsky, M., Dumoulin, V., & Courville, A. (2017). Improved Training
  of Wasserstein GANs. Advances in Neural Information Processing Systems 30.
  [paper](https://arxiv.org/abs/1704.00028)
- Helmbold, D. P., Schapire, R. E., Singer, Y., & Warmuth, M. K. (1998). On-Line Portfolio
  Selection Using Multiplicative Updates. Mathematical Finance, 8(4), 325-347.
  [paper](https://doi.org/10.1111/1467-9965.00058)
- Li, B., & Hoi, S. C. H. (2014). Online Portfolio Selection: A Survey. ACM Computing Surveys,
  46(3), 1-36. [paper](https://doi.org/10.1145/2512962)
- Li, J., Zhang, Y., & Zheng, X. (2026). Dynamic mode decomposition for online portfolio
  selection task. European Journal of Operational Research, 328(1), 349-365.
  [record](https://econpapers.repec.org/article/eeeejores/v_3a328_3ay_3a2026_3ai_3a1_3ap_3a349-365.htm)
- Schmid, P. J. (2010). Dynamic mode decomposition of numerical and experimental data. Journal of
  Fluid Mechanics, 656, 5-28.
- Tsang, M. Y., Sit, T., & Wong, H. Y. (2025). Adaptive robust online portfolio selection.
  European Journal of Operational Research, 321(1), 214-230.
  [record](https://econpapers.repec.org/article/eeeejores/v_3a321_3ay_3a2025_3ai_3a1_3ap_3a214-230.htm)
- Tu, J. H., Rowley, C. W., Luchtenburg, D. M., Brunton, S. L., & Kutz, J. N. (2014). On Dynamic
  Mode Decomposition: Theory and Applications. Journal of Computational Dynamics, 1(2), 391-421.
  [paper](https://arxiv.org/abs/1312.0041)
- Welling, M., & Teh, Y. W. (2011). Bayesian Learning via Stochastic Gradient Langevin Dynamics.
  Proceedings of the 28th International Conference on Machine Learning, 681-688.
- Zhao, J., Kim, Y., Zhang, K., Rush, A. M., & LeCun, Y. (2018). Adversarially Regularized
  Autoencoders. Proceedings of the 35th International Conference on Machine Learning, PMLR 80.
  [paper](https://proceedings.mlr.press/v80/zhao18b.html)

## About me

CUHK BSc Risk Management Science. Interested in quantitative research, market microstructure and
generative models for financial data.
