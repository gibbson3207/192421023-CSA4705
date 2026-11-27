x

IDLE Editor — Question 70

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

datasets import load_breast_cancer

from

sklearn

model_selection import cross_val_score

from

sklearn

preprocessing import StandardScaler

from

sklearn

decomposition import PCA

from

sklearn

pipeline import make pipeline

from

sklearn

linear_model import LogisticRegression

X, y = load_breast_cancer(return_X_y=True)

original = make_pipeline(StandardScaler(),

10

LogisticRegression(max_iter=2000) )

11

reduced = make_pipeline(StandardScaler(), PCA(n_components=5) ,

12

LogisticRegression(max_iter=2000) )

13

14

scorel = cross_val_score(original, X, y, cv=5).mean(

15

score2 = cross_val_score(reduced, X, y, cv=5).mean(

16

print("

ccuracy before PC)

» round(scorel,

4))

7

print("Accuracy after PCA

» round(score2, 4))
