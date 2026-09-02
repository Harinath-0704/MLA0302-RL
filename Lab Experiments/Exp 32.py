# QUESTION 32:
# A retail company aims to optimize its inventory management strategy using model-based RL.
# Develop a data generation model that simulates customer demand and inventory dynamics.
# Generate synthetic data and evaluate different inventory management policies.

import numpy as np

np.random.seed(10)

days = 100
inventory = 50
total_cost = 0

demand_data = np.random.poisson(8, days)

for day in range(days):
    demand = demand_data[day]

    sales = min(inventory, demand)
    inventory -= sales

    holding_cost = inventory * 1
    shortage_cost = max(0, demand - sales) * 5

    if inventory < 20:
        inventory += 30

    total_cost += holding_cost + shortage_cost

print("Days Simulated:", days)
print("Average Demand:", round(np.mean(demand_data), 2))
print("Final Inventory:", inventory)
print("Total Cost:", total_cost)
print("Inventory Policy: Reorder when inventory < 20")
