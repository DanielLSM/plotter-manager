from abc import ABC, abstractmethod


class PlotterManager(ABC):
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


if __name__ == '__main__':
    pass