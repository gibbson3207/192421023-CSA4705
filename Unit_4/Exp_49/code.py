x

IDLE Editor — Question 49

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

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.imdb.load_data(

num_words=10000

)

X_train

tf.keras. preprocessing. sequence.pad_sequences(X_train, maxler

50)

X_test = tf.keras. preprocessing. sequence.pad_sequences(X_test, maxlen=

58)

model = tf.keras.Sequential([

10

tf.keras.layers.Embedding(10000, 32),

11

tf.keras. layers. SimpleRNN (32) ,

12

tf.keras.layers.Dense(1, activation="sigmoid")

13

1)

14

model. compile(optimizer="adam", loss="binary_crossentropy",

15

metrics=["accuracy"])

16

8000], y train[:8000], epochs=2,

model. fit(X_train

7

validation_spli

.2, verbose=1)

18

print("Test accuracy

19

model .evaluate(X_test[:3000], y_test[:3000], verbose=0)[1])
