from numpy import *
def parse_input():
    return map(int, input().split())

def get_l(n):
    return n * 3 + 1

def create_zeros(l, n):
    return zeros((l, n * 5), int64)

def set_init(d):
    d[0][0] = 1

def assign_indices(i):
    return i - 1, i - 2

def compute_first_term(d, i, k, j):
    return d[i - 3] * k * j

def compute_second_term(d, k, j):
    return roll(d[k], -1) * j

def compute_third_term(d, j):
    return roll(d[j], 1)

def compute_row(d, i, k, j, M):
    term1 = compute_first_term(d, i, k, j)
    term2 = compute_second_term(d, k, j)
    term3 = compute_third_term(d, j)
    return (term1 + term2 + term3) % M

def fill_matrix(d, l, M):
    for i in range(1, l):
        j, k = assign_indices(i)
        d[i] = compute_row(d, i, k, j, M)

def compute_result(d, l, M):
    return sum(d[-1][:l]) % M

def main():
    n, M = parse_input()
    l = get_l(n)
    d = create_zeros(l, n)
    set_init(d)
    fill_matrix(d, l, M)
    print(compute_result(d, l, M))

main()