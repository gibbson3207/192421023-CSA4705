x

IDLE Editor — Question 77

a

File

Edit

Format

Run

Options

Window

Help

Python 3

I

IDLE Editor

import numpy as np

from sklearn.preprocessing import StandardScaler

from sklearn.decomposition import PCA, FactorAnalysis

from sklearn.metrics import mean_squared_error

rng

np.random.default_rng(42)

X = rng.normal(size=(200, 6))

XE:, 4] = XL:

0]*0.7 + X[:, 1]*0.2 + rng.normal(0, 0.2, 200)

X[:, 5] =X

21*0.8 + rng.normal(0, 0.2, 200)

10

X = StandardScaler() .fit_transform(X)

11

12

pca = PCA(n_components=3)

13

Z pca

=

=

pca.fit_transform(X)

14

=

=

reconstructed_pca

pca.inverse_transform(Z_pca)

15

16

‘a = FactorAnalysis(n_components=3, random_state=42

=

=

7

Zfa

fa.fit_transform(X)

18

reconstructed_fa = Z_fa @ fa.components_ + fa.mean_

19

.

20

print("PCA retained variance:", round(pca.explained_variance_ratio_.sum(), 3))

21

print("PCA reconstruction MSI

.

22

round(mean_squared_error(X, reconstructed_pca), 4))

23

print("Factor Analysis reconstruction MSI

.

24

round(mean_squared_error(X, reconstructed fa), 4))
