x

IDLE Editor — Question 32

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

import numpy as np

from sklearn.metrics import

log_loss, confusion matrix, accuracy score

actual = np.array([®, 0,

.

1, 6,

1))

=

=

probability

np-array([0.1

0.2, 0.8, 0.7, 0.3, 0.9])

predicted = (probability >=

0.5) .astype(int)

.

print(”

inary cross-entropy:

, round(log_loss(actual, probability), 4)

print("

\ccurac’

, accuracy score(actual, predicted)

10

print("Confusion matrix:")

11

print (confusion _matrix(actual, predicted)
