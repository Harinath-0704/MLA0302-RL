# QUESTION 37:
# Multiple agents collaborate to solve a cooperative task.
# Implement the MAXQ framework to decompose the task into hierarchically
# organized subtasks and learn policies for each level.

import random

tasks = ["Collect", "Transport", "Deliver"]

agents = {
    "Agent 1": "Collect",
    "Agent 2": "Transport",
    "Agent 3": "Deliver"
}

completed = []

for agent, task in agents.items():
    reward = random.randint(8, 15)

    print(agent, "executing", task)
    print("Reward:", reward)

    if reward >= 10:
        completed.append(task)

print()
print("Completed Subtasks:", completed)
print("Total Completed:", len(completed), "/", len(tasks))

if len(completed) == len(tasks):
    print("Overall Task: SUCCESS")
else:
    print("Overall Task: PARTIAL SUCCESS")
