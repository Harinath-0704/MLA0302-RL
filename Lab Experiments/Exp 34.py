# QUESTION 34:
# A dynamic pricing platform aims to optimize its pricing strategy using model-based RL.
# Develop a predictive model for customer demand and dynamically adjust prices.

import numpy as np

np.random.seed(2)

prices = np.array([50, 60, 70, 80, 90])
base_demand = 100

print("Dynamic Pricing Simulation")

for day in range(10):
    price = np.random.choice(prices)

    demand = max(0, int(base_demand - 0.8 * price +
                         np.random.normal(0, 5)))

    revenue = price * demand

    if demand > 50:
        price += 10
    else:
        price -= 10

    print(
        "Day:", day + 1,
        "Demand:", demand,
        "Revenue:", revenue,
        "Next Price:", price
    )
