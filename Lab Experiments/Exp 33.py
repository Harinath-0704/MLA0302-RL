# QUESTION 33:
# Implement a value-equivalence prediction model to estimate the long-term performance
# of different investment portfolios using historical financial data and machine learning.

import numpy as np
from sklearn.linear_model import LinearRegression

np.random.seed(5)

returns = np.random.normal(0.08, 0.03, 100)

X = np.arange(100).reshape(-1, 1)
y = returns

model = LinearRegression()
model.fit(X, y)

portfolios = {
    "Conservative": 0.05,
    "Balanced": 0.08,
    "Aggressive": 0.12
}

investment = 100000

print("Initial Investment:", investment)
print()

for name, rate in portfolios.items():
    predicted = investment * (1 + rate) ** 5
    print(name, "5-Year Predicted Value:", round(predicted, 2))
