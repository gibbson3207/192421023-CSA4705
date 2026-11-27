x

IDLE Editor — Question 79

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

from sklearn.mixture import GaussianMixture

from sklearn.preprocessing import StandardScaler

customers = np.array([

(20, 2],

(22, 3],

fis,

1),

(25, 2],

[80, 8],

(85, 9],

(78, 7],

(90, 9],

[45, 5],

(50, 4],

(48, 6],

(52, 5]

1, dtype=float)

10

11

X = StandardScaler().fit_transform(customers)

12

gmm

GaussianMixture(n_components=3, random_state=42

13

gm. fit (X)

14

15

labels = gmm.predict(X)

16

probabilities

=

=

gmm.predict_proba(X)

7

18

print(”

ustomer cluster labels

labels)

19

print("Membership probabilities:

20

print(np.round(probabilities, 3))
