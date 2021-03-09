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


##########################################################
# Testing if squared data after plotting with plot and get_axix_fig is equal


def plot_square(x, y):
    y_squared = np.square(y)
    return plt.plot(x, y_squared)


def test_plot_square():
    x, y = [0, 1, 2], [0, 1, 2]
    line, = plot_square(x, y)
    x_plot, y_plot = line.get_xydata().T
    np.testing.assert_array_equal(y_plot, np.square(y))


##########################################################
# Testing if simple plot data, plots the title correctly
# and is only called once


@mock.patch("%s.my_plot.plt" % __name__)
def test_plot_data_title(mock_plt):
    x = np.arange(0, 5, 0.1)
    y = np.sin(x)
    my_plot.plot_data(x, y, "my title")

    # Assert plt.title has been called with expected title arg
    mock_plt.title.assert_called_once_with("my title")

    # Assert plt.figure got called
    assert mock_plt.figure.called


##########################################################
# Testing plot_from_file to check if the labels are plotted correctly


@mock.patch("%s.my_plot.plt" % __name__)
def test_plot_from_file_xy_label(mock_plt):
    my_plot.plt.figure()
    my_plot.plot_from_file(file_name="00_25",
                           param_name="return",
                           limit_x_range='steps_return')
    my_plot.show()

    # Assert plt.xlabel and y has been called with expected title arg
    mock_plt.xlabel.assert_called_once_with("steps_return")
    mock_plt.ylabel.assert_called_once_with("return")

    # Assert plt.figure got called
    assert mock_plt.figure.called