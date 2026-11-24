# DMD reversion, and the test that killed it

One sentence: trade the gap between price and a model forecast, expect the price to come back
to it, and find out that the forecast has no idea which way anything is going.

## The idea

A model makes a forecast of tomorrow's return for every stock. If a stock's price is below its
forecast, it is cheap relative to the model and should be bought. If it is above, it should be
sold. The profit is supposed to come from the price closing the gap.

The forecast comes from dynamic mode decomposition: take the last year of returns for a
group of stocks, work out the linear rule that turns one day's cross-section into the next day's,
and apply it to today.

It sounds sensible. It is not what happens, and this project is the four-week test that
established why.

## What it found

**The forecast has no direction.** Its sign is right 49.7 per cent of the time, at every
confidence threshold. A rule that simply says "everything goes up" scores 52.9 per cent. So
the model is not weakly informative, it is uninformative.

**The forecast does measure volatility.** Ignore the sign and look only at the size. Big
forecasts really do precede big moves, with a rank correlation of 0.29 to 0.33 against future
realised volatility. That is a usable risk indicator and a useless trading signal, which are
two different products.

**The cost makes it hopeless anyway.** A trade is scored as a win when its gross return
exceeds 5 per cent, and the cost assumed is 2 per cent per round trip. Under that contract a
win nets 3 per cent and a loss costs 7, so a strategy needs a 70 per cent win rate before it
makes a penny. The four variants reached 43 to 52 per cent.

**Full-rank DMD is an interpolator.** With more stocks than days in the window, the fitted
rule has as many degrees of freedom as it has observations, so it reproduces the window exactly
and forecasts nothing. This is the single most important technical point in the project, and
the notebook demonstrates it: in-sample fit 1.0000 at full rank, 0.07 at the 20 the demo uses.

## The four variants

Close and open price series, long and short sides. They share one pipeline: forecast, then two
thresholds drawn at random on a validation period, then the top candidates held for 20
sessions with one position per stock.

## Results on synthetic data

The repository cannot ship the real panel, so everything here runs on a generator that makes
its own market. Results are reproducible and meaningless; they exist to show the machinery.

Pure noise, nothing planted:

    variant       trades      win     gross       net
    close_long        38    28.9%     0.51%    -1.49%
    close_short       51    43.1%     3.34%     1.34%
    open_long        114    29.8%    -0.69%    -2.69%
    open_short       136    35.3%     0.16%    -1.84%

Read the close_short row again. There is no signal in that data at all, and one variant still
returns 1.34 per cent. That is what luck looks like at fifty trades, and it is why the
diagnostic matters more than the backtest.

The same code on data with a planted reversal:

    variant       trades      win     gross       net
    close_long       144    29.2%     0.86%    -1.14%
    close_short      169    31.4%     1.27%    -0.73%
    open_long         50    32.0%     0.30%    -1.70%
    open_short        59    27.1%     0.22%    -1.78%

The signal is findable there, and the best variant still loses to the cost.

## What is in the folder

| File | What it is |
|---|---|
| notebook.ipynb | the guided walkthrough, with its outputs saved, including the rank demonstration |
| dmd_reversion/pipeline.py | forecast, thresholds and portfolio, all of it about 150 lines |
| dmd_reversion/synthetic.py | the market generator, with an optional planted signal |
| dmd_reversion/dmd.py | the forecast itself, 18 lines |
| dmd_reversion/diagnostics.py | the sign-accuracy and rank-correlation tests |
| run_demo.py | runs the four variants from the command line |
| tests/test_pipeline.py | 14 checks, including the rank-interpolation condition |

## Running it

    pip install -r requirements.txt
    python run_demo.py                     # four variants on noise
    python run_demo.py --signal reversal   # with a planted edge
    python run_demo.py --quick             # faster
    python tests/test_pipeline.py          # 14 checks

Or open notebook.ipynb, which is self-contained.

## Why it is worth reading

Because the diagnostic generalises. Before tuning any signal, check whether its sign is right
more often than a coin flip, and check what a 5 per cent target with a 2 per cent cost demands
of a win rate. Both are one line of code, and both would have saved most of this project.

## Credit

Dynamic mode decomposition follows Schmid (2010) and Tu et al. (2014). The trading framing and
the negative result are mine.
