# Do three markets see a turning point before one does?

One sentence: test whether a turning point in the Hang Seng Index is easier to spot when the
S&P 500 and the FTSE are signalling the same thing at the same time.

## The idea

A reversal that several major markets are approaching at once is probably a stronger signal
than one that only the local index is approaching. The model combines features from three
markets, strictly aligned to the same trading day, and predicts the local turning points from
all of it.

## What is here

| File | What it is |
|---|---|
| GRU_CrossAsset_Fusion_Model_Specification.ipynb | the design and a working build |
| GRU_CrossAsset_Fusion_Model_Specification.pdf | the written specification |

## Why the project stopped here

Aligning three markets to the same day sounds trivial and is not: different holidays,
different closing times, and a feature set that triples. Training time grew to the point where
the loop of change, train, evaluate took long enough that iteration stopped being practical,
and the improvement was not proportional to the cost.

This is the stage where the compute bill, not the idea, ended the project.

## Running it

Colab with a GPU. The heaviest notebook in this folder.
