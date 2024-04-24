from display import chart_save
from emd_algorithm.extremum_localization import get_maximum, get_minimum
from emd_algorithm.interpolation import interpolation, get_medium

import tkinter as tk
from tkinter import messagebox, filedialog
import numpy as np
from PIL import Image, ImageTk


class SignalPlotter:
    initialized = False
    x, y = 0, 0
    step = 0
    image_path = "signal_plot.png"

    @staticmethod
    def choose_file():
        filename = filedialog.askopenfilename(title="Choose a file",
                                              filetypes=(("Text files", "*.txt"), ("All files", "*.*")))

        if filename:
            data = np.loadtxt(filename)
            SignalPlotter.x = data[:, 0]
            SignalPlotter.y = data[:, 1]
            SignalPlotter.step = 0
            SignalPlotter.initialized = True

    @staticmethod
    def add_image_to_canvas(canvas):
        img = Image.open(SignalPlotter.image_path)
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()
        img = img.resize((canvas_width, canvas_height), Image.Resampling.LANCZOS)
        tk_img = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor=tk.NW, image=tk_img)
        canvas.image = tk_img

    @staticmethod
    def plot_signal(canvas):
        try:
            if not SignalPlotter.initialized:
                messagebox.showerror("Error", f"Choose file!")
                return
            SignalPlotter.step += 1
            # Showing current step and extremums
            chart_save.plot_init(f"Step {SignalPlotter.step}")
            chart_save.plot_chart(SignalPlotter.x, SignalPlotter.y, "Chart", SignalPlotter.step)
            x_max, y_max = get_maximum(SignalPlotter.x, SignalPlotter.y)
            x_min, y_min = get_minimum(SignalPlotter.x, SignalPlotter.y)
            chart_save.plot_points(x_max, y_max, "red", "max_points", SignalPlotter.step)
            chart_save.plot_points(x_min, y_min, "green", "min_points", SignalPlotter.step)
            max_interpolation = interpolation(x_max, y_max)
            min_interpolation = interpolation(x_min, y_min)
            chart_save.plot_save(SignalPlotter.image_path)
            SignalPlotter.add_image_to_canvas(canvas)


        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


def main():
    root = tk.Tk()
    root.title("Signal Generator")
    root.attributes("-zoomed", True)
    root.resizable(width=False, height=False)

    canvas = tk.Canvas(root, width=400, height=300)
    canvas.grid(row=8, columnspan=2, sticky="nsew")

    btn_choose_file = tk.Button(root, text="Choose File", command=SignalPlotter.choose_file)

    btn_plot = tk.Button(root, text="Make step", command=lambda: SignalPlotter.plot_signal(
        canvas,
    ))
    btn_choose_file.grid(row=0, columnspan=2)
    btn_plot.grid(row=7, columnspan=2)

    root.rowconfigure(8, weight=1)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    root.mainloop()


if __name__ == "__main__":
    main()
