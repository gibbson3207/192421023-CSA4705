x

IDLE Editor — Question 74

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

from sklearn.decomposition import PCA, FastICA

from sklearn.preprocessing import StandardScaler

=

=

rng

np.random.default_rng(42)

s

np.c_[rng. laplace(siz

88), rng-uniform(-1, 1, 500)]

A

np.array({[1, 0.5],

[0.3,

11)

x

S@A.T

x

StandardScaler().fit_transform(X)

10

11

pca

=

=

PCA(n_components=2)

12

X _pca

pca.fit_transform(X)

13

ica

FastICA(n_component:

, random_state=42,

14

whiten:

=

unit-variance", max_iter=1000)

15

X_ica

=

ica.fit_transform(X)

16

7

print("PCA explained variance:", pca.explained_variance_ratio_)

18

print("

CA transformed shape

X_pca. shape)

19

print("

CA transformed shape

.

X_ica.shape)

20

print("PCA decorrelates; ICA seeks statistically independent components.")
