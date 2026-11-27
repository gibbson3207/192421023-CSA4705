x

IDLE Editor — Question 71

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

from sklearn

-datasets import load_breast_cancer

from sklearn

-preprocessing import StandardScaler

from sklearn

-decomposition import PCA

import numpy

as np

X, y = load_breast_cancer(return_X_y=True)

X_scaled = StandardScaler().fit_transform(X)

pea = PCA() . fit(X_scaled)

cumulative

=

a

)

=

np.cumsum(pca.explained_variance_rati

10

components

np.argmax(cumulative >= 0.95) + 1

11

12

print("Explained variance by component:")

13

print(np.round(pca.explained_variance_ratio

3))

14

print("

omponents needed for 95% varianc

, components)

15

print("Variance retained:", round(cumulative[components-1], 4)
