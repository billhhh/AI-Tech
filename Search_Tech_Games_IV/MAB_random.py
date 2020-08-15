# bill

import random
import numpy as np


def mean(values):
    return sum(values) * 1.0 / len(values)


# BernoulliArm
class Arm():
    def __init__(self, arm_id, p):
        self.arm_id = arm_id
        self.p = p
        self.expectation = p

    def pull(self):
        if random.random() > self.p:
            return 0.0
        else:
            return 1.0


class RandomAgent(object):

    def __init__(self, arms):
        self.arms = arms
        self.values = [[] for i in arms]

    def select_arm(self):

        arm_idx = self.get_random_arm_idx()

        arm = self.arms[arm_idx]
        reward = arm.pull()
        self.update(arm_idx, reward)

    def update(self, arm_idx, reward):
        self.values[arm_idx].append(reward)

    def get_random_arm_idx(self):
        return random.randrange(len(self.arms))


if __name__ == "__main__":
    epsilon = 0.1
    possibilities = [random.random() for i in range(10)]
    arms = [Arm(i, p) for i, p in enumerate(possibilities)]
    algo = RandomAgent(arms)
    for i in range(100):
        algo.select_arm()
    total_reward = 0
    for i, vals in enumerate(algo.values):
        total_reward += sum(vals)
    print("reward:", total_reward, "\t epsilon:", epsilon)
