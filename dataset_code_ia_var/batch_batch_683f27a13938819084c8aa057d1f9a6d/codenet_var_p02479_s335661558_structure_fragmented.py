import math

def read_input():
    return raw_input()

def parse_float(value):
    return float(value)

def compute_area(radius):
    return radius ** 2 * math.pi

def compute_circumference(radius):
    return 2 * radius * math.pi

def format_output(area, circumference):
    return "%.6f %.6f" % (area, circumference)

def print_result(result):
    print result

def main():
    raw_radius = read_input()
    radius = parse_float(raw_radius)
    area = compute_area(radius)
    circumference = compute_circumference(radius)
    result = format_output(area, circumference)
    print_result(result)

main()