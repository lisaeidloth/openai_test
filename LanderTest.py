import gym

if __name__ == '__main__':
    env = gym.make(
        "LunarLander-v2",
        continuous=False,
        gravity=-5.0,
        enable_wind=False,
        turbulence_power=0
    )

    observation, info = env.reset(seed=110, return_info=True)

    for _ in range(1000):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)

        if done:
            observation, info = env.reset(return_info=True)
    env.close()

