M = 4294967311

def mod_add(a, b):
    return pmod(a + b)

def mod_sub(a, b):
    return pmod(a - b)

def mod_mul(a, b):
    return pmod(a * b)

def mod_div(a, b):
    inv_b = minv(b)
    return pmod(a * inv_b)

def is_positive_op(code):
    return code == 1

def is_negative_op(code):
    return code == 2

def is_multiply_op(code):
    return code == 3

def is_divide_op(code):
    return code == 4

def pmod(v):
    return ((v % M) + M) % M

def mpow_even(x):
    return pmod(x * x)

def mpow_mul(res, x):
    return pmod(res * x)

def divide_by_2(N):
    return N // 2

def is_odd(N):
    return N % 2 != 0

def mpow_core(x, N, res):
    while N > 0:
        if is_odd(N):
            res = mpow_mul(res, x)
        x = mpow_even(x)
        N = divide_by_2(N)
    return res

def mpow(x, N):
    return mpow_core(x, N, 1)

def minv(a):
    return mpow(a, M - 2)

def get_input():
    return int(input())

def get_raw_input():
    return input()

def split_input(line):
    return list(map(int, line.strip().split()))

def read_command():
    line = get_raw_input()
    return split_input(line)

def update_v_add(v, y):
    return mod_add(v, y)

def update_v_sub(v, y):
    return mod_sub(v, y)

def update_v_mul(v, y):
    return mod_mul(v, y)

def update_v_div(v, y):
    return mod_div(v, y)

def update_v(v, c, y):
    if is_positive_op(c):
        return update_v_add(v, y)
    elif is_negative_op(c):
        return update_v_sub(v, y)
    elif is_multiply_op(c):
        return update_v_mul(v, y)
    elif is_divide_op(c):
        return update_v_div(v, y)
    else:
        return v

def value_is_small(v):
    return v < (1 << 31)

def correct_v(v):
    if value_is_small(v):
        return v
    else:
        return v - M

def print_result(v):
    print("%d" % v)

def main():
    N = get_input()
    v = 0
    for _ in range(N):
        c, y = read_command()
        v = update_v(v, c, y)
    v = correct_v(v)
    print_result(v)

main()