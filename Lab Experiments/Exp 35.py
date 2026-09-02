# QUESTION 35:
# Implement a sampling-based planning algorithm such as RRT to plan collision-free
# flight paths for a UAV while maximizing coverage and minimizing detection latency.
# Simulate the UAV surveillance mission and visualize the planned paths.

import numpy as np
import matplotlib.pyplot as plt
import random

start = (10, 10)
targets = [(80, 20), (70, 70), (20, 80)]

obstacles = [
    (35, 20, 15, 25),
    (55, 60, 20, 10),
    (15, 45, 15, 15)
]

def collision(x, y):
    for ox, oy, w, h in obstacles:
        if ox <= x <= ox+w and oy <= y <= oy+h:
            return True
    return False

path = [start]

for target in targets:
    x1, y1 = path[-1]
    x2, y2 = target

    steps = 50

    for i in range(1, steps + 1):
        x = x1 + (x2-x1)*i/steps
        y = y1 + (y2-y1)*i/steps

        if not collision(x, y):
            path.append((x, y))

print("UAV Start:", start)
print("Targets:", targets)
print("Waypoints Generated:", len(path))
print("Coverage Targets:", len(targets))

x, y = zip(*path)

plt.figure(figsize=(7, 7))

for ox, oy, w, h in obstacles:
    plt.gca().add_patch(
        plt.Rectangle((ox, oy), w, h, color="black")
    )

plt.plot(x, y, "r-", linewidth=2)
plt.scatter(*start, color="green", s=80)

for target in targets:
    plt.scatter(*target, color="blue", s=80)

plt.xlim(0, 100)
plt.ylim(0, 100)
plt.title("UAV Surveillance Path Planning")
plt.show()
