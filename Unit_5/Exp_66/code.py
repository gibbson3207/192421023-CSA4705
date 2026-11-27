x

IDLE Editor — Question 66

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

series = np.sin(np.arange(490)*0.04) .astype("float32")

seq_len = 40

xX y= U1,

a

for i in range(len(series)-seq_len):

X.append(series[

itseq_len])

10

y-append(series[itseq_len])

11

xX y

np-array(X)[..., None], np.array(y)

12

split

280

13

14

for name, layer in [

15

(CORN

tf.keras. Layers .SimpleRNN(32)),

16

(*LSTM", tf.keras.layers.LSTM(32)

7

18

model = tf.keras.Sequential ([

19

tf.keras. layers. Input(shape=(seq_len, 1)), layer

20

tf. keras. layers .Dense(1)

21

1)

22

model. compile(optimizer="adam", loss="mse")

23

model.fit(X{:split], y[:split], epochs=10, verbose=0

24

pred

model.predict(X[split:]

verbose

).ravel()

25

print(name, “Llong-sequence MSE

26

round(mean_squared_error(y[split:], pred), 5)
