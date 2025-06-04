def read_dimensions():
    return map(int, input().split())

def read_point():
    return map(int, input().split())

def calculate_dx(px, x):
    return px - x

def calculate_dy(py, y):
    return py - y

def is_opposite_sign(dx, dy):
    return dx * dy < 0

def abs_value(val):
    return abs(val)

def abs_list(values):
    return list(map(abs_value, values))

def sum_of_abs_list(values):
    return sum(abs_list(values))

def max_of_abs_list(values):
    return max(abs_list(values))

def update_coordinates(px, py):
    return px, py

def process_step(x, y, px, py):
    dx = calculate_dx(px, x)
    dy = calculate_dy(py, y)
    if is_opposite_sign(dx, dy):
        return sum_of_abs_list([dx, dy])
    else:
        return max_of_abs_list([dx, dy])

def main():
    w, h, n = read_dimensions()
    x, y = read_point()
    a = 0
    def process_points(n, x, y, a):
        for _ in range(n-1):
            px, py = read_point()
            increment = process_step(x, y, px, py)
            a_local = a + increment
            x, y = update_coordinates(px, py)
            a = a_local
        return a
    a = process_points(n, x, y, a)
    print(a)

main()