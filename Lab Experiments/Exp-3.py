"""3) An online retailer uses a multi-armed bandit approach to set prices dynamically. Simulate
different pricing strategies using epsilon-greedy, UCB, and Thompson Sampling. Write a
Python script to compare which strategy maximizes revenue over a series of pricing
decisions."""
import pandas as pd
import numpy as np
from google.colab import files

# -----------------------------
# Upload CSV file
# -----------------------------
print('Upload the pricing_bandit_data.csv file')
uploaded = files.upload()

# Read uploaded CSV
file_name = list(uploaded.keys())[0]
data = pd.read_csv(file_name)

prices = data['Price'].values
probs = data['Success_Probability'].values

arms = len(prices)
steps = 500

# -----------------------------
# Epsilon-Greedy
# -----------------------------
def epsilon_greedy(epsilon=0.1):
    counts = np.zeros(arms)
    values = np.zeros(arms)
    revenue = 0

    for _ in range(steps):
        if np.random.rand() < epsilon:
            arm = np.random.randint(arms)
        else:
            arm = np.argmax(values)

        reward = prices[arm] if np.random.rand() < probs[arm] else 0

        counts[arm] += 1
        values[arm] += (reward - values[arm]) / counts[arm]
        revenue += reward

    return revenue

# -----------------------------
# UCB (Upper Confidence Bound)
# -----------------------------
def ucb():
    counts = np.zeros(arms)
    values = np.zeros(arms)
    revenue = 0

    # Try each arm once
    for arm in range(arms):
        reward = prices[arm] if np.random.rand() < probs[arm] else 0
        counts[arm] = 1
        values[arm] = reward
        revenue += reward

    for t in range(arms, steps):
        ucb_values = values + np.sqrt((2 * np.log(t + 1)) / counts)
        arm = np.argmax(ucb_values)

        reward = prices[arm] if np.random.rand() < probs[arm] else 0

        counts[arm] += 1
        values[arm] += (reward - values[arm]) / counts[arm]
        revenue += reward

    return revenue

# -----------------------------
# Thompson Sampling
# -----------------------------
def thompson_sampling():
    alpha = np.ones(arms)
    beta = np.ones(arms)
    revenue = 0

    for _ in range(steps):
        samples = np.random.beta(alpha, beta)
        arm = np.argmax(samples)

        success = np.random.rand() < probs[arm]
        reward = prices[arm] if success else 0

        if success:
            alpha[arm] += 1
        else:
            beta[arm] += 1

        revenue += reward

    return revenue

# -----------------------------
# Run all strategies
# -----------------------------
epsilon_revenue = epsilon_greedy()
ucb_revenue = ucb()
thompson_revenue = thompson_sampling()

print('\\n===== Revenue Comparison =====')
print('Epsilon-Greedy Revenue :', epsilon_revenue)
print('UCB Revenue            :', ucb_revenue)
print('Thompson Sampling      :', thompson_revenue)

# Find best strategy
revenues = {
    'Epsilon-Greedy': epsilon_revenue,
    'UCB': ucb_revenue,
    'Thompson Sampling': thompson_revenue
}

best = max(revenues, key=revenues.get)

print('\\nBest Strategy:', best)
