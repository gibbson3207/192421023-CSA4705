x

IDLE Editor — Question 48

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

import tensorflow as tf

temperature = (25 + 5*np.sin(np.arange(250) *0.08)) .astype("float32")

xX y= U1,

a

for i in range(len(temperature) -12):

X.append(temperaturel.

+12])

y-append(temperature[i+12])

np-array(X)[..., None]

=

10

np.array(y)

11

12

model = tf.keras.Sequential([

13

tf.keras.layers.SimpleRNN(32, input_shape=(12, 1))

14

tf.keras.layers.Dense(1)

15

1)

16

model. compile(optimizer="adam", Loss:

se")

.

7

model.fit(X, y, epochs=15, verbose:

)

18

prediction

=

2

model.predict(X[-1:], verbose=0) [0] [0]

19

print("Predicted next temperature

» round(float(prediction), 2))

20

print("Actual next temperature:

» round(float(y[-1]), 2))
