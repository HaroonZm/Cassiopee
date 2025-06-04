def read_input():
    return input()

def cube_number(n):
    return n ** 3

def is_zero(n):
    return n == 0

def loop_forever():
    while True:
        yield

def increment(i):
    return i + 1

def cube_root(n):
    return n ** (1/3.0)

def int_cube_root(n):
    return int(cube_root(n))

def inner_break_condition(j, i):
    return j < i

def update_mn(mn, m):
    if m < mn:
        return m
    return mn

def print_result(mn):
    print(mn)

def process_input(n):
    n3 = cube_number(n)
    mn = n3
    i = 0
    for _ in loop_forever():
        i = increment(i)
        i3 = cube_number(i)
        j = int_cube_root(n3 - i3)
        if inner_break_condition(j, i):
            break
        m = n3 - i3 - cube_number(j)
        mn = update_mn(mn, m)
    print_result(mn)

def main_loop():
    for _ in loop_forever():
        n = read_input()
        n = float(n)
        n = int(n)
        n3 = cube_number(n)
        if is_zero(n3):
            break
        process_input(n)

main_loop()