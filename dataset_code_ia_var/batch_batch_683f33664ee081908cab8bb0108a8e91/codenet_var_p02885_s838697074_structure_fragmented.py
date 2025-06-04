def get_input():
    return input()

def parse_input(input_str):
    return map(int, input_str.split())

def get_a(parsed):
    return next(parsed)

def get_b(parsed):
    return next(parsed)

def compute_twice_b(b):
    return b * 2

def check_condition(a, double_b):
    return a <= double_b

def print_zero():
    print(0)

def compute_difference(a, double_b):
    return a - double_b

def print_result(result):
    print(result)

def main():
    input_str = get_input()
    parsed = parse_input(input_str)
    a = get_a(parsed)
    b = get_b(parsed)
    double_b = compute_twice_b(b)
    if check_condition(a, double_b):
        print_zero()
    else:
        diff = compute_difference(a, double_b)
        print_result(diff)

main()