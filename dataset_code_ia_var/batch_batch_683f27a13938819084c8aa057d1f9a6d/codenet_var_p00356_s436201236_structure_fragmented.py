import math

def read_input():
    return input()

def parse_input(s):
    return list(map(int, s.split()))

def get_x(parsed):
    return parsed[0]

def get_y(parsed):
    return parsed[1]

def compute_gcd(a, b):
    return math.gcd(a, b)

def compute_sum(a, b):
    return a + b

def compute_result(a, b, gc):
    s = compute_sum(a, b)
    temp = s - gc
    result = temp + 1
    return result

def print_result(res):
    print(res)

def main():
    s = read_input()
    parsed = parse_input(s)
    x = get_x(parsed)
    y = get_y(parsed)
    gc = compute_gcd(x, y)
    result = compute_result(x, y, gc)
    print_result(result)

main()