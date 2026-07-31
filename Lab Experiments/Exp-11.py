import numpy as np
import random
from collections import deque
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

state_size = 10
action_size = 3

memory = deque(maxlen=2000)

gamma = 0.95
epsilon = 1.0
epsilon_decay = 0.995
epsilon_min = 0.01

model = Sequential()
model.add(Dense(24, input_dim=state_size, activation="relu"))
model.add(Dense(24, activation="relu"))
model.add(Dense(action_size, activation="linear"))

model.compile(loss="mse", optimizer=Adam(learning_rate=0.001))

target_model = Sequential()
target_model.add(Dense(24, input_dim=state_size, activation="relu"))
target_model.add(Dense(24, activation="relu"))
target_model.add(Dense(action_size, activation="linear"))

target_model.compile(loss="mse", optimizer=Adam(learning_rate=0.001))

target_model.set_weights(model.get_weights())

for episode in range(50):

    state = np.random.rand(1, state_size)

    for step in range(100):

        if np.random.rand() <= epsilon:
            action = random.randrange(action_size)
        else:
            action = np.argmax(model.predict(state, verbose=0)[0])

        next_state = np.random.rand(1, state_size)

        reward = random.randint(-5, 10)

        done = random.choice([True, False])

        memory.append((state, action, reward, next_state, done))

        state = next_state

        if len(memory) > 32:

            minibatch = random.sample(memory, 32)

            for s, a, r, ns, d in minibatch:

                target = model.predict(s, verbose=0)

                if d:
                    target[0][a] = r
                else:
                    best_action = np.argmax(model.predict(ns, verbose=0)[0])
                    target_q = target_model.predict(ns, verbose=0)[0][best_action]
                    target[0][a] = r + gamma * target_q

                model.fit(s, target, epochs=1, verbose=0)

        if done:
            break

    target_model.set_weights(model.get_weights())

    if epsilon > epsilon_min:
        epsilon *= epsilon_decay

    print("Episode:", episode + 1, "Completed")

print("Training Finished")
