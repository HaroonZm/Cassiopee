import math

def read_input():
    return raw_input()

def parse_input(line):
    return map(int, line.split())

def compute_pow(val, exp):
    return pow(val, exp)

def compute_half(val):
    return val / 2.0

def compute_sqrt(val):
    return math.sqrt(val)

def compute_ADC(l, x):
    half_sum = compute_half(l + x)
    square1 = compute_pow(half_sum, 2)
    half_l = compute_half(l)
    square2 = compute_pow(half_l, 2)
    diff = square1 - square2
    sqrt_val = compute_sqrt(diff)
    return sqrt_val * compute_half(l)

def compute_ABC(l, a):
    square_l = compute_pow(l,2)
    half_a = compute_half(a)
    square_a = compute_pow(half_a,2)
    diff = square_l - square_a
    sqrt_val = compute_sqrt(diff)
    return sqrt_val * compute_half(a)

def compute_total(ABC, ADC):
    return ABC + 2 * ADC

def main_loop():
    while True:
        try:
            line = read_input()
            a, l, x = parse_input(line)
            ADC = compute_ADC(l, x)
            ABC = compute_ABC(l, a)
            total = compute_total(ABC, ADC)
            print total
        except EOFError:
            break

main_loop()