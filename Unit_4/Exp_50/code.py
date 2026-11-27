x

IDLE Editor — Question 50

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

import numpy as np

import tensorflow as tf

text = ("deep learning models learn patterns from data

“* 30)

chars

sorted(set(text))

to_id

{c: i for i, c in enumerate(chars)}

encoded = np.array([to_id[c] for c in text])

xX y= Ul,

is

seq_len = 20

10

for i in range(len(encoded) -seq_len):

11

X.append(encoded[i:i+seq_len])

12

y-append(encoded[itseq_ten])

13

X, y = np-array(X), np.array(y)

14

15

model = tf.keras.Sequential ([

16

tf.keras.layers.Embedding(len(chars), 32),

7

tf.keras. layers .SimpLeRNN (64) ,

18

tf.keras.layers.Dense(len(chars), activatior

"softmax")

19

1)

20

model. compile(optimizer="adam",

21

loss="sparse_categorical_crossentropy")

22

model.fit(X, y, epochs=10, verbose=0

23

24

seed = "deep learning models"

25

sequence

[to_idic] for c in seed]

26

generated

seed

27

for

in range(60

28

=

=

probs

=

model . predict (np.array([sequence[-seq_len:]]), verbose=0) [0

29

next_id

=

np.random.choice(len(chars), p=probs/probs.sum()

30

generated += chars[next_id]

31

sequence. append(next_id)

32

print("Generated text:

)

33

print (generated)
