x

IDLE Editor — Question 31

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

from sklearn.neural_network import MLPRegressor

from sklearn.metrics import mean_squared_error

x

np.array([[500],

[800],

[1600],

[1200],

[1500],

[1806]])

y

np.array([{20, 30, 38, 45, 55, 65])

model = MLPRegressor(hidden_layer_sizes=(10,), max_iter=5000,

nit=0.001)

random_state=42, learning_rate_-

10

model.fit(X, y)

11

pred = model. predict (X)

12

13

print("Actual prices

vy)

14

print("Predicted prices

, np.round(pred, 2))

15

print("Mean Squared Error

, round(mean_squared_error(y, pred), 3)
