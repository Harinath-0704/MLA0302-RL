import random

states = ["Idle", "Busy", "Completed"]
actions = ["Assign", "Wait"]

Q = {}

for s in states:
    Q[s] = {}
    for a in actions:
        Q[s][a] = 0

alpha = 0.1
gamma = 0.9
epsilon = 0.1

for episode in range(500):

    state = random.choice(states)

    while state != "Completed":

        if random.random() < epsilon:
            action = random.choice(actions)
        else:
            action = max(Q[state], key=Q[state].get)

        reward = random.randint(1, 10)

        next_state = random.choice(states)

        best = max(Q[next_state].values())

        Q[state][action] = Q[state][action] + alpha * (
            reward + gamma * best - Q[state][action]
        )

        state = next_state

print("Optimal Q Values")
print(Q)
