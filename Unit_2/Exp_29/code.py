x

IDLE Editor — Question 29

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

def sigmoid(x):

return 1 / (1 + np.exp(-x))

inputs

np.array([[6.5, 9.8]])

W1 = np.array([[0.2, 0.4]

[@.3, @.1]])

bl = np.array([9-1, 9.2])

w2

np.array([[9.5],

[6.6]])

10

b2

np.array([0.1])

11

12

hidden = sigmoid(inputs @ W1 + b1)

13

output = sigmoid(hidden @ W2 + b2)

14

15

print(”

idden layer output

, np.round(hidden, 4))

16

print("Output layer resul

, np.round(output, 4))
