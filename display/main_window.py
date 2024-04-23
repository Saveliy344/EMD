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

    @staticmethod
    def choose_file():
        filename = filedialog.askopenfilename(title="Choose a file",
                                              filetypes=(("Text files", "*.txt"), ("All files", "*.*")))

        print("Selected file:", filename)
        if filename:
            data = np.loadtxt(filename)
            SignalPlotter.x = data[:, 0]
            SignalPlotter.y = data[:, 1]

    @staticmethod
    def next_step(image_path, canvas):
        try:
            if not SignalPlotter.initialized:
                return
            SignalPlotter.step += 1
            x, y = SignalPlotter.x, SignalPlotter.y
            x, y = get_medium(*interpolation(*get_maximum(x, y)), *interpolation(*get_minimum(x, y)))
            chart_save.save_to_file(x, y, f"Step #{SignalPlotter.step}", image_path)
            canvas.delete("all")
            img = Image.open(image_path)
            canvas_width = canvas.winfo_width()
            canvas_height = canvas.winfo_height()
            img = img.resize((canvas_width, canvas_height), Image.Resampling.LANCZOS)
            tk_img = ImageTk.PhotoImage(img)
            canvas.create_image(0, 0, anchor=tk.NW, image=tk_img)
            canvas.image = tk_img
            SignalPlotter.x, SignalPlotter.y = x, y
        except Exception:
            pass

    @staticmethod
    def plot_signal(image_path, canvas):
        try:
            SignalPlotter.initialized = True
            SignalPlotter.step = 0
            chart_save.save_to_file(SignalPlotter.x, SignalPlotter.y, f"Function", image_path)
            img = Image.open(image_path)
            canvas_width = canvas.winfo_width()
            canvas_height = canvas.winfo_height()
            img = img.resize((canvas_width, canvas_height), Image.Resampling.LANCZOS)
            tk_img = ImageTk.PhotoImage(img)
            canvas.create_image(0, 0, anchor=tk.NW, image=tk_img)
            canvas.image = tk_img
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

    btn_plot = tk.Button(root, text="Plot Signal", command=lambda: SignalPlotter.plot_signal(
        "signal_plot.png",
        canvas,
    ))
    btn_next_step = tk.Button(root, text="Next Step", command=lambda: SignalPlotter.next_step(
        "signal_plot.png",
    canvas))
    btn_choose_file.grid(row=0, columnspan=2)
    btn_next_step.grid(row=9, columnspan=2)
    btn_plot.grid(row=7, columnspan=2)

    root.rowconfigure(8, weight=1)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    root.mainloop()


if __name__ == "__main__":
    main()
