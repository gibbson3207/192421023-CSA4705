x

IDLE Editor — Question 68

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

from

sklearn

-datasets import load_iris

from

sklearn

-preprocessing import StandardScaler

from

sklearn

-decomposition import PCA

from

sklearn

-linear_model import LogisticRegression

from

sklearn

-model_selection import cross_val_score

X, y = load_iris(return_X_y=True)

X_scaled = StandardScaler().fit_transform(X)

X_pca = PCA(n_components=2) . fi

_transform(X_scated)

10

11

scores

=

=

cross_val_score(LogisticRegression (max_iter=1000),

12

X_pea, y, cv=5)

13

print("Original feature:

, X.shape[1])

14

print("PCA features

X_pca.shape[1])

15

print("Mean classification accuracy:", round(scores.mean(), 3)
