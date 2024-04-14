import matplotlib.pyplot as plt
def save_to_file(x, y, name, file_name):
    plt.plot(x, y)
    plt.title(name)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.savefig(file_name)