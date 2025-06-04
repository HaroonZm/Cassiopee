from math import sqrt

def get_input():
    return input()

def parse_input(line):
    return map(int, line.split())

def compute_first_term(l, x):
    return l * sqrt(x * (2 * l + x)) / 2

def compute_second_term(a, l):
    return a * sqrt(4 * l ** 2 - a ** 2) / 4

def compute_result(a, l, x):
    first = compute_first_term(l, x)
    second = compute_second_term(a, l)
    return first + second

def format_result(result):
    return "%.10f" % result

def print_result(formatted_result):
    print(formatted_result)

def process_line(line):
    a, l, x = parse_input(line)
    result = compute_result(a, l, x)
    formatted = format_result(result)
    print_result(formatted)

def main_loop():
    while True:
        try:
            line = get_input()
            process_line(line)
        except EOFError:
            break

def main():
    main_loop()

main()