x

IDLE Editor — Question 78

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

1

import numpy as np

=

=

mean

np-array([25, 60, 1010]

covariance = np.array([[4, 1, 0],

(1, 9, 0.5],

[8, 0.5,

1611)

=

samples

=

np. random.default_rng(42) .multivariate_normal(

mean, covariance, size=1000

10

)

11

12

print("Generated data shape

, samples. shape)

13

print("Estimated mean:")

14

print (np.round(samples.mean(axis=0), 2))

15

print("Estimated covariance:")

16

print(np.round(np.cov(samples, rowvar=False), 2))
