x

IDLE Editor — Question 75

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

from sklearn.preprocessing import StandardScaler

from sklearn.decomposition import FactorAnalysis

data = np.array([

[80,

85,

78, 90,

88],

[7e,

5,

72,

80,

781,

[90,

92,

88,

95,

931,

[60,

65,

62,

78,

68],

10

[85,

88,

84,

91,

901,

11

(75,

78,

74,

82,

80]

12

1, dtype=float)

13

14

X = StandardScaler().fit_transform(data)

15

‘a = FactorAnalysis(n_components=2, random_state=42

16

scores = fa.fit_transform(X)

7

18

print("

‘actor loadings

19

print(np.round( fa. components

3))

20

print("Student factor scores

21

print(np.round(scores, 3))
