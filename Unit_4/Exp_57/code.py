x

IDLE Editor — Question 57

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

import tensorflow as tf

from sklearn.metrics import mean_squared_error

series = np.sin(np.arange(300)*9.1) .astype("float32")

xX y= U1,

a

for i in range(len(series)-10):

X.append(series[i:i+10])

y-append(series[i+10])

10

X, y = np.array(X)[..., None], np.array(y)

11

split = 230

12

13

layers

=

=

[("RNN", tf.keras. layers .SimpleRNN(26)),

14

("LSTM", tf.keras.layers.LSTM(20) ),

15

("GRU", tf.keras.layers.GRU(20))]

16

for name, layer in layers

7

model = tf.keras.Sequential ([

18

tf.keras.layers.Input(shape=(10, 1)), layer.

19

tf. keras. layers .Dense(1)

20

1)

21

model. compile(optimizer="adam", loss:

mse")

22

model. fit(X[:split], y[:split], epochs=8, verbose-0

23

pred = model.predict(X[split:], verbose

).ravel()

24

print(name, "MSE:

,» round(mean_squared_error(y[split:], pred), 5))
