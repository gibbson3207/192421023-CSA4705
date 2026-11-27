x

IDLE Editor — Question 45

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

=

=

augmentation

tf.keras Sequential ([

tf.keras.layers.RandomRotation(0.08) ,

tf.keras.layers.RandomZoom(0.1),

10

tf.keras. layers .RandomFlip("horizontal")

11

1)

12

13

model

tf. keras.Sequential ([

14

tf.keras. layers. Input(shape=(28, 28, 1)),

15

augmentation,

16

tf.keras. layers

-Conv2D(32, 3, activatio

relu"),

7

tf.keras. layers

-MaxPooling2D(),

18

tf.keras. layers

-Flatten(),

19

tf.keras. layers

-Dense(10, activation="softmax")

20

1)

21

model. compile(optimizer="adam",

22

loss="spa

e_categorical_crossentropy",

23

metric

ccurac

"1)

24

model.fit(X_train, y train, epochs=3, verbose=1)

25

print(

est accuracy

26

model .evaluate(X_test, y test, verbose=0)[1])
