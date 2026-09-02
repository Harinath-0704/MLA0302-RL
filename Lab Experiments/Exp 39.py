# QUESTION 39:
# A team of autonomous robots collaborates to accomplish a complex task.
# Implement a simple multi-agent reinforcement learning approach to coordinate
# robot actions and achieve collective objectives.

import random

robots = ["Robot 1", "Robot 2", "Robot 3"]

actions = ["Move", "Search", "Deliver"]

total_reward = 0

for robot in robots:
    action = random.choice(actions)
    reward = random.randint(5, 15)

    total_reward += reward

    print(robot, "Action:", action, "Reward:", reward)

print()
print("Number of Robots:", len(robots))
print("Total Team Reward:", total_reward)
print("Average Reward:", round(total_reward / len(robots), 2))
