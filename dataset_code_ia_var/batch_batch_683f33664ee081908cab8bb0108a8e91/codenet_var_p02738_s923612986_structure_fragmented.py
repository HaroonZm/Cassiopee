from numpy import zeros, roll

def read_input():
    return map(int, input().split())

def compute_l(n):
    return n * 3 + 1

def allocate_d(l, n):
    return zeros((l, n * 5), dtype='int64')

def initialize_d(d):
    d[0][0] = 1

def get_indices(i):
    return i - 1, i - 2

def mult_prev_val(d, i, k, j):
    if i < 3:
        return 0
    return d[i - 3] * k * j

def shift_and_mult(d, k, j):
    if k < 0:
        return 0
    return roll(d[k], -1) * j

def shift_right(d, j):
    if j < 0:
        return 0
    return roll(d[j], 1)

def sum_modulo(arr, l, M):
    return arr[-1][:l].sum() % M

def main_loop(n, M, l, d):
    for i in range(1, l):
        j, k = get_indices(i)
        part1 = mult_prev_val(d, i, k, j)
        part2 = shift_and_mult(d, k, j)
        part3 = shift_right(d, j)
        d[i] = (part1 + part2 + part3) % M

def main():
    n, M = read_input()
    l = compute_l(n)
    d = allocate_d(l, n)
    initialize_d(d)
    main_loop(n, M, l, d)
    result = sum_modulo(d, l, M)
    print(result)

main()