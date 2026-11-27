x

IDLE Editor — Question 76

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

from sklearn.preprocessing import StandardScaler

from sklearn.decomposition import FactorAnalysis

# Column:

electronics, clothing, groceries, books

purchases

np-array([

[8, 2, 3, 7],

(7, 3, 2, 8],

[2, 8, 7, 2],

(3, 7, 8, 3],

(9, 2, 2, 8],

[2, 9, 8,

1),

(7, 3, 3, 71,

[3, 8, 7, 2]

10

1, dtype=float)

11

12

X = StandardScaler() .fit_transform(purchases)

13

‘a = FactorAnalysis(n_components=

, random_state=42)

14

=

=

customer_factors

fa.fit_transform(X)

15

16

print("Factor loadings

7

print(n

-round(fa.components_, 3))

18

print(”

ustomer latent factor scores

19

print(np.round(customer_factors, 3))
