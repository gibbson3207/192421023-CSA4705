x

IDLE Editor — Question 25

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

1

import numpy as np

from sklearn.neural_network import MLPClassifier

x

np.array({[6, 6],

[6,

1),

[1, 61,

[1,

111)

y

np.array([8,

1, 01)

model = MLPClassifier(hidden_layer_sizes=(4,),

activation="tanh", solver="Lbfgs",

max_iter=3000, random_state=1

10

model.fit(X, y)

11

12

print("XOR inputs:

13

print (X)

14

print( "Prediction:

» model.predict(X))

15

print ("Expected:

vy)
