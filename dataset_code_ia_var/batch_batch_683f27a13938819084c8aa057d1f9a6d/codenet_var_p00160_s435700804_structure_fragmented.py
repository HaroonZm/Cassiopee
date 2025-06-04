def read_int():
    return int(input())

def read_coords():
    return map(int, input().split())

def input_n_and_init_v():
    n = read_int()
    v = 0
    return n, v

def break_if_zero(n):
    return n == 0

def adjust_x(x, y, h):
    return x + y + h

def get_points(x, w):
    if x < 61 and w < 3:
        return 600
    elif x < 81 and w < 6:
        return 800
    elif x < 101 and w < 11:
        return 1000
    elif x < 121 and w < 16:
        return 1200
    elif x < 141 and w < 21:
        return 1400
    elif x < 161 and w < 26:
        return 1600
    return 0

def process_one_case():
    n, v = input_n_and_init_v()
    if break_if_zero(n):
        return None
    for _ in range(n):
        result = process_one_line()
        v += result
    print_v(v)
    return True

def process_one_line():
    x, y, h, w = read_coords()
    x = adjust_x(x, y, h)
    return get_points(x, w)

def print_v(v):
    print(v)

def main_loop():
    while True:
        result = process_one_case()
        if result is None:
            break

main_loop()