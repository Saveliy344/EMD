from display import chart_save
from emd_algorithm.extremum_localization import get_maximum, get_minimum
from emd_algorithm.interpolation import interpolation, get_medium
from signal_generation import example

import tkinter as tk
from tkinter import messagebox
import numpy as np
from PIL import Image, ImageTk


class SignalPlotter:
    initialized = False
    x, y = 0, 0
    step = 0
    @staticmethod
    def next_step(start, stop, num_points, canvas, image_path):
        try:
            if not SignalPlotter.initialized:
                return
            SignalPlotter.step += 1
            x, y = SignalPlotter.x, SignalPlotter.y
            x, y = get_medium(*interpolation(*get_maximum(x, y), start, stop, num_points), *interpolation(*get_minimum(x, y), start, stop, num_points))
            chart_save.save_to_file(x, y, f"Step #{SignalPlotter.step}", "signal_plot.png")
            canvas.delete("all")
            img = Image.open(image_path)
            canvas_width = canvas.winfo_width()
            canvas_height = canvas.winfo_height()
            img = img.resize((canvas_width, canvas_height), Image.Resampling.LANCZOS)
            tk_img = ImageTk.PhotoImage(img)
            canvas.create_image(0, 0, anchor=tk.NW, image=tk_img)
            canvas.image = tk_img
            SignalPlotter.x, SignalPlotter.y = x, y
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    @staticmethod
    def plot_signal(start, stop, num_points, sinA, cosA, sinW, cosW, canvas, image_path):
        try:
            SignalPlotter.initialized = True
            SignalPlotter.step = 0
            x, y = example.generate_default_signal(start, stop, num_points, sinA, cosA, sinW, cosW)
            chart_save.save_to_file(x, y, f"y = {sinA}*sin({sinW}*x) + {cosA}*cos({cosW}*x)", "signal_plot.png")
            img = Image.open(image_path)
            canvas_width = canvas.winfo_width()
            canvas_height = canvas.winfo_height()
            img = img.resize((canvas_width, canvas_height), Image.Resampling.LANCZOS)
            tk_img = ImageTk.PhotoImage(img)
            canvas.create_image(0, 0, anchor=tk.NW, image=tk_img)
            canvas.image = tk_img
            SignalPlotter.x = x
            SignalPlotter.y = y
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


def main():
    root = tk.Tk()
    root.title("Signal Generator")
    root.attributes("-zoomed", True)
    root.resizable(width=False, height=False)

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

    canvas = tk.Canvas(root, width=400, height=300)
    canvas.grid(row=8, columnspan=2, sticky="nsew")

    btn_plot = tk.Button(root, text="Plot Signal", command=lambda: SignalPlotter.plot_signal(
        float(entry_start.get()),
        float(entry_stop.get()),
        int(entry_num_points.get()),
        float(entry_sinA.get()),
        float(entry_cosA.get()),
        float(entry_sinW.get()),
        float(entry_cosW.get()),
        canvas,
        "signal_plot.png"
    ))
    btn_next_step = tk.Button(root, text="Next Step", command=lambda: SignalPlotter.next_step(
        float(entry_start.get()),
        float(entry_stop.get()),
        int(entry_num_points.get()),
        canvas,
        "signal_plot.png"))
    btn_next_step.grid(row=9, columnspan=2)
    btn_plot.grid(row=7, columnspan=2)

    root.rowconfigure(8, weight=1)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    root.mainloop()


if __name__ == "__main__":
    main()
