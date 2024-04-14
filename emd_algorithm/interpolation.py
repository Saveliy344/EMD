import numpy as np
from scipy.interpolate import CubicSpline

from display import chart_save


def interpolation(x, y, start, stop, num_points):
    cs = CubicSpline(x, y)
    new_x = np.linspace(start, stop, num_points)
    new_y = cs(new_x)
    chart_save.save_to_file(new_x, new_y, f"экстримум", "extrimum.png")
    return new_x, new_y