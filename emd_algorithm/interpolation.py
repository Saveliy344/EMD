import numpy as np
from scipy.interpolate import CubicSpline


# old_x and old_y are points to make CubicSpline
# x is used to generate points in the same places in chart where they exists
def interpolation(x, old_x, old_y):
    cs = CubicSpline(old_x, old_y)
    new_y = cs(x)
    return x, new_y


def get_medium(x_1, y_1, x_2, y_2):
    medium_x = np.array([(x_1[i] + x_2[i]) / 2 for i in range(len(x_1))])
    medium_y = np.array([(y_1[i] + y_2[i]) / 2 for i in range(len(y_1))])
    return medium_x, medium_y


def get_diff(y_1, y_2):
    diff_y = np.array([y_1[i] - y_2[i] for i in range(len(y_1))])
    return diff_y
