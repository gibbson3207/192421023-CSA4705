x

IDLE Editor — Question 51

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

from sklearn.metrics import mean_absolute_error

=

=

prices

(100 + np.cumsum(np.random.default_rng(2).normal(®, 1, 300)))

prices

prices.astype("float32")

xX y= U1,

a

for i in range(len(prices) -10):

X.append(prices[

i+10])

10

y-append(prices[i+10])

11

xX y

np-array(X)[..., None], np-array(y)

12

split

int (@.8*Len(X))

13

14

model = tf.keras.Sequential([

15

tf.keras.layers.SimpleRNN(32, input_shape=(10, 1))

16

tf.keras.layers.Dense(1)

7

1)

18

model. compile(optimizer="adam", loss:

s

)

19

model. fit(X[:split], yl:

plit], epoch:

68, verbose=0)

20

pred

model.predict(X[split:], verbose=0) . ravel(

21

print ("MAI

» round(mean_absolute_error(y[split:], pred), 3)

22

print("Predicted stock value:", round(float(pred[-1]), 2))
