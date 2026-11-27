x

IDLE Editor — Question 36

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

import tensorflow as tf

from sklearn.datasets import make_classification

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

X, y = make_classification(n_samples=800, n_features=

2,

random_state=42)

X = StandardScaler() .fit_transform(X)

X train, X_test, y train, y test = train_test_split

10

X, y, test_size=0.25, random_state

2

11

)

12

13

model

tf. keras.Sequential ([

14

tf.keras. layers. Input(shape=(12,)),

15

tf.keras.layers.Dense(32, activation="relu",

16

kernel_regularizer=tf.keras.regularizers.12(0.01)),

7

tf.keras.layers.Dense(1, activation="sigmoid")

18

1)

19

model. compile(optimizer="adam", loss="binary_crossentropy",

20

metric

accuracy"])

21

model. fit(X_train, y train, epochs=15, verbose=0)

22

print("

est evaluation

, model.evaluate(X_test, y_test

verbose=6) )

23

print("L2 regularization penalizes large model weights

)
