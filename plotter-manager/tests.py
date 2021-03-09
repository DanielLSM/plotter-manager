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


##########################################################
# Testing plot_from_file to check if fill between is called with
# proper alpha


@mock.patch("%s.my_plot.plt" % __name__)
def test_plot_from_file_fill_between(mock_plt):
    my_plot.plt.figure()
    my_plot.plot_from_file(file_name="00_25",
                           param_name="return",
                           limit_x_range='steps_return')
    my_plot.show()

    # Assert plt.fillbetween has been called
    mock_plt.fill_between.assert_called_once()

    # Assert plt.figure got called
    assert mock_plt.figure.called


##########################################################
# Testing plot_from_file to check if calls with range limits are correct


@mock.patch("%s.my_plot.plt" % __name__)
def test_plot_from_file_ranges(mock_plt):
    my_plot.plt.figure()
    range_y = [-1, 1]
    my_plot.plot_from_file(file_name="00_25",
                           param_name="return",
                           limit_x_range='steps_return',
                           limit_x=1000,
                           range_y=range_y)
    my_plot.show()

    # Assert plt.ylim has been called with expected title arg
    mock_plt.ylim.assert_called_once_with(range_y)

    # Assert plt.figure got called
    assert mock_plt.figure.called


##########################################################
# Testing plot_from_file to check if calls with yticks are correct


@mock.patch("%s.my_plot.plt" % __name__)
def test_plot_from_file_yticks(mock_plt):
    my_plot.plt.figure()
    range_y = [-1, 1]
    y_ticks = 0.01
    my_plot.plot_from_file(file_name="00_25",
                           param_name="return",
                           limit_x_range='steps_return',
                           limit_x=1000,
                           range_y=range_y,
                           y_ticks=y_ticks)
    my_plot.show()

    # Assert plt.yticks has been called with expected title arg
    mock_plt.yticks.assert_called_once()

    # Assert plt.figure got called
    assert mock_plt.figure.called


##########################################################
# multiple plot 2 files to check if the legend is correctly called


@mock.patch("%s.my_plot.plt" % __name__)
def test_2_plot_files_legend(mock_plt):
    my_plot.plt.figure()
    my_plot.plot_files(['00_25', '25_50'],
                       param_name='return',
                       last_N=100,
                       limit_x=None,
                       limit_x_range='steps_return',
                       range_y=None,
                       y_ticks=None,
                       legend=True)

    my_plot.show()

    # Assert plt.legend has been called with expected title arg
    mock_plt.legend.assert_called_once()

    # Assert plt.figure got called
    assert mock_plt.figure.called


##########################################################
# multiple plot 4 files to check if the legend is correctly called


@mock.patch("%s.my_plot.plt" % __name__)
def test_4_plot_files_legend(mock_plt):
    my_plot.plt.figure()
    my_plot.plot_files(['00_25', '25_50', '50_75', '75_100'],
                       param_name='return',
                       last_N=100,
                       limit_x=None,
                       limit_x_range='steps_return',
                       range_y=None,
                       y_ticks=None,
                       legend=True)

    my_plot.show()

    # Assert plt.legend has been called with expected title arg
    mock_plt.legend.assert_called_once()

    # Assert plt.figure got called
    assert mock_plt.figure.called


##########################################################
# multiple plot 4 files checked if they are call plot exactly and only 4 times


@mock.patch("%s.my_plot.plt" % __name__)
def test_4_plot_files_colors(mock_plt):
    my_plot.plt.figure()
    my_plot.plot_files(['00_25', '25_50', '50_75', '75_100'],
                       param_name='return',
                       last_N=100,
                       limit_x=None,
                       limit_x_range='steps_return',
                       range_y=None,
                       y_ticks=None,
                       legend=True)

    my_plot.show()

    assert mock_plt.plot.call_count == 4

    # Assert plt.figure got called
    assert mock_plt.figure.called