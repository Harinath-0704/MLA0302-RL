"""4) A delivery drone needs to find the shortest path from a warehouse to multiple delivery
points in a city represented as a grid. Implement a policy iteration algorithm using dynamic
programming to find the optimal route policy in Python."""
import pandas as pd
import numpy as np
from google.colab import files

# -----------------------------
# Upload CSV file
# -----------------------------
print('Upload the delivery_drone_grid.csv file')
uploaded = files.upload()

file_name = list(uploaded.keys())[0]
grid = pd.read_csv(file_name, header=None).values

rows, cols = grid.shape

# Rewards
rewards = {'S': 0, 'E': -1, 'D': 5, 'G': 10, 'O': -5}

# Actions: Up, Down, Left, Right
actions = [(-1,0), (1,0), (0,-1), (0,1)]
action_names = ['U', 'D', 'L', 'R']

gamma = 0.9
theta = 0.001

# Initialize value function and random policy
V = np.zeros((rows, cols))
policy = np.zeros((rows, cols), dtype=int)

def valid(x, y):
    return 0 <= x < rows and 0 <= y < cols

# -----------------------------
# Policy Iteration
# -----------------------------
stable = False

while not stable:

    # Policy Evaluation
    while True:
        delta = 0
        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == 'G':
                    continue

                a = policy[i][j]
                dx, dy = actions[a]
                ni, nj = i + dx, j + dy

                if not valid(ni, nj):
                    ni, nj = i, j

                reward = rewards[grid[ni][nj]]
                value = reward + gamma * V[ni][nj]

                delta = max(delta, abs(value - V[i][j]))
                V[i][j] = value

        if delta < theta:
            break

    # Policy Improvement
    stable = True

    for i in range(rows):
        for j in range(cols):

            if grid[i][j] == 'G':
                continue

            old_action = policy[i][j]

            best_action = old_action
            best_value = -1e9

            for a, (dx, dy) in enumerate(actions):
                ni, nj = i + dx, j + dy

                if not valid(ni, nj):
                    ni, nj = i, j

                reward = rewards[grid[ni][nj]]
                value = reward + gamma * V[ni][nj]

                if value > best_value:
                    best_value = value
                    best_action = a

            policy[i][j] = best_action

            if best_action != old_action:
                stable = False

# -----------------------------
# Print Results
# -----------------------------
print('\\nValue Function:')
for row in V:
    print(['{:.2f}'.format(x) for x in row])

print('\\nOptimal Policy:')
for i in range(rows):
    row = []
    for j in range(cols):
        if grid[i][j] == 'G':
            row.append('G')
        elif grid[i][j] == 'O':
            row.append('X')
        else:
            row.append(action_names[policy[i][j]])
    print(row)
