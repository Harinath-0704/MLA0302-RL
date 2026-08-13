"""8) Simulate an autonomous car navigating a simple road network with intersections. Design
policies for the car to follow traffic rules and reach the destination safely. Implement these
policies in Python and evaluate their effectiveness."""
import numpy as np

# Road network (3x3)
rows, cols = 3, 3
start = (0, 0)
goal = (2, 2)

# Policy: Move Right, otherwise Down
def policy(state):
    x, y = state

    if y < cols - 1:
        return (x, y + 1), "RIGHT"
    elif x < rows - 1:
        return (x + 1, y), "DOWN"
    else:
        return state, "STOP"

# Simulation
state = start
path = [state]
steps = 0

while state != goal:
    state, action = policy(state)
    path.append(state)
    steps += 1

print("Path Followed:")
for p in path:
    print(p)

print("\nTotal Steps:", steps)

# Evaluate Policy
if state == goal:
    print("Destination reached safely.")
else:
    print("Policy failed.")
