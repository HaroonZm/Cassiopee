import sys

def read_lines():
    return sys.stdin.readlines()

def convert_to_float(line):
    return float(line)

def init_sum():
    return 0

def loop_range():
    return range(5)

def accumulate_sum(s, value):
    return s + value

def multiply_by_two(value):
    return value * 2

def divide_by_three(value):
    return value / 3

def process_line(line):
    i = convert_to_float(line)
    s = init_sum()
    for x in loop_range():
        s = accumulate_sum(s, i)
        i = multiply_by_two(i)
        s = accumulate_sum(s, i)
        i = divide_by_three(i)
    return s

def print_result(s):
    print(s)

def main():
    lines = read_lines()
    for line in lines:
        s = process_line(line)
        print_result(s)

main()