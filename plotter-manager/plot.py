import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

import numpy as np

DATA_DIR = "data/"
OUTPUT_DIR = "figs/"


def get_axis_fig():
    fig, ax = plt.subplots()
    return fig, ax


def plot(axis, x, y):
    assert len(x) == len(y)
    axis.plot(x, y)


def set_labels(axis, x_label, y_label, title):
    axis.set(xlabel=x_label, ylabel=y_label, title=title)


def set_grid(axis):
    axis.grid()


def save_figure(fig, fig_name):
    fig.savefig(OUTPUT_DIR + fig_name)


def load_IEEE_settings():
    matplotlib.rcParams['svg.fonttype'] = 'none'
    matplotlib.rcParams['font.family'] = 'sans-serif'
    matplotlib.rcParams['font.sans-serif'] = 'Latin Modern Math'
    matplotlib.rcParams['font.size'] = 10


def show():
    plt.show()