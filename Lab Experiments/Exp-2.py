"""2) A robot navigates a warehouse to pick and place items. Define states (locations in the
warehouse), actions (move in four directions), and rewards (picking an item: +2, reaching
the goal: +5, hitting an obstacle: -2). Implement a policy evaluation algorithm to determine
the value function for a given policy in Python."""
import pandas as pd
from google.colab import files
print('Upload the warehouse CSV file')
uploaded = files.upload()

file_path = list(uploaded.keys())[0]
grid = pd.read_csv(file_path, header=None).values.tolist()

ROWS = len(grid)
COLS = len(grid[0])

# Rewards
REWARDS = {
    'S': 0,
    'E': 0,
    'I': 2,   # Picking an item
    'G': 5,   # Goal
    'O': -2   # Obstacle
}

# -----------------------------
# Display warehouse
# -----------------------------
print('\\nWarehouse Grid')
for row in grid:
    print(' '.join(row))

# -----------------------------
# Fixed Policy
# Right -> Down -> Left -> Up
# -----------------------------
policy_order = [(0,1), (1,0), (0,-1), (-1,0)]

def valid(x, y):
    return 0 <= x < ROWS and 0 <= y < COLS

# -----------------------------
# Policy Evaluation
# -----------------------------
gamma = 0.9
theta = 0.001

V = [[0.0 for _ in range(COLS)] for _ in range(ROWS)]

while True:
    delta = 0

    for i in range(ROWS):
        for j in range(COLS):

            if grid[i][j] == 'G':
                continue

            old_value = V[i][j]
            new_value = old_value

            # Choose first valid action from the policy
            for dx, dy in policy_order:
                ni, nj = i + dx, j + dy
                if valid(ni, nj):
                    reward = REWARDS[grid[ni][nj]]
                    new_value = reward + gamma * V[ni][nj]
                    break

            V[i][j] = new_value
            delta = max(delta, abs(old_value - new_value))

    if delta < theta:
        break

# -----------------------------
# Print Value Function
# -----------------------------
print('\\nValue Function V(s)')
for row in V:
    print(['{:.2f}'.format(x) for x in row])
