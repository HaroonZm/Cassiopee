def read_input():
    return input()

def to_int(value):
    return int(value)

def divide_by_three(value):
    return value / 3

def power(value, exponent):
    return value ** exponent

def format_result(value):
    return value

def output_result(value):
    print(value)

def main():
    raw_input = read_input()
    number = to_int(raw_input)
    divided = divide_by_three(number)
    cubed = power(divided, 3)
    result = format_result(cubed)
    output_result(result)

main()