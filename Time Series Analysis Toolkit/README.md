# Time Series Analysis Toolkit

Seven small, self-contained projects. Each one asks a single question, answers it in under 200
lines, and has its own README.

## Projects

| Folder | Question | Approach |
|---|---|---|
| [01-dmd-index-forecasting](<01-dmd-index-forecasting/README.md>) | can a cross-section of ETFs forecast tomorrow's S&P 500 close? | dynamic mode decomposition |
| [02-windowed-fft-cycles](<02-windowed-fft-cycles/README.md>) | which cycles are present, and how do they drift? | windowed FFT with Gaussian fade |
| [03-cycle-bull-bear-indicator](<03-cycle-bull-bear-indicator/README.md>) | bull or bear, by period length? | FFT over 1 month to all history |
| [04-garch-svjd-tail-simulation](<04-garch-svjd-tail-simulation/README.md>) | what does the tail of one equity look like? | GARCH(1,1) plus jump diffusion |
| [05-portfolio-risk-monte-carlo](<05-portfolio-risk-monte-carlo/README.md>) | what does the tail of a portfolio look like? | correlated GBM Monte Carlo |
| [06-extreme-event-return-generator](<06-extreme-event-return-generator/README.md>) | can a network generate paths that keep extreme events? | semi-supervised generator, EVT injection |
| [07-gru-path-generator](<07-gru-path-generator/README.md>) | can a plain GRU generate plausible paths? | recurrent generator with stochastic injection |

## How they relate

Projects 01 to 03 are about seeing structure in a series: a linear operator, a cycle
decomposition, and a cycle indicator. Projects 04 and 05 are about the tail. Projects 06 and
07 are about generating data, and they are the ones that led somewhere: 07 concludes that a
plain GRU cannot produce regime change on its own, and 06 is the response, injecting extremes
from a fitted distribution. That line of thinking became the Extreme-Value-Aware folder in
this repo.

## Running

    pip install numpy pandas scipy matplotlib sktime yfinance

07 needs torch and was written on Colab.

## Known rough edge

02-windowed-fft-cycles/A Dynamic FFT Implementation on TSA has no file extension. It is a
Python script saved without one, so it will not open as Python until it is renamed to .py.
