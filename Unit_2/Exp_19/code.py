x

IDLE Editor — Question 19

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

import numpy

as np

from sklearn.

linear_model import Lasso, Ridge

from sklearn.

model_selection import train _test_split

from sklearn.

metrics import mean_squared_error

rng

np.random.default_rng(1)

X = rng.normal(size=(150, 5))

y = 4*X[:, 0] - 2*X[:, 1] + 0.5*X[:, 2] + rng.normal(0, 6.5, 150)

X train, X_test, y train, y test = train_test_split

10

X, y, test_size=0.25, random_state

2

11

)

12

13

for name, model in [("L1 (Lasso)", Lasso(alphi

-1)),

14

("L2 (Ridge)", Ridge(alph:

-1))1:

15

model. fit(X_train, y train)

16

pred = model.predict(X_test

7

print(name)

18

print ("Coefficients

, np.round(model.coef_, 3))

19

print("Test MSE

, round(mean_squared_error(y test, pred), 3)
