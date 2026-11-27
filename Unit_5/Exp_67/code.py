x

IDLE Editor — Question 67

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

from sklearn.datasets import load_breast_cancer

from sklearn.preprocessing import StandardScaler

from sklearn.decomposition import PCA

X, y = load_breast_cancer(return_X_y=True)

X_scaled

StandardScaler().fit_transform(X)

pca = PCA(n_components=2)

X_reduced = pca.fit_transform(X_scaled)

10

print("Original shape:

, X.shape)

11

print("

‘educed shape

X_reduced. shape)

12

print("Explained variance ratio

13

pca.explained_variance_ratio_)

14

print("Total variance retained

15

round (pca.explained_variance_ratio_.sum(), 4))
