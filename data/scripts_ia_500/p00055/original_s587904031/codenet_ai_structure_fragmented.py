import sys

def read_lines():
    return sys.stdin

def process_line(line):
    a = convert_to_float(line)
    s = calculate_sum(a)
    return s

def convert_to_float(line):
    return float(line)

def calculate_sum(a_initial):
    s = 0
    a = a_initial
    for i in range(10):
        s = accumulate_sum(s, a)
        a = update_a(a, i)
    return s

def accumulate_sum(current_sum, value):
    return current_sum + value

def update_a(a, index):
    if is_even(index):
        return multiply_by_two(a)
    else:
        return divide_by_three(a)

def is_even(number):
    return number % 2 == 0

def multiply_by_two(value):
    return value * 2

def divide_by_three(value):
    return value / 3

def print_result(result):
    print(result)

def main():
    for line in read_lines():
        result = process_line(line)
        print_result(result)

main()