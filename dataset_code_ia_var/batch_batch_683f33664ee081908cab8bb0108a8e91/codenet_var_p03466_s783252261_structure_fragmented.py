import sys
import numpy as np
import numba
from numba import njit, i8

read = sys.stdin.buffer.read

@njit((i8, i8), cache=True)
def swap_if_needed(a, b):
    if a < b:
        return b, a
    return a, b

@njit((i8, i8), cache=True)
def compute_min_length(a, b):
    a, b = swap_if_needed(a, b)
    return (a + b) // (b + 1)

@njit((i8, i8, i8), cache=True)
def is_valid_count(a, b, L):
    ok = (a >= 0 and b >= 0)
    if a == 0:
        ok = ok and (b <= L - 1)
    else:
        ok = ok and (a <= L * (b + 1))
        ok = ok and (1 + b <= L * (a + 1))
    return ok

def handle_add_vars(vals, new_c, new_d):
    vals[0] = new_c
    vals[1] = new_d

def get_m_and_update(vals, x, y):
    c = vals[0]
    m = (c - 1) // (x + y)
    vals[0] -= m * (x + y)
    vals[1] -= m * (x + y)
    return m

def process_while(vals, s, x, t, y, n, ret):
    c = vals[0]
    d = vals[1]
    while n and c <= d:
        if d <= x:
            ret.append(s * (d - c + 1))
            vals[1] = 0
            return
        if 1 <= c <= x:
            ret.append(s * (x - c + 1))
            vals[0] = x + 1
        ret.append(t * (min(d, x + y) - vals[0] + 1))
        vals[0] = 1
        vals[1] -= x + y
        n -= 1

def add_chars(s, x, t, y, n, vals, ret):
    if (x + y) * n < vals[0]:
        vals[0] -= (x + y) * n
        vals[1] -= (x + y) * n
        return
    m = get_m_and_update(vals, x, y)
    n -= m
    process_while(vals, s, x, t, y, n, ret)

def binary_search_for_n(a, b, L):
    l, r = 0, b + 100
    while l + 1 < r:
        m = (l + r) >> 1
        a1, b1 = a - L * m, b - m
        if is_valid_count(a1, b1, L):
            l = m
        else:
            r = m
    return l

def binary_search_for_k(a, b, L):
    l, r = 0, L
    while l + 1 < r:
        m = (l + r) // 2
        if is_valid_count(a - m, b - 1, L):
            l = m
        else:
            r = m
    return l

def binary_search_for_kB(a, b, L, flag):
    l, r = -1, L - 1
    if flag:
        r = L
    while l + 1 < r:
        m = (l + r) // 2
        if is_valid_count(a, b - m, L) and b - m <= a * L:
            r = m
        else:
            l = m
    return r

def build_result_sequence(a, b, c, d, L):
    ret = []
    vals = [c, d]
    n = binary_search_for_n(a, b, L)
    flag = (n == 0)
    add_chars('A', L, 'B', 1, n, vals, ret)
    a -= L * n
    b -= n
    k = binary_search_for_k(a, b, L)
    flag = flag and (k == 0)
    if k:
        add_chars('A', k, 'B', 1, 1, vals, ret)
        a -= k
        b -= 1
    if a == 0:
        add_chars('B', b, 'A', 0, 1, vals, ret)
        return ''.join(ret)
    if b == 0:
        add_chars('A', a, 'B', 0, 1, vals, ret)
        return ''.join(ret)
    kB = binary_search_for_kB(a, b, L, flag)
    if kB >= 0:
        add_chars('B', kB, 'A', 1, 1, vals, ret)
        a -= 1
        b -= kB
    nB = min(b // L, a)
    add_chars('B', L, 'A', 1, nB, vals, ret)
    a -= nB
    b -= nB * L
    add_chars('B', b, 'A', 0, 1, vals, ret)
    add_chars('B', 0, 'A', a, 1, vals, ret)
    return ''.join(ret)

@njit((i8, i8, i8, i8), cache=True)
def find_min_length(a, b, c, d):
    return compute_min_length(a, b)

def f(a, b, c, d):
    L = compute_min_length(a, b)
    return build_result_sequence(a, b, c, d, L)

def parse_input():
    ABCD = np.array(read().split(), np.int64)[1:]
    return ABCD.reshape(-1, 4)

def main():
    abcd_chunks = parse_input()
    for a, b, c, d in abcd_chunks:
        print(f(a, b, c, d))

if __name__ == '__main__':
    main()