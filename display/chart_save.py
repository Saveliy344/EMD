import matplotlib.pyplot as plt


def plot_init(name):
    plt.clf()
    plt.title(name)
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')


def plot_chart(x, y, label, step_number):
    plt.plot(x, y, label=f"{label} on step #{step_number}")


def plot_points(x, y, color, label, step_number):
    plt.scatter(x, y, color=color, label=f"{label} on step #{step_number}")


def plot_save(file_name):
    plt.legend()
    plt.savefig(file_name)
