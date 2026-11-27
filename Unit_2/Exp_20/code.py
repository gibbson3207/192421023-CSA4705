x

IDLE Editor — Question 20

fa)

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

x

np.array([1., 2., 3., 4.1)

y

2*X

for Ur in [0.001, 0.01, 0.1]:

w= 0.0

losses = []

for epoch in range(100) :

10

error =w*X-y

11

loss =

p.mean(error ** 2)

12

gradient = 2 * np.mean(error * X)

13

w -= Ur * gradient

14

Losses. append(1oss)

15

print("Learning rate:

»w)

16

print("Final weight

» round(w, 4))

7

print("Final loss:

» round(losses[-1],

6))
