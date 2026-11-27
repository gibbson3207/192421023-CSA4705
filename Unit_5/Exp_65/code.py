x

IDLE Editor — Question 65

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

import tensorflow as

tf

# Toy parallel data:

reverse short

integer sequences.

vocab_size = 12

X = np-array([[1,

2,

3,

ol,

[2,

3,

4,

ol,

(3,

4,

5,

ol,

[4,

5,

6,

911)

Y = np-array({[3,

2,

1,

ol,

[4,

3,

2,

ol,

(5,

4,

3,

ol,

[6,

5,

4,

911)

10

11

encoder_input = tf.keras.Input(shape=(4,))

=

=

12

enc

tf.keras.layers.Embedding(vocab_size, 16)(encoder_input)

13

_» state_h, state_c

tf.keras. Layers .LSTM(

14

rue

32, return_stati

15

(enc)

16

decoder_input = tf.keras.Input(shape=(4,))

7

dec = tf.keras.layers.Embedding(vocab_size, 16)(decoder_input)

18

dec = tf.keras.layers.LSTM(32, return_sequences=True) (

19

dec, initial_state=[state_h, state_c]

20

)

21

output = tf.keras.layers.Dense(vocab_size, activation="softmax") (dec)

22

model = tf.keras.Model( [encode

input, decoder_input], output)

23

model. compile(optimizer="adam'

24

los:

‘sparse_categorical_crossentropy")

25

model. fit([X, Y], Y[.--, None], epochs=

8, verbose=0)

26

print("

eq2Seq model trained on toy sequence pairs.")

27

print("Output shape:", model.predict({X[:

1, Y[:1]], verbose=0) . shape)
