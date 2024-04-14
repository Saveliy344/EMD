import numpy as np


def generate_default_signal(start, stop, num_points, sinA, cosA, sinW, cosW):
    x = np.linspace(start, stop, num_points)
    y = sinA * np.sin(sinW * x) + cosA * np.cos(cosW * x)
    return x, y

