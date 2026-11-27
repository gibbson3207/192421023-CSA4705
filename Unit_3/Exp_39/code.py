x

IDLE Editor — Question 39

fa)

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

1

import numpy as np

2 from scipy.signal import

convolve2d

image

=

=

np.array({[1, 2,

1,

ol,

[6,

1,

2,

1),

[1, 6,

1,

21,

[2,

1,

6,

1))

kernel = np.array([[1, 0, -1],

[1, 6,

-1l,

10

[1, 6,

-1]))

11

=

=

12

feature_map

convolve2d(image, kernel, mode="valid")

13

print ("Input imag

)

14

print (image )

15

print("Convolution feature map:

)

16

print(feature_map)
