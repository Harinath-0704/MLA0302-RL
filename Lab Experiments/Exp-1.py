"""1) An autonomous cleaning robot navigates a 5x5 grid where certain cells contain dirt (reward:
+1) and obstacles (penalty: -1). The robot starts at the top-left corner and must find an
optimal policy to clean the entire grid efficiently. Implement the grid environment as an
MDP and write a Python program to simulate the robot’s navigation using different policies."""
import pandas as pd
import random
from collections import deque
from google.colab import files
print('Upload the 5x5 grid CSV file')
uploaded = files.upload()

file_path = list(uploaded.keys())[0]

grid = pd.read_csv(file_path, header=None).values.tolist()

ROWS = len(grid)
COLS = len(grid[0])

REWARDS = {
    'D': 1,   # Dirt
    'O': -1,  # Obstacle
    'E': 0,   # Empty
    'S': 0    # Start
}

# Find start position
start = (0, 0)
for i in range(ROWS):
    for j in range(COLS):
        if grid[i][j] == 'S':
            start = (i, j)


moves = [(-1,0), (1,0), (0,-1), (0,1)]

def valid(x, y):
    return 0 <= x < ROWS and 0 <= y < COLS

def print_grid():
    print('\\nGrid Environment')
    for row in grid:
        print(' '.join(row))
    print()

print_grid()

# -----------------------------
# Random Policy
# -----------------------------
def random_policy(max_steps=50):
    pos = start
    score = 0
    cleaned = set()

    print('--- Random Policy ---')
    print('Start:', pos)

    for step in range(max_steps):
        dx, dy = random.choice(moves)
        nx, ny = pos[0] + dx, pos[1] + dy

        if not valid(nx, ny):
            continue

        pos = (nx, ny)
        cell = grid[nx][ny]

        if cell == 'D' and pos not in cleaned:
            score += 1
            cleaned.add(pos)
        elif cell == 'O':
            score -= 1

        print(f'Step {step+1}: {pos} -> {cell} | Score = {score}')

        if len(cleaned) == sum(row.count('D') for row in grid):
            print('All dirt cleaned!')
            break

    print('Final Score:', score)
    print()

# -----------------------------
# Greedy Policy (nearest dirt)
# -----------------------------
def nearest_dirt(position, cleaned):
    q = deque([(position, [])])
    visited = {position}

    while q:
        (x, y), path = q.popleft()

        if grid[x][y] == 'D' and (x, y) not in cleaned:
            return path

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if valid(nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append(((nx, ny), path + [(nx, ny)]))

    return []

def greedy_policy():
    pos = start
    score = 0
    cleaned = set()

    print('--- Greedy Policy ---')
    print('Start:', pos)

    step = 0
    total_dirt = sum(row.count('D') for row in grid)

    while len(cleaned) < total_dirt:
        path = nearest_dirt(pos, cleaned)

        if not path:
            break

        for next_pos in path:
            step += 1
            pos = next_pos
            cell = grid[pos[0]][pos[1]]

            if cell == 'D' and pos not in cleaned:
                score += 1
                cleaned.add(pos)
            elif cell == 'O':
                score -= 1

            print(f'Step {step}: {pos} -> {cell} | Score = {score}')

    print('All reachable dirt cleaned!')
    print('Final Score:', score)
    print()

random_policy()
greedy_policy()
