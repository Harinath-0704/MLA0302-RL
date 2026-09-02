# QUESTION 42:
# Apply reinforcement learning to optimize healthcare management processes
# such as patient scheduling and resource allocation.
# Simulate patient flow, resource constraints, and treatment outcomes.

import random

patients = 20
resources = 5

treated = 0
waiting = 0
total_cost = 0

for i in range(patients):

    if resources > 0:
        resources -= 1
        treated += 1
        reward = 10
        total_cost += 5

        print("Patient", i + 1, "Treated", "Reward:", reward)

        if random.random() < 0.6:
            resources += 1
    else:
        waiting += 1
        total_cost += 2

        print("Patient", i + 1, "Waiting")

print()
print("Total Patients:", patients)
print("Patients Treated:", treated)
print("Patients Waiting:", waiting)
print("Total Cost:", total_cost)
print("Treatment Rate:", round(treated / patients * 100, 2), "%")
