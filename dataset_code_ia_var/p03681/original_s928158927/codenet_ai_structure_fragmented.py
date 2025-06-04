import sys

def read_input():
    line = sys.stdin.readline()
    return line

def parse_input(line):
    values = line.strip().split()
    return values

def convert_to_ints(values):
    return map(int, values)

def get_N_M():
    line = read_input()
    values = parse_input(line)
    N, M = convert_to_ints(values)
    return N, M

def calc_mod():
    return 10**9+7

def compute_permutation_range(n, x):
    return range(n, n-x, -1)

def compute_permutation_tmp(tmp, i, mod):
    return (tmp * i) % mod

def permutation(n, x, mod):
    tmp = 1
    rng = compute_permutation_range(n, x)
    for i in rng:
        tmp = compute_permutation_tmp(tmp, i, mod)
    return tmp

def abs_diff(a, b):
    return abs(a - b)

def check_abs_diff_gt_one(diff):
    return diff > 1

def check_abs_diff_eq_one(diff):
    return diff == 1

def handle_diff_gt_one():
    print(0)

def handle_diff_eq_one(N, M, mod):
    res = permutation(N, N, mod)
    res2 = permutation(M, M, mod)
    output = (res * res2) % mod
    print(output)

def handle_else_case(N, M, mod):
    res = permutation(N, N, mod)
    res2 = permutation(M, M, mod)
    output = (2 * res * res2) % mod
    print(output)

def main():
    N, M = get_N_M()
    mod = calc_mod()
    diff = abs_diff(N, M)
    if check_abs_diff_gt_one(diff):
        handle_diff_gt_one()
    elif check_abs_diff_eq_one(diff):
        handle_diff_eq_one(N, M, mod)
    else:
        handle_else_case(N, M, mod)

main()