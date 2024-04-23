import numpy as np
from scipy.interpolate import CubicSpline


def interpolation(x, y):
    cs = CubicSpline(x, y)
    new_y = cs(x)
    return x, new_y


def get_medium(extremum_1_x, extremum_1_y, extremum_2_x, extremum_2_y):
    medium_x = np.array([(extremum_1_x[i] + extremum_2_x[i]) / 2 for i in range(len(extremum_1_x))])
    medium_y = np.array([(extremum_1_y[i] + extremum_2_y[i]) / 2 for i in range(len(extremum_1_y))])
    return medium_x, medium_y
