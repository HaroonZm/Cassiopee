import math
import sys

def get_input():
    return sys.stdin.readline().rstrip()

def parse_input(input_line):
    return list(map(float, input_line.split()))

def to_radians(degrees):
    return math.radians(degrees)

def calculate_triangle_area(a, b, C_rad):
    return a * b * math.sin(C_rad) / 2

def calculate_side_length(a, b, C_rad):
    return math.sqrt(a**2 + b**2 - 2*a*b*math.cos(C_rad))

def calculate_perimeter(a, b, length):
    return a + b + length

def calculate_height(b, C_rad):
    return b * math.sin(C_rad)

def print_value(value):
    print(value)

def main():
    input_line = get_input()
    a_val, b_val, C_deg = parse_input(input_line)
    C_rad = to_radians(C_deg)
    triangle_area = calculate_triangle_area(a_val, b_val, C_rad)
    third_side_length = calculate_side_length(a_val, b_val, C_rad)
    perimeter = calculate_perimeter(a_val, b_val, third_side_length)
    height = calculate_height(b_val, C_rad)
    print_value(triangle_area)
    print_value(perimeter)
    print_value(height)

main()