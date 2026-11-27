x

IDLE Editor — Question 80

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

import numpy as np

import tensorflow as tf

from sklearn.datasets import load_breast_cancer

from

sklearn.model_selection import train_test_split

from

sklearn.preprocessing import StandardScaler

from

sklearn.metrics import classification_report

=

data

=

load_breast_cancer()

xX y

=

=

data.data, data.target

10

X train, X_test, y train, y test = train_test_split

11

X, y, test_size=0.2, random state=42, stratify=y

12

)

13

scaler

StandardScaler()

14

X_train

scaler. fit_transform(X_train)

15

X_test = scaler.transform(X_test)

16

7

model = tf.keras.Sequential([

18

tf

-keras. layers

-Input (shape=(X_train.shape[1],)),

19

tf

-keras. layers

-Dense(32, activatior

relu"),

20

tf

-keras. layers

-Dropout (0.2),

21

tf

-keras. layers

-Dense(16, activatior

relu"),

22

tf

-keras. layers

-Dense(1, activation="sigmoid")

23

1)

24

model. compile(optimizer="adam",

loss="binary_crossentropy",

25

metric

ccurac

"1)

26

model. fit(X_train, y train, epoch

=15, batch _size=16, verbose=0)

27

28

=

=

probabilities

=

model.predict(X_test, verbose=0) .ravel()

29

predictions

=

(probabilities >= 0.5).astype(int)

30

print("Test evaluation

model.evaluate(X_test, y test, verbose=0))

31

print(classification_report(y test, predictions

32

target_names=data.target_names) )

33

print("Example predicted class

, data.target_names[predictions[0]])
