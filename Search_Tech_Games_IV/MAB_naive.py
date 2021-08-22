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


class NaiveAlgorithm(object):

    def __init__(self, arms, explore_n=5):
        self.arms = arms
        self.explore_n = explore_n
        self.values = [[] for i in arms]

    def select_arm(self):

        trail_n_list = [len(self.values[i]) for i in range(len(arms))]  # how many times have been tried
        trail_n = np.array(trail_n_list)
        if np.any(trail_n < self.explore_n):  # if have been explored less than specified
            arm_idx = np.argmin(trail_n)  # return the one least explored
        else:  # return the best mean forever
            estimated_means = [np.mean(self.values[i]) for i in range(len(arms))]  # the current means
            best_mean = np.argmax(estimated_means)  # the best mean
            return best_mean

        arm = self.arms[arm_idx]
        reward = arm.pull()
        self.update(arm_idx, reward)

    def update(self, arm_idx, reward):
        self.values[arm_idx].append(reward)


if __name__ == "__main__":
    possibilities = [random.random() for i in range(10)]
    arms = [Arm(i, p) for i, p in enumerate(possibilities)]
    algo = NaiveAlgorithm(arms, 5)
    for i in range(100):
        algo.select_arm()
    total_reward = 0
    for i, vals in enumerate(algo.values):
        total_reward += sum(vals)
    print("reward:", total_reward)
