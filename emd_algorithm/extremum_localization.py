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


def get_maximum_to_inter(x, y):
    # Создаем зеркальные отражения сигнала
    y_left_reflected = np.concatenate((np.flip(y), y))
    y_right_reflected = y

    # Создаем соответствующие массивы x для зеркальных отражений
    x_left_reflected = -np.flip(x)
    x_right_reflected = np.concatenate((x, x[-1] + (x[-1] - x[-2]) * np.arange(1, len(y) + 1)))
    new_x = np.concatenate((x_left_reflected, x_right_reflected))
    new_y = np.concatenate((y_left_reflected, y_right_reflected))
    local_max_indices = argrelextrema(new_y, np.greater)

    return new_x[local_max_indices], new_y[local_max_indices]


def get_minimum_to_inter(x, y):
    # Создаем зеркальные отражения сигнала
    y_left_reflected = np.concatenate((np.flip(y), y))
    y_right_reflected = y

    # Создаем соответствующие массивы x для зеркальных отражений
    x_left_reflected = -np.flip(x)
    x_right_reflected = np.concatenate((x, x[-1] + (x[-1] - x[-2]) * np.arange(1, len(y) + 1)))
    new_x = np.concatenate((x_left_reflected, x_right_reflected))
    new_y = np.concatenate((y_left_reflected, y_right_reflected))
    local_max_indices = argrelextrema(new_y, np.less)

    return new_x[local_max_indices], new_y[local_max_indices]
