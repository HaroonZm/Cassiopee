def get_input():
    return input()

def to_int(s):
    return int(s)

def get_modulo():
    return 1000000007

def compute_power(base, exponent):
    return base ** exponent

def subtract(a, b):
    return a - b

def add(a, b):
    return a + b

def modulo(a, mod):
    return a % mod

def print_result(result):
    print(result)

def calculate_expression(N):
    ten_power_n = compute_power(10, N)
    nine_power_n_1 = compute_power(9, N)
    nine_power_n_2 = compute_power(9, N)
    eight_power_n = compute_power(8, N)
    part1 = subtract(ten_power_n, nine_power_n_1)
    part2 = subtract(part1, nine_power_n_2)
    final = add(part2, eight_power_n)
    return final

def main():
    raw_n = get_input()
    N = to_int(raw_n)
    result = calculate_expression(N)
    mod = get_modulo()
    result_mod = modulo(result, mod)
    print_result(result_mod)

main()