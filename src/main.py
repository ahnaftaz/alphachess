"""Main entry point for AlphaZero Connect Four training."""

from pettingzoo.classic import connect_four_v3

def main():
    """Main function to run AlphaZero training."""

    # Render mode can either be for showing us the real game
    # or headless when actually training
    env = connect_four_v3.env(render_mode="human")
    # Seed helps us make sure everything runs the same for all of us
    env.reset(seed=42)

    for agent in env.agent_iter():
        # Each time a step/ action is taken, the below variables are updated
        # and then fetched using the env.last() method
        observation, reward, termination, truncation, info = env.last()

        if termination or truncation:
            # Refers to when the game ends (win, loss, etc) for termination
            # and for when the game is cancelled after going for too long
            action = None
        else:
            # If game is not over, pick an action using the policy network
            # or randomly like in this demo code below
            mask = observation["action_mask"]
            # this is where we would insert our policy model that we train
            action = env.action_space(agent).sample(mask)

        # We move to the next state by taking the chosen action
        env.step(action)
    # At the end of the game, we have to close the environment to free memory
    env.close()

    print("Demo completed!")

if __name__ == "__main__":
    # Uncomment the function you want to run
    main()