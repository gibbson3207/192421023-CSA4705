x

IDLE Editor - Question 38

a

File

Edit

Format

Run

Options

Window

Help

Python 3

I

IDLE Editor

1

import tensorflow as tf

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

X_train

X_train[.

None] .astype("float32") / 255.0

X_test = X_test[.

None] .astype("float32") / 255.0

model = tf.keras.Sequential ([

tf

keras.

layers

Input(shape=(28, 28, 1)),

tf

keras.

layers

Conv2D(32, 3, activatio

relu"),

10

tf

keras.

layers

MaxPooling2D(),

11

tf

keras.

layers

Conv2D(64, 3, activatio

relu"),

12

tf

keras.

layers

MaxPooling2D(),

13

tf

keras.

layers

Flatten(),

14

tf

keras.

layers

Dense(64, activatioi

relu"),

15

tf

keras.

layers

Dense(10, activation="softmax")

16

1)

7

model. compile(optimizer="adam",

18

los:

sparse_categorical_crossentropy",

19

metric

ccuracy"])

20

model. fit(X_train, y train, epochs:

, batch_size=128, verbose=1

21

print("Test accuracy

22

model .evaluate(X_test, y test, verbose=0)[1])
