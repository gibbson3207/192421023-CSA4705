x

IDLE Editor — Question 55

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

from sklearn.metrics import mean_absolute_error, mean_squared_error

rng = np.random.default_rng(3)

prices

(100 + np.cumsum(rng.normal(0, 0.8, 350))).astype("float32")

xX y= U1,

a

for i in range(len(prices) -15):

X.append(prices[

i+15])

10

y-append(prices[i+15])

11

xX y

np-array(X)[..., None], np.array(y)

12

split

int (@.8*Len(X))

13

14

model = tf.keras.Sequential([

15

tf.keras.layers.LSTM(32, input_shape=(15, 1))

16

tf.keras. layers .Dense(1)

7

1)

18

model. compile(optimizer="adam", loss:

s

)

19

model. fit(X[:split], yl:

plit], epoch:

2, verbose=0)

20

pred

model.predict(X[split:], verbose=0) . ravel()

21

print ("MAI

» round(mean_absolute_error(y[split:], pred), 3))

22

print("

ISE:

round(mean_squared_error(y[split:], pred), 3))

23

print (“RMSE

round(mean_squared_error(y[split:], pred)**0.5, 3))
