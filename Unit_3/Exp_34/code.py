x

IDLE Editor — Question 34

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

X_train.astype("float32") / 255.0

X_test = X_test.astype("float32") / 255.0

model = tf.keras.Sequential([

tf.keras

-layers

-Flatten(input_shape=(28, 28)),

tf.keras

-layers

-Dense(256, activatio

relu"),

10

tf.keras

-layers

-Dense(128, activatio

relu")

11

tf.keras

-layers

-Dense(10, activatior

‘softma:

12

1)

13

model. compile(optimizer="adam",

14

los:

sparse_categorical_crossentropy",

15

metrics=["accuracy"])

16

model.fit(X_train, y train, epochs=3, batch_size=128, verbose=1)

7

loss, accuracy = model.evaluate(X test, y test, verbose=0

18

print(™

est loss

round(loss, 4))

19

print("Test accuracy:

, round(accuracy, 4))
