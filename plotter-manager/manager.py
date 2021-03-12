from abc import ABC, abstractmethod

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

from utils import moving_average, save_pickle, load_pickle

from plot import plot_data


class Plotter(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def plot_data(self):
        return NotImplemented

    @abstractmethod
    def plot_from_file(self):
        return NotImplemented

    @abstractmethod
    def plot_files(self):
        return NotImplemented

    @abstractmethod
    def show(self):
        return NotImplemented

    @abstractmethod
    def get_axis_fig(self):
        return NotImplemented

    @abstractmethod
    def save_figure(self):
        return NotImplemented


class StaticPlotter(Plotter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.axis = None
        self.figure = None

    def plot_files(self):
        raise NotImplementedError

    def plot_from_file(self):
        raise NotImplementedError

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
        fig.savefig(OUTPUT_DIR + fig_name)

    def show(self):
        plt.show()


if __name__ == '__main__':
    sp = StaticPlotter()