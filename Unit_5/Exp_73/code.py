x

IDLE Editor — Question 73

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

2 from sklearn.decomposition import FastICA

rng = np.random.default_rng(10)

t = np.linspace(@, 10, 1500)

voicel

np ..sin(2*np.pi*2*t)

voice2

=

np .sign(np.sin(2*np.pi*3*t))

sources

=

np.c_[voicel, voice2]

sources += 0.02*rng.normal (size=sources. shape)

10

11

mixing = np.array([[1, 0.6]

[@.4, 1.2]])

=

a

12

recordings

sources @ mixing.T

13

14

ica = FastICA(n_components=2, random_state=10,

15

max_iter=1500, whiten="unit-variance")

16

recovered = ica.fit_transform(recordings)

7

18

print("

riginal recordings shap.

, recordings. shape)

19

print("

eparated signals shape

, recovered . shape)

20

print("Correlation between recovered components:

.

21

np. round(np.corrcoef(recovered.T)[0,

1], 3))
