# y - current ordinates
# y_input - input ordinates
def check_stop_algorithm(y, eps, y_input):
    if len(y_input) == 0:
        return True
    y_max = y_input[0]
    for y_ in y_input:
        if y_ > y_max:
            y_max = y_
    for y_ in y:
        if y_ >= eps * y_max:
            return False
    return True


def check_stop_one_iteration(y, y_prev):
    sum = 0
    try:
        for i in range(len(y)):
            sum += (y[i] - y_prev[i]) ** 2 / y_prev[i] ** 2
        return sum <= 10
    except Exception:
        return True
