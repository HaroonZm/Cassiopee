def read_input():
    return input()

def parse_input(raw_input):
    return map(int, raw_input.split())

def increment_value(value):
    return value + 1

def compute_gcd(a, b):
    from math import gcd
    return gcd(a, b)

def subtract_value(value1, value2):
    return value1 - value2

def perform_calculation(x, y):
    x_inc = increment_value(x)
    y_inc = increment_value(y)
    values_sum = x_inc + y_inc
    g = compute_gcd(x, y)
    temp = subtract_value(values_sum, g)
    result = subtract_value(temp, 1)
    return result

def print_result(result):
    print(result)

def main():
    raw_input = read_input()
    x, y = parse_input(raw_input)
    result = perform_calculation(x, y)
    print_result(result)

main()