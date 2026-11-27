x

IDLE Editor — Question 54

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

series = (20 + 4*np.sin(np.arange(300)*0.1)) .astype("float32")

xX y= U1,

a

for i in range(len(series)-12):

X.append(series[i:i+12])

y-append(series[i+12])

10

X, y = np.array(X)[..., None], np.array(y)

11

split = 230

12

13

for name, layer in [

14

(*RNN"

tf.keras. Layers .SimpleRNN(24)),

15

(*LSTM

, tf.keras. layers .LSTM(24))

16

]

7

model = tf.keras.Sequential ([

18

tf.keras. layers. Input(shape=(12, 1)), layer.

19

tf. keras. layers .Dense(1)

20

1)

21

model. compile(optimizer="adam", loss:

mse")

22

model.fit(X{:split], y[:split], epochs=10, verbose=0

23

pred = model.predict(X[split:], verbose

).ravel()

24

print(name, "MSE:

,» round(mean_squared_error(y[split:], pred), 4))
