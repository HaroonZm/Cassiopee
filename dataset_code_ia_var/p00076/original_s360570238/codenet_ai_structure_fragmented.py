from math import pi, cos, sin, atan2

def get_input():
    return int(input())

def should_break(n):
    return n == -1

def decrement(n):
    return n - 1

def initial_angle():
    return 0.0

def initial_x():
    return 1.0

def initial_y():
    return 0.0

def quarter_turn():
    return pi / 2

def step_angle(ang):
    return ang + quarter_turn()

def step_x(x, ang):
    return x + cos(ang)

def step_y(y, ang):
    return y + sin(ang)

def update_angle(y, x):
    return atan2(y, x)

def format_output(value):
    return "{:.2f}".format(value)

def print_result(x, y):
    print(format_output(x))
    print(format_output(y))

def iterate_steps(n, ang, x, y):
    def step(i, ang, x, y):
        ang = step_angle(ang)
        x = step_x(x, ang)
        y = step_y(y, ang)
        ang = update_angle(y, x)
        return ang, x, y
    for i in range(n):
        ang, x, y = step(i, ang, x, y)
    return x, y

def process_one_input(n):
    n = decrement(n)
    ang = initial_angle()
    x = initial_x()
    y = initial_y()
    x, y = iterate_steps(n, ang, x, y)
    print_result(x, y)

def main_loop():
    while True:
        n = get_input()
        if should_break(n):
            break
        process_one_input(n)

def main():
    main_loop()

main()