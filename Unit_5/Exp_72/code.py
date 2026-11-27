x

IDLE Editor — Question 72

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

import matplotlib.pyplot as plt

from sklearn.decomposition import FastICA

t = np.linspace(@, 8, 1000)

sl

np.sin(2*t)

82

np.sign(np.sin(3*t))

S$ = np.c_[sl, s2]

S += 0.05*np. random.default_rng(42) .normal (size=S. shape)

10

A = np-array({[1, 1],

(0.5, 2]])

11

mixed = S$ @ A.T

12

13

ica = FastICA(n_component

, random state=42,

14

max_iter=1000, white

unit-variance")

15

separated = ica.fit_transform(mixed)

16

7

plt

figure(figsize=(9, 5))

18

plt

subplot (2, 1, 1)

19

plt

plot (mixed)

20

plt

title("Mixed signals")

21

plt

subplot (2, 1, 2)

22

plt

plot (separated)

23

plt

title("ICA separated components")

24

plt

tight_Layout()

25

plt

show()

26

print("Separated signal shap.

, separated. shape)
