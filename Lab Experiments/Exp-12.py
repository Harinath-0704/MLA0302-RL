import numpy as np
import random

ROWS = 4
COLS = 4

actions = ["UP", "DOWN", "LEFT", "RIGHT"]

alpha = 0.1
gamma = 0.9
epsilon = 0.1

Q = {}

for r in range(ROWS):
    for c in range(COLS):
        Q[(r, c)] = {a: 0 for a in actions}

goal = (3, 3)

def choose_action(state):
    if random.uniform(0, 1) < epsilon:
        return random.choice(actions)
    return max(Q[state], key=Q[state].get)

def next_state(state, action):
    r, c = state

    if action == "UP":
        r = max(r - 1, 0)
    elif action == "DOWN":
        r = min(r + 1, ROWS - 1)
    elif action == "LEFT":
        c = max(c - 1, 0)
    elif action == "RIGHT":
        c = min(c + 1, COLS - 1)

    return (r, c)

episodes = 500

for ep in range(episodes):

    state = (0, 0)
    action = choose_action(state)

    while state != goal:

        ns = next_state(state, action)

        reward = 10 if ns == goal else -1

        na = choose_action(ns)

        Q[state][action] += alpha * (
            reward + gamma * Q[ns][na] - Q[state][action]
        )

        state = ns
        action = na

print("SARSA Training Completed")
