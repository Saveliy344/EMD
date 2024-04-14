import numpy as np
from display import chart_save

def generate_default_signal(start, stop, num_points, sinA, cosA, sinW, cosW):
    x = np.linspace(start, stop, num_points)
    y = sinA*np.sin(sinW*x) + cosA * np.cos(cosW*x)
    chart_save.save_to_file(x, y, f"y = {sinA}*sin({sinW}*x) + {cosA}*cos({cosW}*x)", "signal_plot.png")
