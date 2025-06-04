def get_input():
    return input()

def convert_to_float(value):
    return float(value)

def cube(value):
    return value ** 3

def divide(value, divisor):
    return value / divisor

def format_output(value, decimals=10):
    format_str = '{:.' + str(decimals) + 'f}'
    return format_str.format(value)

def print_output(formatted_value):
    print(formatted_value)

def calculate_result(L):
    cubed = cube(L)
    divided = divide(cubed, 27.0)
    return divided

def main():
    raw_input = get_input()
    L = convert_to_float(raw_input)
    result = calculate_result(L)
    formatted_result = format_output(result, 10)
    print_output(formatted_result)

main()