import numpy as np
import random

ROWS = 5
COLS = 5

actions = ["UP", "DOWN", "LEFT", "RIGHT"]

Q = {}

alpha = 0.1
gamma = 0.9
epsilon = 0.1

goal = (4, 4)

for r in range(ROWS):
    for c in range(COLS):
        Q[(r, c)] = {a: 0 for a in actions}

def choose_action(state):
    if random.random() < epsilon:
        return random.choice(actions)
    return max(Q[state], key=Q[state].get)

def move(state, action):

    r, c = state

    if action == "UP":
        r = max(0, r - 1)
    elif action == "DOWN":
        r = min(ROWS - 1, r + 1)
    elif action == "LEFT":
        c = max(0, c - 1)
    elif action == "RIGHT":
        c = min(COLS - 1, c + 1)

    return (r, c)

for episode in range(1000):

    state = (0, 0)

    while state != goal:

        action = choose_action(state)

        ns = move(state, action)

        reward = 100 if ns == goal else -1

        best = max(Q[ns].values())

        Q[state][action] += alpha * (
            reward + gamma * best - Q[state][action]
        )

        state = ns

print("Q Learning Completed")
