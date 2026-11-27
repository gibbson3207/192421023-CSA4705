x

IDLE Editor — Question 58

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

import

numpy as np

import

tensorflow as tf

t = np

arange(400)

data =

np.column_stack([

30 + np.sin(t*.1),

5 + np.cos(t*®.07),

2 + 0.5*np. sit

t*0.2)

1) -astype("float32")

10

xX y= U1,

a

11

for i in range(len(data)-15):

12

X.append(data[i:i+15])

13

y-append(data[i+15])

14

X, y = np-array(X), np.array(y)

15

16

model = tf.keras.Sequential([

7

tf.keras.layers.SimpLeRNN(32, return_sequences=True

18

input_shape=(15, 3)),

19

tf.keras.layers.SimpleRNN(16) ,

20

tf.keras. layers .Dense(3)

21

1)

22

model. compile(optimizer="adam", loss="mse")

23

model.fit(X, y, epochs=10, verbose=0

24

print("Predicted next machine readings:")

25

print(np.round(model.predict(X[-1:], verbose=0)[@], 3))
