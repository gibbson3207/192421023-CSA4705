a

x

#. exp 1\py - C/Users/prith/Downloads/dlary-app/exp 1ipy (3.14.2)

edit

File

Format Run Options

Window Help

orl numpy as np

np-array (11,

2, 3, 4, Si)

np-array([2, 4y 6, 8, 10])

Jearning_rate

0.01

100

epochs

a

a

a

0

for i

Sn range (epochs) =

gradient

np.mean(2 * x *

Ww x= 1)

w

=

=

w+ learning rate * gradient

Jprint ("Batch GD Weight:

ow)

be

E

a

°

for i in range(epochs) :

For J in range (len(X))

gradient

2° xtjl*

(w * XU ~ YC)

w

=

=

w= learning rate * gradient

print ("Stochastic GD Weight:", w)

be

°

batch_size - 2

for i

Sn range (epochs) t

for j in range(0, len(x), batch_size):

XL

+patch size]

yb =

YL

+ batch_size]

gradient,

=

-

np.mean(2 # xb *

(w * xb - yb))

”

w > learning cate * gradient

print. (™Mini-Ratch GD Weigh

”

)

In? Coko!
