# QUESTION 31:
# An autonomous exploration robot needs to navigate and map an unknown environment.
# Implement a sampling-based planning algorithm such as RRT to plan collision-free paths.
# Simulate the robot's exploration process and visualize the generated paths.

import numpy as np
import matplotlib.pyplot as plt
import random

start = (10, 10)
goal = (90, 90)

obstacles = [
    (20, 20, 20, 10),
    (50, 30, 15, 25),
    (30, 65, 30, 10),
    (70, 60, 15, 20)
]

def collision(p):
    x, y = p
    for ox, oy, w, h in obstacles:
        if ox <= x <= ox+w and oy <= y <= oy+h:
            return True
    return False

nodes = [start]
parent = {start: None}

for _ in range(1500):
    sample = (random.randint(0, 100), random.randint(0, 100))
    nearest = min(nodes, key=lambda p: np.linalg.norm(np.array(p)-sample))

    direction = np.array(sample) - np.array(nearest)
    length = np.linalg.norm(direction)

    if length == 0:
        continue

    direction = direction / length
    new = tuple(np.array(nearest) + direction * 3)

    if not collision(new) and 0 <= new[0] <= 100 and 0 <= new[1] <= 100:
        new = (round(new[0], 2), round(new[1], 2))
        nodes.append(new)
        parent[new] = nearest

        if np.linalg.norm(np.array(new)-goal) < 5:
            parent[goal] = new
            nodes.append(goal)
            break

path = []
p = goal

if p in parent:
    while p is not None:
        path.append(p)
        p = parent[p]

path.reverse()

print("Start:", start)
print("Goal:", goal)
print("Nodes Generated:", len(nodes))
print("Path Found:", len(path) > 0)
print("Path Length:", len(path))

plt.figure(figsize=(7, 7))

for ox, oy, w, h in obstacles:
    plt.gca().add_patch(
        plt.Rectangle((ox, oy), w, h, color="black")
    )

for node in nodes:
    if parent[node] is not None:
        plt.plot(
            [node[0], parent[node][0]],
            [node[1], parent[node][1]],
            "gray",
            linewidth=0.5
        )

if path:
    x, y = zip(*path)
    plt.plot(x, y, "r-", linewidth=2)

plt.scatter(*start, color="green", s=80, label="Start")
plt.scatter(*goal, color="blue", s=80, label="Goal")
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.title("RRT Autonomous Robot Path Planning")
plt.legend()
plt.show()
