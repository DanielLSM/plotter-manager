from abc import ABC, abstractmethod

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

from utils import moving_average, save_pickle, load_pickle

from plot import plot_data


class Plotter(ABC):
    def __init__(self, **kwargs):
        self.__DATA_DIR = None
        self.__OUTPUT_DIR = None

    @abstractmethod
    def plot_files(self):
        return NotImplemented

    @abstractmethod
    def plot_from_file(self):
        return NotImplemented

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

    def plot_files(self):
        raise NotImplementedError

    def plot_from_file(self):
        raise NotImplementedError


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

    def plot_files(self):
        raise NotImplementedError

    def plot_from_file(self):
        raise NotImplementedError


if __name__ == '__main__':
    sp = StaticPlotter()
    sieee = IEEEPlotter()