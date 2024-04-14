import tkinter as tk
from tkinter import messagebox
from signal_generation import example

import tkinter as tk
from tkinter import messagebox
import numpy as np

class SignalGenerator:
    @staticmethod
    def generate_default_signal(start, stop, num_points, sinA, cosA, sinW, cosW):
        x = np.linspace(start, stop, num_points)
        y = sinA * np.sin(sinW * x) + cosA * np.cos(cosW * x)
        return x, y

class SignalPlotter:
    @staticmethod
    def plot_signal(start, stop, num_points, sinA, cosA, sinW, cosW):
        try:
            example.generate_default_signal(start, stop, num_points, sinA, cosA, sinW, cosW)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def main():
    root = tk.Tk()
    root.title("Signal Generator")

    # Создание и размещение элементов управления
    tk.Label(root, text="Start:").grid(row=0, column=0)
    entry_start = tk.Entry(root)
    entry_start.grid(row=0, column=1)
    entry_start.insert(0, "0.0")

    tk.Label(root, text="Stop:").grid(row=1, column=0)
    entry_stop = tk.Entry(root)
    entry_stop.grid(row=1, column=1)
    entry_stop.insert(0, "10.0")

    tk.Label(root, text="Number of Points:").grid(row=2, column=0)
    entry_num_points = tk.Entry(root)
    entry_num_points.grid(row=2, column=1)
    entry_num_points.insert(0, "1000")

    tk.Label(root, text="Sin Amplitude:").grid(row=3, column=0)
    entry_sinA = tk.Entry(root)
    entry_sinA.grid(row=3, column=1)
    entry_sinA.insert(0, "1.0")

    tk.Label(root, text="Cos Amplitude:").grid(row=4, column=0)
    entry_cosA = tk.Entry(root)
    entry_cosA.grid(row=4, column=1)
    entry_cosA.insert(0, "2.0")

    tk.Label(root, text="Sin Frequency:").grid(row=5, column=0)
    entry_sinW = tk.Entry(root)
    entry_sinW.grid(row=5, column=1)
    entry_sinW.insert(0, "1.0")

    tk.Label(root, text="Cos Frequency:").grid(row=6, column=0)
    entry_cosW = tk.Entry(root)
    entry_cosW.grid(row=6, column=1)
    entry_cosW.insert(0, "2.0")



    btn_plot = tk.Button(root, text="Plot Signal", command=lambda: SignalPlotter.plot_signal(
        float(entry_start.get()),
        float(entry_stop.get()),
        int(entry_num_points.get()),
        float(entry_sinA.get()),
        float(entry_cosA.get()),
        float(entry_sinW.get()),
        float(entry_cosW.get())
    ))
    btn_plot.grid(row=7, columnspan=2)

    # Запуск основного цикла обработки событий
    root.mainloop()
