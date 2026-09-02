# QUESTION 36:
# A logistics company aims to optimize supply chain operations using model-based RL.
# Simulate order fulfillment, inventory flows, and transportation networks.
# Generate synthetic data and evaluate supply chain management policies.

import numpy as np

np.random.seed(20)

days = 50
inventory = 100
orders = np.random.randint(5, 20, days)

total_cost = 0
fulfilled = 0

for order in orders:
    if inventory >= order:
        inventory -= order
        fulfilled += order
    else:
        shortage = order - inventory
        inventory = 0
        total_cost += shortage * 10

    total_cost += inventory * 0.5

    if inventory < 30:
        inventory += 50
        total_cost += 100

print("Simulation Days:", days)
print("Total Orders Fulfilled:", fulfilled)
print("Final Inventory:", inventory)
print("Total Supply Chain Cost:", round(total_cost, 2))
