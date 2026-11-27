x

IDLE Editor — Question 30

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

x

=

=

np-array({1.0, 0.5])

target = 1.0

W = np.array([@.2, -0.3])

b

0.1

10

lr

0.5

11

=

=

12

Zz

np.dot(x, W) + b

13

prediction

=

=

sigmoid(z)

14

error = prediction - target

15

gradient = error * prediction * (1 - prediction)

16

7

W-=

r * gradient * x

18

b -= Ur * gradient

19

20

print("Prediction before update

, round(prediction, 4))

21

print("Updated weights

np.round(W, 4))

22

print("Updated bias:

» round(b, 4))
