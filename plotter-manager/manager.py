from abc import ABC, abstractmethod

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

from utils import moving_average, save_pickle, load_pickle
from utils import moving_std

from plot import plot_data

from mvgavg import mvgavg


class Plotter(ABC):
    def __init__(self, **kwargs):
        self.__DATA_DIR = None
        self.__OUTPUT_DIR = None

    def plot_files(self,
                   *file_names,
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
            self.plot_from_file(
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

    def plot_from_file(self,
                       file_name,
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
        std = moving_std(score, last_N=last_N)
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
            plt.yticks(np.arange(range_y[0], range_y[1] + 2 * y_ticks,
                                 y_ticks))
        if limit_x_range is not None:
            plt.xlabel(limit_x_range)
        else:
            plt.xlabel("episodes")
        plt.ylabel(param_name)

    def plot_data(self, x, y, title):
        plot_data(x=x, y=t, title=title)

    def get_axis_fig(self):
        fig, ax = plt.subplots()
        return fig, ax

    def plot(self, axis, x, y):
        return axis.plot(x, y)

    def set_labels(self, axis, x_label, y_label, title):
        axis.set(xlabel=x_label, ylabel=y_label, title=title)

    def set_grid(self, axis):
        axis.grid()

    def save_figure(self, fig, fig_name):
        fig.savefig(self.__OUTPUT_DIR + fig_name)

    def show(self):
        plt.show()

    def get_data_dir(self):
        return self.__DATA_DIR

    def get_output_dir(self):
        return self.__OUTPUT_DIR

    def set_data_dir(self, data_dir: str):
        self.__DATA_DIR = data_dir

    def set_output_dir(self, output_dir: str):
        self.__OUTPUT_DIR = output_dir


class StaticPlotter(Plotter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.axis = None
        self.figure = None
        self.__DATA_DIR = "data/"
        self.__OUTPUT_DIR = "figs/"


class IEEEPlotter(Plotter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.axis = None
        self.figure = None
        self.__DATA_DIR = "data/"
        self.__OUTPUT_DIR = "figs/"
        matplotlib.rcParams['svg.fonttype'] = 'none'
        matplotlib.rcParams['font.family'] = 'sans-serif'
        matplotlib.rcParams['font.sans-serif'] = 'Latin Modern Math'
        matplotlib.rcParams['font.size'] = 10


if __name__ == '__main__':
    sp = StaticPlotter()
    sieee = IEEEPlotter()

    sp.plot_files(['00_25', '25_50'],
                  param_name='return',
                  last_N=100,
                  limit_x=None,
                  limit_x_range='steps_return',
                  range_y=None,
                  y_ticks=None,
                  legend=True)
    sp.show()
