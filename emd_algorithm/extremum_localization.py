import numpy as np
from scipy.signal import argrelextrema


def get_maximum(x, y):
    local_max_indices = argrelextrema(y, np.greater)
    local_max_x = x[local_max_indices]
    local_max_y = y[local_max_indices]
    return local_max_x, local_max_y


def get_minimum(x, y):
    local_min_indices = argrelextrema(y, np.less)
    local_min_x = x[local_min_indices]
    local_min_y = y[local_min_indices]
    return local_min_x, local_min_y
