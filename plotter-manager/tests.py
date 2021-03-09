import numpy as np
import matplotlib.pyplot as plt
from plot import plot, get_axis_fig, plot_files

from unittest import mock
import plot as my_plot

##########################################################
# Testing if linear data after plotting with plot and get_axix_fig is equal


def test_plot_linear():
    x, y = [0, 1, 2], [0, 1, 2]
    fig, ax = get_axis_fig()
    line, = plot(ax, x, y)
    x_plot, y_plot = line.get_xydata().T
    np.testing.assert_array_equal(x_plot, y_plot)
