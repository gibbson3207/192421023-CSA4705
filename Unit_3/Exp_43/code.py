x

IDLE Editor — Question 43

a

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

1

import numpy as np

2 from sklearn.metrics import (accuracy score, precision score,

recall_score, fl_score,

confusion_matrix)

actual = np.array({®, 6, 1, 1, 8, 1, ®, 11)

predicted

np-array({@, 1, 1, 1, 0, 6, 0,

1))

print(”

\ccurac’

, accuracy score(actual, predicted) )

10

print("

recision

, precision_score(actual, predicted))

11

print("

fecal

recall_score(actual, predicted) )

12

print("

1-scoré

» fl_score(actual, predicted))

13

print("Confusion matrix:")

14

print(confusion_matrix(actual, predicted) )
