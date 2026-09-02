# QUESTION 41:
# An autonomous system makes decisions with ethical implications.
# Implement ethical considerations using reinforcement learning techniques,
# including fairness constraints and avoiding harmful decisions.

import random

actions = ["Help Person A", "Help Person B", "Reject Request"]

scores = {
    "Help Person A": 0,
    "Help Person B": 0,
    "Reject Request": 0
}

for i in range(10):
    action = random.choice(actions)

    if action == "Reject Request":
        reward = -2
    else:
        reward = 5

    scores[action] += reward

    print(
        "Decision:", action,
        "Reward:", reward
    )

print()
print("Ethical Decision Scores:")

for action, score in scores.items():
    print(action, ":", score)

best = max(scores, key=scores.get)
print("Preferred Ethical Action:", best)
