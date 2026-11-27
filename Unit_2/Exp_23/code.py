x

IDLE Editor — Question 23

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

# States:

= low traffic,

1

high traffic

# Actions:

= keep current signal, 1

=

=

switch signal

=

=

Q

np.zeros((2, 2))

rewards = np.array([[2, 1],

[-2, 51])

=

a

alpha, gamma, epsilon

0.1, 0.9, 0.1

rng = np.random.default_rng(42)

10

for episode in range(500)

11

state = rng.integers(0, 2)

12

action = (rng.integers(®, 2) if rng.random() < epsilon

13

else np.argmax(Q[state]))

14

next_state = rng.integers(@, 2)

15

reward = rewards[state, action]

16

Q[state, action] += alpha * (

7

reward + gamma * np.max(Q[next_state]) - Q[state, action

18

)

19

20

print("Learned Q-table

)

21

print(np.round(Q, 2))

22

print("

est action for low traffic:

np.argmax(Q{0]))

23

print("Best action for high traffii

» np.argmax(Q{1]))
