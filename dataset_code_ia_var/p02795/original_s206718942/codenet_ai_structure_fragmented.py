def read_int():
    return int(input())

def get_height():
    return read_int()

def get_width():
    return read_int()

def get_n():
    return read_int()

def get_max_value(a, b):
    return max(a, b)

def compute_division(dividend, divisor):
    return dividend / divisor

def apply_ceiling(value):
    import math
    return math.ceil(value)

def print_result(result):
    print(result)

def process():
    h = get_height()
    w = get_width()
    n = get_n()
    m = get_max_value(h, w)
    div = compute_division(n, m)
    res = apply_ceiling(div)
    print_result(res)

process()