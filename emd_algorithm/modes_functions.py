import numpy as np


def get_amplitude(y):
    maximum = y[0]
    minimum = y[0]
    for i in range(len(y)):
        if y[i] < minimum:
            minimum = y[i]
        if y[i] > maximum:
            maximum = y[i]
    return maximum - minimum


def check_orthogonality(imfs):
    num_imfs = len(imfs)
    total_sum = 0.0

    for i in range(num_imfs):
        for j in range(i + 1, num_imfs):
            product_sum = np.sum(imfs[1][i] * imfs[1][j])
            total_sum += product_sum

    if total_sum >= 1:
        return False
    return True
