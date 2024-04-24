import matplotlib.pyplot as plt


def plot_init(name):
    plt.clf()
    plt.title(name)
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')


def plot_chart(x, y, color, label, dashed=False):
    line_style = '--' if dashed else '-'
    plt.plot(x, y, color=color, linestyle=line_style, label=label)


def plot_points(x, y, color, label):
    plt.scatter(x, y, color=color, label=label)


def plot_save(file_name):
    plt.legend()
    plt.savefig(file_name)
