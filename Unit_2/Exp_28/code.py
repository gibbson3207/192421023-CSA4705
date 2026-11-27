IDLE Editor — Question 28

a

x

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

sklearn.datasets import make_classification

from

sklearn.model_selection import train_test_split

from

sklearn.neural_network import MLPClassifier

from

sklearn.metrics import accuracy_score

X, y = make_classification(n_samples=

00, n_features=10,

random_state

2)

X train, X_test, y train, y test = train_test_split(

X, y, test_siz

-25, random_state=42

10

11

12

for activation in

"relu",

‘tanh

logistic",

13

model = MLPClassifier(hidden_layer_sizes=(32, 16),

14

activation:

tivation, max_iter=500,

15

random_state=42)

16

model. fit(X_train, y train)

7

pred

model. predict (X_test)

18

print(activation, “accuracy:

:

19

round(accuracy_score(y test, pred), 3))
