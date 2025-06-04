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

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353
dd = [(0,-1),(1,0),(0,1),(-1,0)]
ddn = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1)]

def LI():
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    return [int(x)-1 for x in sys.stdin.readline().split()]

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

def read_n_l():
    n, l = LI()
    return n, l

def process_ls(n):
    a = []
    b = []
    for idx in range(n):
        d, p = LS()
        dird = d
        pos = int(p)
        if pos % 2 == 0:
            a.append((dird, pos, idx+1))
        else:
            b.append((dird, pos, idx+1))
    return a, b

def update_max(lc, rm, rf, d, p, i, l):
    if d == 'L':
        lc += 1
    m = int(p)
    if d == 'R':
        m = l - m
    if rm < m or (rm == m and d == 'L'):
        rm = m
        rf = d == 'R'
    return lc, rm, rf

def find_ri_and_rf(a, l, init_rm):
    lc = 0
    rm = init_rm
    rf = False
    for d, p, i in a:
        lc, rm, rf = update_max(lc, rm, rf, d, p, i, l)
    ri = lc
    if rf:
        ri = lc + 1
    ari = -1
    if a:
        ari = a[ri-1][2]
    return rm, rf, ari, lc, ri

def update_max_b(lc, rm, rf, af, d, p, i, l):
    if d == 'L':
        lc += 1
    m = int(p)
    if d == 'R':
        m = l - m
    if rm < m or (rm == m and d == 'L'):
        rm = m
        rf = d == 'R'
        af = False
    return lc, rm, rf, af

def find_bri_and_rf(b, l, init_rm):
    lc = 0
    rm = init_rm
    rf = False
    af = True
    for d, p, i in b:
        lc, rm, rf, af = update_max_b(lc, rm, rf, af, d, p, i, l)
    ri = lc
    if rf:
        ri = lc + 1
    bri = -1
    if b:
        bri = b[ri-1][2]
    return rm, rf, bri, lc, ri, af

def build_result(af, rm, ari, bri):
    if af:
        return '{} {}'.format(rm, ari)
    else:
        return '{} {}'.format(rm, bri)

def process_test_case(n, l):
    a, b = process_ls(n)
    rm_a, rf_a, ari, lc_a, ri_a = find_ri_and_rf(a, l, 0)
    rm_b, rf_b, bri, lc_b, ri_b, af = find_bri_and_rf(b, l, rm_a)
    res = build_result(af, max(rm_a, rm_b), ari, bri)
    return res

def main_loop():
    rr = []
    while True:
        n, l = read_n_l()
        if n == 0:
            break
        res = process_test_case(n, l)
        rr.append(res)
    return rr

def main():
    results = main_loop()
    return '\n'.join(map(str, results))

print(main())