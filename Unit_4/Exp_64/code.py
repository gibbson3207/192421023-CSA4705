IDLE Editor — Question 64

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

import numpy as np

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.tree import DecisionTreeClassifier

from sklearn.pipeline import make_pipeline

# A tree-based classifier uses word features as a simple baseline.

# A true recursive neural network requires parsed sentence trees

texts

"this movie is good

"this film is excellent

"this movie is bad

this film is terribl

10

"the story is good

the story is boring"]

=

11

labels

=

(1,

1, 6, 0,

6]

12

13

model = make_pipeline(CountVectorizer(),

14

DecisionTreeClassifier(random_state=42) )

15

model. fit(texts, labels)

16

tests

"the movie is excellen’

"the film is boring"]

7

print("Predictions (

ositive, O=negative) :

, model.predict(tests))

18

print("Note: this is a tree-based baseline, not a full recursive neural network.
