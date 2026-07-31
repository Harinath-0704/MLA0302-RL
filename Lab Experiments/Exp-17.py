import gym
from stable_baselines3 import DDPG

env = gym.make("Pendulum-v1")

model = DDPG(
    "MlpPolicy",
    env,
    verbose=1
)

model.learn(total_timesteps=10000)

obs = env.reset()

if isinstance(obs, tuple):
    obs = obs[0]

for i in range(100):

    action, _ = model.predict(obs)

    result = env.step(action)

    if len(result) == 5:
        obs, reward, terminated, truncated, info = result
        done = terminated or truncated
    else:
        obs, reward, done, info = result

    env.render()

    if done:
        obs = env.reset()
        if isinstance(obs, tuple):
            obs = obs[0]

env.close()
