import math

def read_input():
    return input()

def split_input(input_str):
    return input_str.split()

def convert_to_int(str_list):
    return [int(x) for x in str_list]

def get_triangle_sides_and_angle():
    input_str = read_input()
    str_list = split_input(input_str)
    int_list = convert_to_int(str_list)
    return int_list

def to_radians(degrees):
    return math.radians(degrees)

def compute_sin(angle_rad):
    return math.sin(angle_rad)

def compute_cos(angle_rad):
    return math.cos(angle_rad)

def compute_side_b_sin_c(b, sin_c):
    return b * sin_c

def compute_area(a, b, sin_c):
    return a * b * sin_c / 2

def compute_sqrt(val):
    return math.sqrt(val)

def compute_side_l(a, b, sin_c, cos_c):
    part1 = (b * sin_c) ** 2
    part2 = (a - b * cos_c) ** 2
    return a + b + compute_sqrt(part1 + part2)

def compute_height(b, sin_c):
    return b * sin_c

def print_value(val):
    print(val)

def main():
    a, b, c = get_triangle_sides_and_angle()
    c_rad = to_radians(c)
    sin_c = compute_sin(c_rad)
    cos_c = compute_cos(c_rad)
    area = compute_area(a, b, sin_c)
    l = compute_side_l(a, b, sin_c, cos_c)
    h = compute_height(b, sin_c)
    print_value(area)
    print_value(l)
    print_value(h)

main()