x

IDLE Editor — Question 26

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

datasets import load_iris

from

sklearn

model_selection import train test_split

from

sklearn

preprocessing import StandardScaler

from

sklearn

neural_network import MLPClassifier

from

sklearn

metrics import accuracy score, classification_report

X, y = load_iris(return_X_y=True)

X train, X_test, y train, y test = train_test_split(

X, y, test_size=0.2, random state=42, stratify=y

10

)

11

scaler

StandardScaler()

12

X_train

scaler. fit_transform(X_train)

13

X_test = scaler.transform(X_test)

14

15

model = MLPClassifier(hidden_layer_sizes=(16, 8),

16

max_iter=1500, random_state=42)

7

model. fit(X_train, y train)

18

pred = model.predict(X_test)

19

20

print ("Accurac

» round(accuracy _score(y test, pred), 3))

21

print(classification_report(y test, pred))
