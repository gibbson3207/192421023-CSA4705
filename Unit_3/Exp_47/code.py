x

IDLE Editor — Question 47

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

# Synthetic sensor readings

series = np.sin(np.arange(300) * 0.1).astype("float32")

xX y= U1,

a

for i in range(len(series) - 10):

X.append(series[i:i+10])

y-append(series[i+10])

10

x

np-array(X)[..., None]

11

y

np.array(y)

12

13

model

tf. keras.Sequential ([

14

tf.keras.layers.SimpleRNN(16, input_shape=(10, 1))

15

tf.keras.layers.Dense(1)

16

1)

7

model. compile(optimizer="adam", loss="mse")

18

model.fit(X, y, epochs=10, verbos.

)

19

print("Predicted next sensor value

20

model .predict(X[-1:], verbos:

)(01[01)

21

print("Actual next sensor value

y[-1])
