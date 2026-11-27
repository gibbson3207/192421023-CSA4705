x

IDLE Editor — Question 61

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

series

np .sin(np.arange(250)*0.1) .astype( "float32")

xX y= U1,

a

for i in range(len(series)-10):

X.append(series[i:i+10])

y-append(series[i+10])

X, y = np.array(X)[..., None], np.array(y)

10

11

for Lr, units, batch in [(@.001,

16,

16),

(0.01, 32, 32)]:

12

model = tf.keras.Sequential([

13

tf.keras.layers.LSTM(units, input_shape=(10, 1))

14

tf. keras. layers .Dense(1)

15

1)

16

model. compile(optimizer=tf.keras.optimizers.Adam(1r), Los

"mse")

=

=

7

history

model.fit(X, y, epochs=8, batch_size=batch, verbos

)

18

print("Learning rat

our,

"Hidden units

i.

units,

19

"Batch siz

, batch,

20

"Final loss

» round(history-history["loss"][-1], 5))
