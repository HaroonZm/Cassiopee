import math

def get_input():
    return input()

def convert_input(value):
    return float(value)

def compute_area(radius):
    return math.pi * pow(radius, 2)

def compute_circumference(radius):
    return 2 * math.pi * radius

def format_result(area, circumference):
    return "%f %f" % (area, circumference)

def print_result(result):
    print(result)

def main():
    r_raw = get_input()
    r = convert_input(r_raw)
    area = compute_area(r)
    circumference = compute_circumference(r)
    result = format_result(area, circumference)
    print_result(result)

main()