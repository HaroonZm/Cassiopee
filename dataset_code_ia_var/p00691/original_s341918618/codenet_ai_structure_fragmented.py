def get_input():
    return input()

def str_to_int(s):
    return int(s)

def should_break(z):
    return z == 0

def calculate_zz(z):
    return z * z * z

def get_divisor():
    return 2

def get_exponent():
    return 1 / 3

def calc_double_a():
    return pow(get_divisor(), get_exponent())

def compute_upper_range(z):
    return int(z / calc_double_a()) + 1

def init_m():
    return 0

def iter_range(upper):
    return range(1, upper)

def cube(x):
    return x * x * x

def pow_a(val):
    return pow(val, get_exponent())

def int_pow(val):
    return int(pow_a(val))

def compute_y(zz, xx):
    return int_pow(zz - xx)

def update_m(m, yy, xx):
    return max(m, yy + xx)

def print_res(res):
    print(res)

def main_process():
    while True:
        z = str_to_int(get_input())
        if should_break(z):
            break
        zz = calculate_zz(z)
        m = init_m()
        upper = compute_upper_range(z)
        for x in iter_range(upper):
            xx = cube(x)
            y = compute_y(zz, xx)
            yy = cube(y)
            m = update_m(m, yy, xx)
        print_res(zz - m)

main_process()