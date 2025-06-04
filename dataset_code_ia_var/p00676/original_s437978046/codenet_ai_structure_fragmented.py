import math

def get_input_line():
    try:
        return raw_input()
    except EOFError:
        return None

def parse_input(line):
    return map(int, line.split())

def compute_first_term(a, l):
    val1 = pow(a / 2.0, 2)
    val2 = pow(l, 2)
    diff = val2 - val1
    sqrt_val = math.sqrt(diff)
    return sqrt_val * a / 2

def compute_second_term(l, x):
    val3 = pow(l / 2.0, 2)
    val4 = pow((l + x) / 2.0, 2)
    diff2 = val4 - val3
    sqrt_val2 = math.sqrt(diff2)
    return sqrt_val2 * l / 2 * 2

def compute_ans(a, l, x):
    first = compute_first_term(a, l)
    second = compute_second_term(l, x)
    return first + second

def print_ans(ans):
    print ans

def process_line(line):
    a, l, x = parse_input(line)
    ans = compute_ans(a, l, x)
    print_ans(ans)

def main_loop():
    while True:
        line = get_input_line()
        if line is None:
            break
        process_line(line)

main_loop()