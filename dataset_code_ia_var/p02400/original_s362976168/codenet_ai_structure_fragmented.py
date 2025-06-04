def get_input():
    return input()

def convert_to_float(value):
    return float(value)

def get_pi():
    return 3.1415926535897

def calculate_area(radius, pi):
    return pi * radius * radius

def calculate_circumference(radius, pi):
    return pi * radius * 2

def format_output(area, circumference):
    return '{} {}'.format(area, circumference)

def print_result(result):
    print(result)

def main():
    input_value = get_input()
    radius = convert_to_float(input_value)
    pi_value = get_pi()
    area = calculate_area(radius, pi_value)
    circumference = calculate_circumference(radius, pi_value)
    output = format_output(area, circumference)
    print_result(output)

main()