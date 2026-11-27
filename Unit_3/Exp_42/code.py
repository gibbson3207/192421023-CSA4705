x

IDLE Editor — Question 42

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

import tensorflow as tf

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

X_train

X_train[.

None] .astype("float32") / 255.0

X_test = X_test[.

None] .astype("float32") / 255.0

for filters,

kernel in [(16, 3),

(32, 3),

(32, 5)]:

model = tf.keras.Sequential ([

tf

keras

-layers

-Input (shape=(28, 28, 1))

10

tf

keras

-layers

-Conv2D (filters,

kernel, activation="relu"),

11

tf

keras

-layers

-MaxPooling2D(),

12

tf

keras

-layers

-Flatten(),

13

tf

keras

-layers

-Dense(10, activation:

oftmax")

14

1)

15

model. compile(optimizer="adam",

16

loss:

parse_categorical_crossentropy",

7

metrics=["accuracy"])

18

model.fit(X_train, y train, epochs=:

» verbose=0)

=

=

19

loss, acc

.

model.evaluate(X test, y test, verbose=0

20

print("Filter:

, filters,

"Kerne

.

kernel,

21

“Accuracy

round(acc, 4))
