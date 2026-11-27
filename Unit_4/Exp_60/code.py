x

IDLE Editor — Question 60

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

series = (20 + 3*np.sin(np.arange(280)*0.1)).astype("float32")

for seq_len in [5, 10, 20

xy

ul,

a

for i in range(len(series) -seq_len)

X.append(series[i:i+seq_len])

10

y-append(series[itseq_len])

11

xX y

np-array(X)[..., None], np.array(y)

12

split

int(0.8*1en(X))

13

model

tf.keras Sequential ([

14

tf.keras.layers.SimpleRNN(16, input_shape=(seq_len, 1))

15

tf. keras. layers .Dense(1)

16

1)

7

model. compile(optimizer="adam", loss="mse")

18

model. fit(X[:split], y[:split], epochs=8, verbose-0

19

pred

model. predict (X[spli

» verbos

).ravel()

20

print("Sequence lengt!

» seq_ten,

21

"MSE:", round(mean_squared_error(y[split:], pred), 4)
