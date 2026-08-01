import pandas as pd
import numpy as np
from google.colab import files

# -----------------------------
# Upload CSV file
# -----------------------------
print('Upload the taxi_dispatch_grid.csv file')
uploaded = files.upload()

file_name = list(uploaded.keys())[0]
grid = pd.read_csv(file_name, header=None).values

rows, cols = grid.shape

# Rewards
rewards = {
    'S': 0,
    'E': -1,
    'P': 5,
    'G': 10,
    'O': -5
}

# Actions: Up, Down, Left, Right
actions = [(-1,0), (1,0), (0,-1), (0,1)]
action_names = ['U', 'D', 'L', 'R']

gamma = 0.9
theta = 0.001

V = np.zeros((rows, cols))

def valid(x, y):
    return 0 <= x < rows and 0 <= y < cols

# -----------------------------
# Value Iteration
# -----------------------------
while True:
    delta = 0
    new_V = V.copy()

    for i in range(rows):
        for j in range(cols):

            if grid[i][j] == 'G':
                continue

            best_value = -1e9

            for dx, dy in actions:
                ni, nj = i + dx, j + dy

                if not valid(ni, nj):
                    ni, nj = i, j

                reward = rewards[grid[ni][nj]]
                value = reward + gamma * V[ni][nj]

                if value > best_value:
                    best_value = value

            new_V[i][j] = best_value
            delta = max(delta, abs(new_V[i][j] - V[i][j]))

    V = new_V

    if delta < theta:
        break

# -----------------------------
# Extract Optimal Policy
# -----------------------------
policy = np.empty((rows, cols), dtype=object)

for i in range(rows):
    for j in range(cols):

        if grid[i][j] == 'G':
            policy[i][j] = 'G'
            continue

        if grid[i][j] == 'O':
            policy[i][j] = 'X'
            continue

        best_action = 0
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

        policy[i][j] = action_names[best_action]

# -----------------------------
# Print Results
# -----------------------------
print('\\nValue Function:')
for row in V:
    print(['{:.2f}'.format(x) for x in row])

print('\\nOptimal Dispatch Policy:')
for row in policy:
    print(list(row))
