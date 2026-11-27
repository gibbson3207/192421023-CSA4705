x

IDLE Editor — Question 37

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

X, y = make_classification(n_samples=700, n_features=

5,

n_informativ

, random_state=42)

X = StandardScaler().fit_transform(X)

X train, X_test, y train, y test = train_test_split

10

X, y, test_size=0.25, random_state

2

11

)

12

13

for label,

regularizer in [

14

("Without regularization

None),

15

("With L2 regularization", tf.keras.regularizers.12(0.01))

16

]

7

model = tf.keras.Sequential ([

18

tf.keras. layers. Input(shape=(15,))

19

tf. keras.layers.Dense(64, activation:

relu",

20

kernel_regularizer=regularizer) ,

21

tf. keras.layers.Dense(1, activatior

sigmoid")

22

1)

23

model. compile(optimizer="adam", Los

binary_crossentropy",

24

metrics=["accuracy"])

25

model.fit(X_train, y train, epochs=15, verbose=0)

26

print(Label)

27

print("Train:", model.evaluate(X_train, y train, verbos.

‘0))

28

print("Tes

, model.evaluate(X_test, y_test, verbose=0))
