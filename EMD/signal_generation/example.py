import numpy as np
from display import chart_save

def generate_default_signal(start, stop, num_points, sin, cos):
    x = np.linspace(start, stop, num_points)
    y = sin*np.sin(x) + cos * np.cos(x)
    chart_save.save_to_file(x, y, f"y = {sin}*sin(x) + {cos}*cos(x)", "signal_plot.png")

start = 0
stop = 10
num_points = 1000
sin = 2
cos = 3
generate_default_signal(start, stop, num_points, sin, cos)
