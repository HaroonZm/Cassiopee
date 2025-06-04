import math

def read_input():
    return raw_input()

def parse_input(input_str):
    return map(int, input_str.strip().split())

def compute_s_value(a, b):
    return b + a / 2.0

def compute_sqrt_part(s, a, b):
    return s * (s - a) * (s - b) ** 2

def safe_sqrt(value):
    return math.sqrt(value)

def S(a, b):
    s = compute_s_value(a, b)
    value = compute_sqrt_part(s, a, b)
    return safe_sqrt(value)

def compute_lx_half(l, x):
    return (l + x) / 2.0

def compute_first_part(a, l):
    return S(a, l)

def compute_second_part(l, x):
    mid = compute_lx_half(l, x)
    return 2 * S(l, mid)

def compute_result(a, l, x):
    part1 = compute_first_part(a, l)
    part2 = compute_second_part(l, x)
    return part1 + part2

def print_result(res):
    print res

def main_loop():
    while True:
        try:
            inp = read_input()
            a, l, x = parse_input(inp)
            result = compute_result(a, l, x)
            print_result(result)
        except:
            break

main_loop()