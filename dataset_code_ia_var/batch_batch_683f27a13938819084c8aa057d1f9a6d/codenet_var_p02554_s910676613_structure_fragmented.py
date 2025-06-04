def read_input():
    return int(input())

def get_mod():
    return 10 ** 9 + 7

def compute_power(base, exp):
    return pow(base, exp)

def compute_part1(n):
    return compute_power(10, n)

def compute_part2(n):
    return compute_power(8, n)

def compute_part3(n):
    return 2 * compute_power(9, n)

def apply_mod(value, mod):
    return value % mod

def prepare_parts(n, mod):
    p1 = apply_mod(compute_part1(n), mod)
    p2 = apply_mod(compute_part2(n), mod)
    p3 = apply_mod(compute_part3(n), mod)
    return p1, p2, p3

def compute_result(part1, part2, part3, mod):
    return (part1 + part2 - part3) % mod

def main():
    n = read_input()
    mod = get_mod()
    part1, part2, part3 = prepare_parts(n, mod)
    result = compute_result(part1, part2, part3, mod)
    print(result)

main()