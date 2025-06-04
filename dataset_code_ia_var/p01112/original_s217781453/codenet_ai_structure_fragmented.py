import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import copy
import functools
import time
import random
import resource

def set_sys_recursionlimit():
    sys.setrecursionlimit(10**7)

def get_constants():
    inf = 10**20
    eps = 1.0 / 10**10
    mod = 10**9 + 7
    mod2 = 998244353
    dd = [(-1,0), (0,1), (1,0), (0,-1)]
    ddn = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
    return inf, eps, mod, mod2, dd, ddn

def input_integer_list():
    return list(map(int, sys.stdin.readline().split()))

def input_integer_list_zero_based():
    return [int(x)-1 for x in sys.stdin.readline().split()]

def input_integer():
    return int(sys.stdin.readline())

def read_test_case_n():
    return input_integer()

def read_test_case_m():
    return input_integer()

def read_test_case_edges(m):
    return [input_integer_list_zero_based() for _ in range(m)]

def create_matrix(n):
    return [[0]*n for _ in range(n)]

def create_wl(n):
    return [[0]*2 for _ in range(n)]

def fill_matrices(n, edges, aa, wl):
    for x, y in edges:
        aa[x][y] = aa[y][x] = 1
        wl[x][0] += 1
        wl[y][1] += 1

def get_half_n(n):
    return n // 2

def append_zero_if_invalid(wl, n, rr):
    nn = get_half_n(n)
    for i in range(n):
        if wl[i][0] > nn or wl[i][1] > nn:
            rr.append(0)
            return True
    return False

def get_missing_edges(n, aa):
    kh = []
    for x in range(n):
        for y in range(x+1, n):
            if aa[x][y] == 0:
                kh.append((x, y))
    return kh

def get_ks(kh):
    return len(kh)

def count_ff(wl, i, ks, kh, nn):
    def increase_wl(wl, x, y, idx1, idx2):
        wl[x][idx1] += 1
        wl[y][idx2] += 1

    def decrease_wl(wl, x, y, idx1, idx2):
        wl[x][idx1] -= 1
        wl[y][idx2] -= 1

    if i == ks:
        return 1
    r = 0
    x, y = kh[i]
    if wl[x][0] < nn and wl[y][1] < nn:
        increase_wl(wl, x, y, 0, 1)
        r += count_ff(wl, i+1, ks, kh, nn)
        decrease_wl(wl, x, y, 0, 1)
    if wl[x][1] < nn and wl[y][0] < nn:
        increase_wl(wl, x, y, 1, 0)
        r += count_ff(wl, i+1, ks, kh, nn)
        decrease_wl(wl, x, y, 1, 0)
    return r

def join_array(a, sep):
    return sep.join(map(str, a))

def process_one_case(rr):
    n = read_test_case_n()
    if n == 0:
        return False
    m = read_test_case_m()
    edges = read_test_case_edges(m)
    nn = get_half_n(n)
    aa = create_matrix(n)
    wl = create_wl(n)
    fill_matrices(n, edges, aa, wl)
    if append_zero_if_invalid(wl, n, rr):
        return True
    kh = get_missing_edges(n, aa)
    ks = get_ks(kh)
    res = count_ff(wl, 0, ks, kh, nn)
    rr.append(res)
    return True

def run_main_loop():
    rr = []
    while True:
        has_input = process_one_case(rr)
        if not has_input:
            break
    return rr

def main():
    set_sys_recursionlimit()
    run_constants = get_constants()
    rr = run_main_loop()
    output = join_array(rr, "\n")
    print(output)
    return output

main()