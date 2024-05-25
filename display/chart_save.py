import matplotlib.pyplot as plt


def plot_init(name, show_axis=True):
    plt.clf()
    plt.title(name)
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    if not show_axis:
        plt.gca().set_xticks([])
        plt.gca().set_yticks([])


def plot_chart(x, y, color, label, linewidth=1, dashed=False):
    line_style = '--' if dashed else '-'
    plt.plot(x, y, color=color, linestyle=line_style, label=label, linewidth=linewidth)


def plot_points(x, y, color, label, s=2):
    plt.scatter(x, y, color=color, label=label, s=s)


def plot_save(file_name, show_legend=False):
    if show_legend:
        plt.legend()
    plt.savefig(file_name)


def save_data_to_file(x, y, file_name):
    with open(file_name, 'w') as file:
        for i in range(len(x)):
            file.write(f"{x[i]} {y[i]}\n")
