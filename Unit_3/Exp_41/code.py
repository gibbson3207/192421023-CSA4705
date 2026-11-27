x

IDLE Editor — Question 41

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

import tensorflow as tf

# Directory structure: dataset/train/cats, dataset/train/dogs

# and dataset/test/cats, dataset/test/dogs

train = tf.keras.utils.image_dataset_from directory

.

“dataset/train", image_size=(128, 128), batch_siz

2,

label_mode="binary"

)

test = tf.keras.utils.image_dataset_from directory

10

“dataset/test

image_size=(128, 128), batch_size=32,

11

label_mode="binary"

12

)

13

14

model = tf.keras.Sequential ([

15

tf

keras.

layers

Rescaling(1./255, input_shape=(128, 128, 3)),

16

tf

keras.

layers

Conv2D(32, 3, activatio

relu"),

7

tf

keras.

layers

MaxPooling2D(),

18

tf

keras.

layers

Conv2D(64, 3, activatio

relu"),

19

tf

keras.

layers

MaxPooling2D(),

20

tf

keras.

layers

Flatten(),

21

tf

keras.

layers

Dense(64, activatioi

relu"),

22

tf

keras.

layers

Dense(1, activation="sigmoid")

23

1)

24

model. compile(optimizer="adam",

loss="binary_crossentropy",

25

metric

ccurac

"I)

26

model. fit(train, epoch:

)

27

print("Test results:

» model.evaluate(test) )
