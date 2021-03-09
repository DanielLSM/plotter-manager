import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

import numpy as np

from utils import moving_average, save_pickle, load_pickle

DATA_DIR = "data/"
OUTPUT_DIR = "figs/"


def plot_data(x, y, title):
    plt.figure()
    plt.title(title)
    plt.plot(x, y)
    plt.show()


def get_axis_fig():
    fig, ax = plt.subplots()
    return fig, ax


def plot(axis, x, y):
    return axis.plot(x, y)


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


def plot_from_file(file_name,
                   param_name,
                   last_N=100,
                   color='blue',
                   limit_x=None,
                   limit_x_range=None,
                   range_y=None,
                   y_ticks=None):
    metadata = load_pickle(file_name)
    score = metadata[param_name]
    mean, std = moving_average(score, last_N=last_N)
    if limit_x is not None:
        episodes = range(limit_x)
        mean = mean[:limit_x]
        std = std[:limit_x]
    elif limit_x_range is not None:
        episodes = metadata[limit_x_range]
    else:
        episodes = range(len(score))
        mean, std = moving_average(score, last_N=last_N)

    lower_bound = [a_i - 0.5 * b_i for a_i, b_i in zip(mean, std)]
    upper_bound = [a_i + 0.5 * b_i for a_i, b_i in zip(mean, std)]
    # plt.plot(episodes, score)
    plt.fill_between(episodes,
                     lower_bound,
                     upper_bound,
                     facecolor=color,
                     alpha=0.5)
    plt.plot(episodes, mean, color=color)
    if range_y is not None:
        plt.ylim(range_y)
    if y_ticks is not None:
        plt.yticks(np.arange(range_y[0], range_y[1] + 2 * y_ticks, y_ticks))
    if limit_x_range is not None:
        plt.xlabel(limit_x_range)
    else:
        plt.xlabel("episodes")
    plt.ylabel(param_name)


def plot_files(*file_names,
               param_name,
               limit_x=None,
               limit_x_range=None,
               range_y=None,
               y_ticks=None,
               last_N=100,
               legend=False):

    colors = ['blue', 'green', 'red', 'yellow']
    # import ipdb
    # ipdb.set_trace()
    for _ in range(len(file_names[0])):
        plot_from_file(
            file_name=file_names[0][_],
            param_name=param_name,
            color=colors[_],
            limit_x=limit_x,
            limit_x_range=limit_x_range,
            range_y=range_y,
            y_ticks=y_ticks,
            last_N=last_N,
        )
    if legend:
        patches = [
            mpatches.Patch(color=colors[_], label=file_names[0][_])
            for _ in range(len(file_names[0]))
        ]
        plt.legend(handles=patches)


if __name__ == '__main__':
    plot_files(['00_25', '25_50'],
               param_name='return',
               last_N=100,
               limit_x=None,
               limit_x_range='steps_return',
               range_y=None,
               y_ticks=None,
               legend=True)
