x

IDLE Editor — Question 56

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

arange(350)

data =

np.column_stack([

25 + 5*np.sin(t*0.08),

60 + 10*np.cos(t*0.05),

1010 + 4*np.sin(t*0.03)

1) -astype("float3

")

10

11

xX y= U1,

a

12

for i in range(len(data)-12):

13

X.append(data[i:i+12])

14

y-append(data[i+12])

15

X, y = np-array(X), np.array(y)

16

7

model = tf.keras.Sequential([

18

tf.keras.layers.GRU(32, input_shape=(12, 3)),

19

tf.keras. layers .Dense(3)

20

1)

21

model. compile(optimizer="adam", loss="mse")

22

model.fit(X, y, epochs=12, verbose=0

23

print(”

redicted [temperature, humidity, pressure]:")

24

print(np.round(model.predict(X[-1:], verbose=0)[@], 2))
