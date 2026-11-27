x

IDLE Editor — Question 22

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

from

sklearn

datasets import load_breast_cancer

from

sklearn

model_selection import GridSearchCV, RandomizedSearchCV

from

sklearn

svm import SVC

from

sklearn

preprocessing import StandardScaler

from

sklearn

pipeline import Pipeline

from

scipy.stats import loguniform

=

xX y

=

load_breast

ancer(return_X_y=True)

pipe

=

=

Pipeline([

"scali

, StandardScaler()),

("sve", SVC())])

10

grid

params

{"sve_C

[8.1,

1

10],

11

“sve_kerne

[

inea|

“ rbeT}

12

grid = GridSearchCV(pipe, grid_params, cv=3)

13

grid.fit(X, y)

14

print("Grid search

, grid.best_params_, round(grid.best_score_, 3))

15

16

random = RandomizedSearchCV(

7

Pipe, {"sve_<

Loguniform(9.01

100),

18

“svc_kernel

["Linear’

.

bf" I},

19

n_iter=8, cv=3, random_state=

20

)

21

random.fit(X, y)

22

print("Random search:", random.best_params_,

23

3))

round (random.best_score

24

print("Bayesian optimization: use a Bayesian optimizer such as Optuna")

25

print("to select new trials using previous trial results

.
