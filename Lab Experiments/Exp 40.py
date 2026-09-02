# QUESTION 40:
# An autonomous robot navigates through a partially observable environment
# with limited sensor information and uncertainty.
# Implement a POMDP framework for localization and navigation.

import random

states = ["Left", "Center", "Right"]
actions = ["Move Left", "Move Right", "Stay"]

state = "Center"
steps = 10

print("POMDP Robot Navigation")

for i in range(steps):
    action = random.choice(actions)

    if action == "Move Left" and state != "Left":
        state = states[states.index(state) - 1]

    elif action == "Move Right" and state != "Right":
        state = states[states.index(state) + 1]

    observation = random.choice(["Obstacle", "Free"])

    print(
        "Step:", i + 1,
        "Action:", action,
        "Observation:", observation,
        "Estimated State:", state
    )

print("Final Robot State:", state)
