"""10) A financial institution wants to optimize its investment strategy. Use a basic policy gradient
method to simulate and optimize the investment policy for maximum returns. Implement
this in Python."""
import gym
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers

env = gym.make("CartPole-v1")

num_actions = env.action_space.n
num_inputs = env.observation_space.shape[0]

model = tf.keras.Sequential([
    layers.Dense(24, activation="relu", input_shape=(num_inputs,)),
    layers.Dense(24, activation="relu"),
    layers.Dense(num_actions, activation="softmax")
])

optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)

gamma = 0.99

for episode in range(100):
    state = env.reset()

    if isinstance(state, tuple):
        state = state[0]

    rewards = []
    log_probs = []

    done = False

    while not done:
        state_tensor = tf.convert_to_tensor([state], dtype=tf.float32)

        probs = model(state_tensor)
        action = np.random.choice(num_actions, p=np.squeeze(probs))

        result = env.step(action)

        if len(result) == 5:
            next_state, reward, terminated, truncated, info = result
            done = terminated or truncated
        else:
            next_state, reward, done, info = result

        rewards.append(reward)

        log_prob = tf.math.log(probs[0, action])
        log_probs.append(log_prob)

        state = next_state

    discounted_rewards = []
    G = 0

    for r in rewards[::-1]:
        G = r + gamma * G
        discounted_rewards.insert(0, G)

    discounted_rewards = np.array(discounted_rewards)
    discounted_rewards = (discounted_rewards - np.mean(discounted_rewards)) / (
        np.std(discounted_rewards) + 1e-8
    )

    with tf.GradientTape() as tape:
        loss = 0
        for log_prob, G in zip(log_probs, discounted_rewards):
            loss += -log_prob * G

    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))

    print("Episode:", episode + 1, "Reward:", sum(rewards))

print("Training Completed")
