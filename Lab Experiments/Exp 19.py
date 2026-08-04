import pandas as pd
from google.colab import files

# ----------------------------
# Upload CSV file
# ----------------------------
uploaded = files.upload()

# Get uploaded file name
file_name = list(uploaded.keys())[0]

# Load dataset
df = pd.read_csv(file_name)

print("Dataset Loaded Successfully\n")
print(df.head())

# ----------------------------
# Reward Function
# +1 = customer stays
# -1 = customer churns
# ----------------------------
df["reward"] = df["churn"].apply(lambda x: -1 if x == 1 else 1)

# ----------------------------
# Monte Carlo Policy Evaluation
# ----------------------------
returns = {}
counts = {}

for _, row in df.iterrows():
    state = row["state"]
    G = row["reward"]

    returns[state] = returns.get(state, 0) + G
    counts[state] = counts.get(state, 0) + 1

# Calculate state values
V = {}

print("\nMonte Carlo State Values\n")
for state in returns:
    V[state] = returns[state] / counts[state]
    print(f"State: {state:6s}  V(s): {V[state]:.3f}")

# ----------------------------
# Policy Evaluation
# ----------------------------
policy_values = df.groupby("policy_action")["reward"].mean()

print("\nPolicy Evaluation\n")
print(policy_values)

overall_return = df["reward"].mean()

print(f"\nOverall Expected Return: {overall_return:.3f}")

print("\nInterpretation:")
print("Positive value  - policy tends to retain customers")
print("Negative value  - policy is associated with more churn")
print("Higher state value means customers in that state are more likely to stay subscribed.")
