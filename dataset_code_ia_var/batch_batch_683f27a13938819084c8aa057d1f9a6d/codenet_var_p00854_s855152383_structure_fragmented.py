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
import random
import time
import copy
import functools

def set_recursion_limit():
    sys.setrecursionlimit(10 ** 7)

def get_inf():
    return 10 ** 20

def get_eps():
    return 1.0 / 10 ** 10

def get_mod():
    return 998244353

def LI():
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def LF():
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    return sys.stdin.readline().split()

def I():
    return int(sys.stdin.readline())

def F():
    return float(sys.stdin.readline())

def S():
    return input()

def pf(s):
    return print(s, flush=True)

def read_n_k_m():
    return LI()

def is_termination(n):
    return n == 0

def make_a_list(n):
    return list(range(1, n + 1))

def initial_t(m):
    return m - 1

def remove_elem(a, t):
    return a[:t] + a[t+1:]

def update_t(t, k, a):
    return (t - 1 + k) % len(a)

def solve_one_case(n, k, m):
    a = make_a_list(n)
    t = initial_t(m)
    for _ in range(n - 1):
        a = remove_elem(a, t)
        t = update_t(t, k, a)
    return a[0]

def join_results(rr):
    return '\n'.join(map(str, rr))

def main_loop():
    rr = []
    while True:
        n_k_m = read_n_k_m()
        n = n_k_m[0]
        k = n_k_m[1]
        m = n_k_m[2]
        if is_termination(n):
            break
        res = solve_one_case(n, k, m)
        rr.append(res)
    return join_results(rr)

def main():
    set_recursion_limit()
    # inf, eps, mod defined but not used, maintain for completeness
    inf = get_inf()
    eps = get_eps()
    mod = get_mod()
    result = main_loop()
    return result

print(main())