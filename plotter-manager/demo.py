from plot import get_axis_fig, set_labels, set_grid
from plot import plot, show, save_figure

import numpy as np


def demo_plot_sin():
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)
    fig, ax = get_axis_fig()
    plot(ax, t, s)
    set_labels(ax,
               x_label='time (s)',
               y_label='voltage (mV)',
               title='About as simple as it gets, folks')
    set_grid(ax)
    show()


if __name__ == "__main__":
    demo_plot_sin()