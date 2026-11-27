x

IDLE Editor — Question 17

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

from

sklearn

-neural_network import MLPClassifier

from

sklearn

-model_selection import train_test_split

from

sklearn

-datasets import make_moons

from

sklearn

-metrics import accuracy score

X, y = make_moons(n_samples=500, nois:

-25, random_state=42)

X_train, X_test, y train, y test = train_test_split(

X, y, test_size-0.3, random_state=42

)

10

11

model = MLPClassifier(hidden_layer_sizes=(100, 100),

12

max_iter=1000, random_state=42)

13

model. fit(X_train, y train)

14

=

15

train_acc

=

accuracy _score(y train, model.predict(X_train))

16

test_acc = accuracy score(y test, model.predict(X_test))

7

18

print("

raining accurac

, round(train_acc, 3))

19

print(”

esting accuracy:

» round(test_acc, 3))

20

if train_acc > test_acc + 0.10:

21

print("Possible overfitting detected")

22

else:

23

print("No major overfitting detected")
