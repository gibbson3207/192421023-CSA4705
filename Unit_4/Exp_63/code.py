x

IDLE Editor — Question 63

fa)

File

Edit

Format

Run

Options

Window

Help

Python 3

|

IDLE Editor

import numpy as np

from sklearn.metrics import precision score, recall_score, fl_score

actual = np.array({®, 1, 2, 1, ®, 2, 1, 61)

predicted

np.array([0, 1, 1, 1, 0, 2, 0, 8])

print ("Precision

precision _score(actual, predicted,

average="macro"))

print("

fecal

acr

"))

recall_score(actual, predicted, average:

.

10

print(”

1-score:", f1_score(actual, predicted, average:

macro"))
