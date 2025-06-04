def read_integer():
    return int(input())

def create_zero_list(size):
    return [0] * size

def read_triplet():
    return map(int, input().split())

def fill_input_data(n, t, x, y):
    def assign_triplet(i):
        ti, xi, yi = read_triplet()
        t[i] = ti
        x[i] = xi
        y[i] = yi
    for i in range(1, n+1):
        assign_triplet(i)

def absolute_difference(a, b):
    return abs(a - b)

def manhattan_distance(x0, y0, x1, y1):
    return absolute_difference(x1, x0) + absolute_difference(y1, y0)

def compute_tmp(t0, t1, x0, y0, x1, y1):
    return absolute_difference(t1, t0) - manhattan_distance(x0, y0, x1, y1)

def is_invalid(tmp):
    return tmp < 0 or tmp % 2 != 0

def process_steps(n, t, x, y):
    for i in range(n):
        tmp = compute_tmp(t[i], t[i+1], x[i], y[i], x[i+1], y[i+1])
        if is_invalid(tmp):
            print_no_and_exit()
    print_yes()

def print_no_and_exit():
    print('No')
    quit()

def print_yes():
    print('Yes')

def main():
    n = read_integer()
    t = create_zero_list(n+1)
    x = create_zero_list(n+1)
    y = create_zero_list(n+1)
    fill_input_data(n, t, x, y)
    process_steps(n, t, x, y)

main()