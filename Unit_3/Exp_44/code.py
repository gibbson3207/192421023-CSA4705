x

IDLE Editor — Question 44

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

for label, use_bn in [(

Jithout batch normalization",

False),

("With batch normalization", True)]:

layers = [tf.keras.layers.Input(shape=(28, 28, 1)),

10

tf.keras. layers .Conv2D(32, 3, activation=None) ]

11

if use_bn:

12

layers .append(tf.keras. layers. BatchNormalization())

13

layers += [tf.keras. layers

-Activation("relu"),

14

tf.keras. layers

-MaxPooling2D (),

15

tf.keras. layers

-Flatten(),

16

tf.keras. layers

-Dense(10, activation

softmax")]

7

model = tf.keras. Sequential (layers)

18

model. compile(optimizer="adam",

19

loss="

parse_categorical_crossentropy",

20

metrics=["accuracy"])

21

model.fit(X_train, y train, epochs=:

» verbose=0)

22

print(label, “test accuracy:",

23

model.evaluate(X_test, y test, verbose=0)[1])
