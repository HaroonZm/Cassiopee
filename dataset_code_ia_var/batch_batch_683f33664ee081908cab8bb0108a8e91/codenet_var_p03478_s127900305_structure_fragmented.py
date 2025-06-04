def read_input():
    return input()

def parse_input_line(line):
    return map(int, line.split())

def initialize_list():
    return []

def get_range(n):
    return range(1, n+1)

def int_to_str(i):
    return str(i)

def str_to_digits_list(s):
    return list(s)

def convert_char_to_int(c):
    return int(c)

def sum_of_digits(digits):
    total = 0
    for digit in digits:
        total += convert_char_to_int(digit)
    return total

def is_in_range(value, a, b):
    return a <= value <= b

def append_to_list(l, value):
    l.append(value)

def compute_sum(l):
    return sum(l)

def print_result(result):
    print(result)

def process_number(i, a, b):
    s = int_to_str(i)
    digits = str_to_digits_list(s)
    digit_sum = sum_of_digits(digits)
    return is_in_range(digit_sum, a, b)

def build_list(n, a, b):
    l = initialize_list()
    for i in get_range(n):
        if process_number(i, a, b):
            append_to_list(l, i)
    return l

def main():
    input_line = read_input()
    n, a, b = parse_input_line(input_line)
    l = build_list(n, a, b)
    total = compute_sum(l)
    print_result(total)

main()