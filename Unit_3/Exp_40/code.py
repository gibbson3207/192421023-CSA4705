x

IDLE Editor — Question 40

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

import numpy as np

=

=

feature_map

np-array([[1,

3,

2, 41,

(5,

6,

1, 21,

(7,

2,

8, 31,

[1,

4

5, 9]])

def pooling(data, mode)

result = []

10

for i in range(@, data.shape[0], 2)

11

row

=

=

is)

12

for j in range(@, data.shape[1], 2

13

block

dataL

42, 52542]

14

row.append(block.max() if mode

"max" else block.mean())

15

result. append (row)

16

return np.array(result)

7

18

print ("Max poolini

)

19

print(pooling(feature map, “max")

20

print("Average pooling

)

21

print(pooling(feature map, “average")
