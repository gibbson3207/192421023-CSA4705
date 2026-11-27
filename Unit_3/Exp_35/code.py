x

IDLE Editor — Question 35

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

X_train.astype("float32") / 255.0

X_test = X_test.astype("float32") / 255.0

def build_model(use_dropout) :

=

layers

=

[tf.keras.layers.Flatten(input_shape=(28, 28)

.

tf.keras.layers.Dense(256, activatiot

relu"

]

10

if use_dropout:

11

layers .append(tf.keras. layers .Dropout(@.5))

12

layers += [tf.keras.layers.Dense(10, activatio

softmax")]

13

model

tf.keras. Sequential (layers)

14

model. compile(optimizer="adam",

15

loss:

sparse_categorical_crossentropy",

16

metrics=["accuracy"])

7

return model

18

19

for

label, dropout in [("Without dropout",

False),

20

("With dropout", True)]:

21

model = build_model(dropout)

22

model.fit(X_train, y train, epochs=3, batch_size=128, verbose=@)

23

train_loss, train_ace

model.evaluate(X_train, y train, verbose=0

24

test_loss, test_acc

model.evaluate(X_test, y test, verbose=0

25

print(label, “train accurac’

, round(train_acc, 4),

26

“test accuracy

» round(test_acc, 4))
