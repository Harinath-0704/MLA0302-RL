import numpy as np

states = 16
actions = 4

gamma = 0.9

policy = np.zeros(states, dtype=int)
value = np.zeros(states)

reward = np.full(states, -1)
reward[15] = 10

stable = False

while not stable:

    while True:

        delta = 0

        for s in range(states):

            v = value[s]

            value[s] = reward[s] + gamma * value[s]

            delta = max(delta, abs(v - value[s]))

        if delta < 0.001:
            break

    stable = True

    for s in range(states):

        old_action = policy[s]

        action_values = []

        for a in range(actions):
            action_values.append(reward[s] + gamma * value[s])

        policy[s] = np.argmax(action_values)

        if old_action != policy[s]:
            stable = False

print("Optimal Policy")
print(policy)

print("\nState Values")
print(value)
