import math
import sys

def get_input():
    return raw_input()

def convert_to_float(value):
    return float(value)

def calculate_area(radius):
    return radius ** 2 * math.pi

def calculate_circumference(radius):
    return 2 * radius * math.pi

def format_number(number):
    return '%.5f' % number

def convert_to_str(value):
    return str(value)

def create_output(area_str, circumference_str):
    return area_str + " " + circumference_str

def print_output(output):
    print(output)

def terminate():
    sys.exit()

def main():
    input_value = get_input()
    radius = convert_to_float(input_value)
    area = calculate_area(radius)
    circumference = calculate_circumference(radius)
    area_formatted = format_number(area)
    circumference_formatted = format_number(circumference)
    area_str = convert_to_str(area_formatted)
    circumference_str = convert_to_str(circumference_formatted)
    output = create_output(area_str, circumference_str)
    print_output(output)
    terminate()

main()