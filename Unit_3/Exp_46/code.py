x

IDLE Editor — Question 46

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

# Place labelled plant images in dataset/train and dataset/test folders

train = tf.keras.utils.image_dataset_from directory

.

“dataset/trai

» image_size=(224, 224), batch_size=16

)

test = tf.keras.utils.image_dataset_from_directory

“dataset/test", image_size=(224, 224), batch_size=16

)

10

11

base = tf.keras. applications .ResNet50(

12

include_to

alse, weights="imagenet",

13

input_shape=(224, 224, 3), poolin

avg"

14

)

15

base.trainable = False

16

=

=

7

inputs

tf.keras.Input(shape=(224, 224, 3))

18

x

=

=

tf.keras. applications. resnet50.preprocess_input(inputs)

=

=

19

x

base(x, training=False)

20

x = tf.keras.layers.Dense(128, activation:

relu") (x)

21

outputs = tf.keras.layers.Dense(train.class_names._len_()

22

activation="softmax") (x)

23

model = tf.keras.Model (inputs, outputs

24

model. compile(optimizer="adam",

25

los:

sparse_categorical_crossentropy",

26

metric

ccuracy"])

27

model. fit(train, epochs=3)

28

print("Test results

model.evaluate(test) )
