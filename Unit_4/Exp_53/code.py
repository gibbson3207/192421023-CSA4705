x

IDLE Editor — Question 53

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

sentences

=

“deep learning is useful

machine learning is powerful",

“deep learning uses neural networks",

=

"neural networks learn patterns")

tokenizer

=

tf. keras. preprocessing. text. Tokenizer ()

tokenizer.

fit_on_texts(sentences)

10

sequences

tokenizer. texts_to_sequences (sentences)

11

X% y= OC,

a

12

for seq

in sequences:

13

for

i

in range(1, len(seq)):

14

x

-append(seq[:i])

15

y

-append(seq[i])

16

=

=

max(map(len, X))

max_len

7

X = tf.keras. preprocessing. sequence.pad_sequences(X, maxlen=max_len)

18

19

model = tf.keras.Sequential([

20

tf.keras. layers .Embedding(Len( tokenizer .word_index)+1, 16),

21

tf.keras. layers .SimpLeRNN (32) ,

22

tf.keras. layers .Dense(len(tokenizer.word_index)+1, activation="softmax" )

23

1)

24

model. compile(optimizer="adam",

25

los:

‘sparse_categorical_crossentropy")

26

model. fit(X, np.array(y), epochs=100, verbose=0

27

28

seed = “deep learning"

29

seq = tokenizer.texts_to_sequences([seed]) [0]

30

padded

tf .keras. preprocessing. sequence.pad_sequences([seq], maxlen=max_len

31

next_id

int(np.argmax(model.predict(padded, verbose=0) [0]))

32

print (

jlext word

tokenizer.index_word.get(next_id, "<unknown>") )
