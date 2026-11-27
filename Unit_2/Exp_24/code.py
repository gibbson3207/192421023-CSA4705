x

IDLE Editor — Question 24

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

from sklearn.linear_model import Perceptron

from sklearn.metrics import accuracy score

x

np.array({[2, 1],

(3, 21,

(4, 11,

(6, 5],

7, 71,

[8, 611)

y

np-array([@, 8, 8, 1, 1, 11)

model = Perceptron(max_iter=1000, eta0=0.1, random_state=42)

model.fit(X, y)

10

11

pred = model. predict (X)

12

print("

redicted classe:

, pred)

13

print("Actual classes:

vy)

14

print ("Accurac

, accuracy score(y, pred))

15

print("New applicant [5, 4]

» model.predict([[5, 4]])[0])
