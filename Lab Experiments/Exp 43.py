# QUESTION 43:
# Apply reinforcement learning techniques to optimize natural resource management.
# Develop a simulation environment that models resource dynamics and environmental
# constraints and learn policies that balance resource utilization and sustainability.

import random

resource = 100
total_reward = 0

for year in range(1, 11):

    action = random.choice(["Low Use", "Medium Use", "High Use"])

    if action == "Low Use":
        usage = 10
        reward = 8
    elif action == "Medium Use":
        usage = 20
        reward = 12
    else:
        usage = 35
        reward = 5

    resource -= usage

    if resource < 30:
        reward -= 5

    resource += 15

    total_reward += reward

    print(
        "Year:", year,
        "Action:", action,
        "Resource:", resource,
        "Reward:", reward
    )

print()
print("Final Resource Level:", resource)
print("Total Reward:", total_reward)

if resource >= 50:
    print("Sustainability Status: GOOD")
else:
    print("Sustainability Status: POOR")
