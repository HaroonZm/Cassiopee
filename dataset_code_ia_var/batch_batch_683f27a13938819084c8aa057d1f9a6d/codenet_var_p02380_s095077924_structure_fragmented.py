import math

def read_input():
    return input()

def split_input(s):
    return s.split()

def str_to_float_list(lst):
    return list(map(float, lst))

def get_a(values):
    return values[0]

def get_b(values):
    return values[1]

def get_C(values):
    return values[2]

def deg_to_rad(deg):
    return math.pi * deg / 180

def compute_area(a, b, C_rad):
    return math.sin(C_rad) * a * b / 2

def compute_third_side(a, b, C_rad):
    return math.sqrt(a**2 + b**2 - 2*a*b*math.cos(C_rad))

def compute_perimeter(a, b, third_side):
    return a + b + third_side

def compute_height(b, C_rad):
    return b * math.sin(C_rad)

def format_float(val):
    return "{0:.8f}".format(val)

def print_formatted(value):
    print(value)

def main():
    s = read_input()
    splitted = split_input(s)
    numbers = str_to_float_list(splitted)
    a = get_a(numbers)
    b = get_b(numbers)
    C = get_C(numbers)
    C_rad = deg_to_rad(C)
    area = compute_area(a, b, C_rad)
    third_side = compute_third_side(a, b, C_rad)
    perimeter = compute_perimeter(a, b, third_side)
    height = compute_height(b, C_rad)
    area_fmt = format_float(area)
    perimeter_fmt = format_float(perimeter)
    height_fmt = format_float(height)
    print_formatted(area_fmt)
    print_formatted(perimeter_fmt)
    print_formatted(height_fmt)

main()