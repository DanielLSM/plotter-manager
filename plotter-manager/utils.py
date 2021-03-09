import numpy as np
import pickle as pkl
from datetime import datetime


def save_pickle(obj, name):
    with open("data/" + name + ".pkl", 'wb') as handle:
        pkl.dump(obj, handle, protocol=pkl.HIGHEST_PROTOCOL)


def load_pickle(name):
    with open("data/" + name + ".pkl", 'rb') as handle:
        return pkl.load(handle)