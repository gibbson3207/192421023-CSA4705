x

IDLE Editor — Question 69

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

import matplotlib.pyplot as plt

from sklearn.datasets import load_iris

from sklearn.preprocessing import StandardScaler

from sklearn.decomposition import PCA

data = load_iris()

X = StandardScaler().fit_transform(data.data)

X_2d = PCA(n_components=2) . fit_transform(X)

10

for label, name in enumerate(data.target_names) :

11

plt.scatter(X_2d[data.target

label, 6],

12

X_2d[data.target

label,

1], label=name)

13

plt

xlabel ("Principal Component 1"

14

plt

ylabel("Principal Component 2")

15

plt

title("Iris Dataset - PCA")

16

plt

Legend( )

7

plt

grid(True)

18

plt

show()
