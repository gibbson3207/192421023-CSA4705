x

IDLE Editor — Question 33

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

from sklearn.datasets import make_moons

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

X, y = make_moons(n_samples=600, nois:

2, random_state=42)

X = StandardScaler() .fit_transform(X)

X train, X_test, y train, y test = train_test_split

X, y, test_size=0.25, random_state=42

10

)

11

12

for name, optimizer in [

13

("SGD", tf.keras.optimizers.SGD(learning_rat

-01)),

14

("RMSprop", tf.keras.optimizers.RMSprop(learning_rate=0.001))

15

("Adam", tf.keras. optimizers .Adam(learning_rate=0.001)

16

7

model = tf.keras.Sequential ([

18

tf.keras. layers. Input(shape=(2,))

19

tf. keras.layers.Dense(16, activatio:

relu")

20

tf. keras.layers.Dense(1, activatior

sigmoid")

21

1)

22

model. compile( optimize

optimizer, loss="binary_crossentropy",

23

metrics:

accuracy"])

24

model.fit(X_train, y train, epochs=20, verbose=0)

25

loss, accuracy = model.evaluate(X test, y test, verbose=0

26

print(name, “Los:

+ round(loss, 4),

27

"accuracy:

, round(accuracy, 4))
