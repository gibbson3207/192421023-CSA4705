x

IDLE Editor — Question 27

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

import matplotlib.pyplot as plt

x

=

=

np.linspace(-6, 6, 200)

sigmoid = 1 / (1 + np.exp(-x)

tanh = np.tanh(x)

relu = np.maximum(@, x)

plt

plot(x, sigmoid, labe

Sigmoi

10

plt

plot(x, tanh, lLabe

Tanh")

11

plt

plot (x,

relu, labe

ReLU")

12

plt

xlabel ("Input")

13

plt

ylabel ("Output")

14

plt

title("Activation Functions")

15

plt

Legend( )

16

plt

grid(True)

7

plt

show()

18

19

print(”

igmoid range: @ to 1"

20

print("Tanh range: -1 to 1"

21

print("ReLU range: @ to infinity")
