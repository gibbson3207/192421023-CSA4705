x

IDLE Editor — Question 52

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

t = np.arange(400)

=

=

consumption

(50 + 10*np.sin(t*2*np.pi/24) +

3*np.sin(t*2*np.pi/7)) .astype("float32")

xX y= U1,

a

for i in range(len(consumption) -24) :

X.append(consumption[,

+24])

10

y-append(consumption[i+24])

11

X, y = np.array(X)[..., None], np.array(y)

12

13

model

tf. keras.Sequential ([

14

tf.keras.layers.SimpleRNN(32, input_shape=(24, 1)),

15

tf.keras.layers.Dense(1)

16

1)

7

model. compile(optimizer="adam", loss="mse")

18

model.fit(X, y, epochs=12, verbose=0

19

print("Forecast next deman

20

round (float (model. predict(X[-1:], verbose=0)[@][0]), 2))
