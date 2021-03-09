import numpy as np
import pickle5 as pkl
from datetime import datetime


def save_pickle(obj, name):
    with open("data/" + name + ".pkl", 'wb') as handle:
        pkl.dump(obj, handle, protocol=pkl.HIGHEST_PROTOCOL)


def load_pickle(name):
    with open("data/" + name + ".pkl", 'rb') as handle:
        return pkl.load(handle)


def return_date():
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
    return dt_string


def moving_average(rewards, last_N):
    scores = []
    averages = []
    stds = []
    for _ in range(len(rewards)):
        scores.append(rewards[_])
        average = sum(scores[-last_N:]) / len(scores[-last_N:])
        averages.append(average)
        x = scores[-last_N:]
        x_mean = averages[-last_N:]
        diff = []
        for _ in range(len(x)):
            diff.append((abs(x[_] - x_mean[_]))**(1 / 2))
        diff_sum = sum(diff)

        stds.append(diff_sum / last_N)

    return averages, stds