from display import chart_save
from emd_algorithm.checks import check_stop_algorithm, check_stop_one_iteration
from emd_algorithm.extremum_localization import get_maximum, get_minimum, get_maximum_to_inter, get_minimum_to_inter
from emd_algorithm.interpolation import interpolation, get_medium, get_diff

import tkinter as tk
from tkinter import messagebox, filedialog
import numpy as np
from PIL import Image, ImageTk

from emd_algorithm.modes_functions import get_amplitude, check_orthogonality


class SignalPlotter:
    mods = []
    initialized = False
    x, y = 0, 0
    step = 0
    prev_y = None

    image_path = "signal_plot.png"
    mods_image_path = "mods.png"

    is_finished = False

    initial_signal = None
    signal = None

    counter = 0

    modes_counter = 0

    eps = 0.1

    @staticmethod
    def choose_file():
        filename = filedialog.askopenfilename(title="Choose a file",
                                              filetypes=(("Text files", "*.txt"), ("All files", "*.*")))

        if filename:
            data = np.loadtxt(filename)
            SignalPlotter.prev_y = None
            SignalPlotter.x = data[:, 0]
            SignalPlotter.y = data[:, 1]
            SignalPlotter.modes_counter = 0
            # saving initial signal
            SignalPlotter.initial_signal = [SignalPlotter.x, SignalPlotter.y]
            SignalPlotter.signal = [SignalPlotter.x, SignalPlotter.y]
            SignalPlotter.step = 1
            SignalPlotter.initialized = True
            SignalPlotter.is_finished = False
            SignalPlotter.mods = []

    @staticmethod
    def add_image_to_canvas(canvas, path):
        img = Image.open(path)
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()
        img = img.resize((canvas_width, canvas_height), Image.Resampling.LANCZOS)
        tk_img = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor=tk.NW, image=tk_img)
        canvas.image = tk_img

    @staticmethod
    def plot_signal(canvas):
        try:
            if SignalPlotter.is_finished:
                if check_orthogonality(SignalPlotter.mods):
                    messagebox.showinfo("Finished", "Mods are orthogonal")
                else:
                    messagebox.showinfo("Finished", "Mods are not orthogonal")

                return
            if not SignalPlotter.initialized:
                messagebox.showerror("Error", "Choose file!")
                return

            # Showing current step and extremums
            chart_save.plot_init(f"Step {SignalPlotter.step}")
            chart_save.plot_chart(SignalPlotter.x, SignalPlotter.y, "blue", "Chart")
            x_max, y_max = get_maximum(SignalPlotter.x, SignalPlotter.y)
            x_min, y_min = get_minimum(SignalPlotter.x, SignalPlotter.y)
            chart_save.plot_points(x_max, y_max, "red", "max_points")
            chart_save.plot_points(x_min, y_min, "green", "min_points")
            x_max_to_inter, y_max_to_inter = get_maximum_to_inter(SignalPlotter.x, SignalPlotter.y)
            x_min_to_inter, y_min_to_inter = get_minimum_to_inter(SignalPlotter.x, SignalPlotter.y)
            max_interpolation = interpolation(SignalPlotter.x, x_max_to_inter, y_max_to_inter)
            min_interpolation = interpolation(SignalPlotter.x, x_min_to_inter, y_min_to_inter)
            medium = get_medium(*min_interpolation, *max_interpolation)
            chart_save.plot_chart(*max_interpolation, "orange", "max_interpolation",
                                  dashed=False)
            chart_save.plot_chart(*min_interpolation, "pink", "min_interpolation",
                                  dashed=False)
            chart_save.plot_chart(*medium, "black", "medium", dashed=True)
            chart_save.plot_save(SignalPlotter.image_path)
            SignalPlotter.add_image_to_canvas(canvas, SignalPlotter.image_path)
            SignalPlotter.y_prev = SignalPlotter.y
            SignalPlotter.y = get_diff(SignalPlotter.y, medium[1])
            SignalPlotter.counter += 1
            if SignalPlotter.counter > 1 and check_stop_one_iteration(SignalPlotter.y, SignalPlotter.y_prev):
                SignalPlotter.counter = 0
                SignalPlotter.step += 1
                SignalPlotter.mods.append((SignalPlotter.x, SignalPlotter.y))
                # remain
                r = get_diff(SignalPlotter.signal[1], SignalPlotter.y)
                SignalPlotter.signal[1] = r
                SignalPlotter.y = r
                if check_stop_algorithm(SignalPlotter.y, SignalPlotter.eps, SignalPlotter.initial_signal[1]):
                    SignalPlotter.is_finished = True
                    # Showing result
                    chart_save.plot_init("Mods", show_axis=False)

                    amplitude = get_amplitude(SignalPlotter.initial_signal[1])
                    check_orthogonality(SignalPlotter.mods)
                    for i in range(len(SignalPlotter.mods)):
                        chart_save.plot_chart(SignalPlotter.mods[i][0], SignalPlotter.mods[i][1] - amplitude * i, "blue", "")
                    chart_save.plot_save(SignalPlotter.mods_image_path)
                    SignalPlotter.add_image_to_canvas(canvas, SignalPlotter.mods_image_path)
                    # Getting sum of mods
                    y_sum = np.zeros_like(SignalPlotter.mods[0][1])
                    # Saving mods and signal to files
                    for index in range(len(SignalPlotter.mods)):
                        chart_save.plot_init(f"Mode #{index + 1}")
                        chart_save.plot_chart(SignalPlotter.mods[index][0], SignalPlotter.mods[index][1], "blue", "")
                        chart_save.plot_save(f"Mode #{index + 1}.png")
                        chart_save.save_data_to_file(SignalPlotter.mods[index][0], SignalPlotter.mods[index][1], f"Mode #{index + 1}.txt")
                        y_sum += SignalPlotter.mods[index][1]
                    chart_save.plot_init("Input signal")
                    chart_save.plot_chart(SignalPlotter.initial_signal[0], SignalPlotter.initial_signal[1],
                                          "black", "Input signal")
                    chart_save.plot_chart(SignalPlotter.initial_signal[0], y_sum, "red", "Sum of mods")
                    chart_save.plot_save(SignalPlotter.image_path, show_legend=True)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred {str(e)}")


def main():
    root = tk.Tk()
    root.title("Signal Generator")
    root.attributes("-zoomed", True)
    root.resizable(width=False, height=False)

    canvas = tk.Canvas(root, width=400, height=300)
    canvas.grid(row=8, columnspan=2, sticky="nsew")

    btn_choose_file = tk.Button(root, text="Choose File", command=SignalPlotter.choose_file)
    btn_plot = tk.Button(root, text="Make step", command=lambda: SignalPlotter.plot_signal(
        canvas
    ))

    btn_close = tk.Button(root, text="Close", command=root.destroy)

    btn_choose_file.grid(row=0, columnspan=2)
    btn_plot.grid(row=7, columnspan=2)
    btn_close.grid(row=9, columnspan=2)

    root.rowconfigure(8, weight=1)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    root.mainloop()


if __name__ == "__main__":
    main()
