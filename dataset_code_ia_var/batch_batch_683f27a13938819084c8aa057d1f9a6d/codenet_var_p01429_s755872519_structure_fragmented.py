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

def set_sys_recursion_limit():
    sys.setrecursionlimit(10 ** 7)

def get_constants():
    return 10 ** 20, 1.0 / 10 ** 13, 10 ** 9 + 7

def get_directions():
    dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    return dd, ddn

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
    print(s, flush=True)

def main():
    set_sys_recursion_limit()
    inf, eps, mod = get_constants()
    dd, ddn = get_directions()
    rr = []
    def read_input():
        return LI()
    def is_termination_case(n):
        return n == 0
    def process_case(n, m, l):
        k = get_k(n)
        s = get_s(m)
        wam = get_wam(m, s)
        wa, wb = get_wa_wb(n, k, wam)
        fm = initialize_fm(wa, wb, l)
        r = compute_min_result(n, wa, wb, l, fm)
        return r
    def get_k(n):
        k = LI()
        k = sorted(k)
        return k
    def get_s(m):
        s = LI()
        return s
    def get_wam(m, s):
        wam = [0] * (m + 1)
        def accumulate(i):
            wam[i + 1] = wam[i] + s[i]
        for i in range(m):
            accumulate(i)
        return wam
    def get_wa_wb(n, k, wam):
        wa = [0] * n
        wb = [0] * n
        def fill_wa_wb(i):
            wa[i] = wam[k[i]]
            wb[i] = wam[k[i] - 1]
        for i in range(n):
            fill_wa_wb(i)
        return wa, wb
    def initialize_fm(wa, wb, l):
        fm = {}
        fm[(0, 0)] = 0
        if len(wa) > 1 and len(wb) > 0:
            fm[(0, 1)] = (wa[1] - wb[0]) // l
        return fm
    def f_memoized(wa, wb, l, fm):
        def _f(i, j):
            key = (i, j)
            if key in fm:
                return fm[key]
            r = inf
            if i == j - 1:
                for k in range(i):
                    t = _f(k, i) + (wa[j] - wb[k]) // l
                    if r > t:
                        r = t
            else:
                t = _f(i, j - 1) + (wa[j] - wb[j - 1]) // l
                if r > t:
                    r = t
            fm[key] = r
            return r
        return _f
    def compute_min_result(n, wa, wb, l, fm):
        r = inf
        _f = f_memoized(wa, wb, l, fm)
        for i in range(1, n - 1):
            t = _f(i, n - 1)
            u = (wa[n - 1] - wb[i]) // l
            if r > t + u:
                r = t + u
        return r
    while True:
        data = read_input()
        if len(data) < 3:
            continue
        n, m, l = data
        if is_termination_case(n):
            break
        result = process_case(n, m, l)
        rr.append(result)
        break
    def output_result(rr):
        return '\n'.join(map(str, rr))
    return output_result(rr)

print(main())