def get_input_n():
    return int(input())

def get_input_a_b():
    return map(int, input().split())

def get_input_p():
    return list(map(int, input().split()))

def is_category_x(val, a):
    return val <= a

def is_category_y(val, a, b):
    return a < val <= b

def is_category_z(val, b):
    return val > b

def count_categories(n, a, b, p):
    x = count_x(n, a, p)
    y = count_y(n, a, b, p)
    z = count_z(n, b, p)
    return x, y, z

def count_x(n, a, p):
    return sum([increment_x(p[i], a) for i in range(n)])

def count_y(n, a, b, p):
    return sum([increment_y(p[i], a, b) for i in range(n)])

def count_z(n, b, p):
    return sum([increment_z(p[i], b) for i in range(n)])

def increment_x(val, a):
    if is_category_x(val, a):
        return 1
    return 0

def increment_y(val, a, b):
    if is_category_y(val, a, b):
        return 1
    return 0

def increment_z(val, b):
    if is_category_z(val, b):
        return 1
    return 0

def print_minimum(x, y, z):
    print(min(x, y, z))

def main():
    n = get_input_n()
    a, b = get_input_a_b()
    p = get_input_p()
    x, y, z = count_categories(n, a, b, p)
    print_minimum(x, y, z)

main()