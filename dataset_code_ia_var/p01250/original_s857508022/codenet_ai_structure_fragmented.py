from math import pi

def get_radius():
    return float(input())

def is_zero(value):
    return value == 0

def initialize_n():
    return 1

def initialize_d():
    return 1

def get_pi():
    return pi

def abs_diff(a, b):
    return abs(a - b)

def less_than(a, b):
    return a < b

def approx_fraction(target, tolerance):
    n = initialize_n()
    d = initialize_d()
    while not is_good_enough(n, d, target, tolerance):
        n, d = update_fraction(n, d, target)
    return n, d

def is_good_enough(n, d, target, tolerance):
    return abs_diff(n / d, target) <= tolerance

def update_fraction(n, d, target):
    if less_than(n / d, target):
        n = increment(n)
    else:
        d = increment(d)
    return n, d

def increment(x):
    return x + 1

def display_result(n, d):
    print(format_fraction(n, d))

def format_fraction(n, d):
    return '%d/%d' % (n, d)

def main_loop():
    while forever():
        r = get_radius()
        if is_zero(r): 
            break
        n, d = approx_fraction(get_pi(), r)
        display_result(n, d)

def forever():
    return True

main_loop()