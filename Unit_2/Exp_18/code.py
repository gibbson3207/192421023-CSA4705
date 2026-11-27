x

IDLE Editor - Question 18

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

from sklearn

preprocessing import PolynomialFeatures

from sklearn

linear_model import LinearRegression

from sklearn

pipeline import make pipeline

from sklearn

model_selection import train test_split

from sklearn

metrics import mean_squared_error

=

rng

=

np.random.default_rng(42)

X = np.linspace(0, 6, 120).reshape(-1, 1

=

=

10

np.sin(X).ravel() + rng.normal(@, 0.15,

120)

11

X train, X_test, y train, y test = train_test_split

12

X, y, test_size=0.25, random_state=42

13

)

14

15

for degree in [1, 3, 10]:

16

model = make_pipeline(PolynomialFeatures (degree) ,

7

LinearRegression())

18

model. fit(X_train, y train)

19

train_error = mean_squared_error(y train, model.predict(X_train))

20

test_error = mean_squared error(y test, model.predict(X_test))

21

print ("Degree

degree,

22

"Train MSE

, round(train_error, 4),

23

"Test MSE

round(test_error, 4))
