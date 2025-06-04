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

def get_inf():
    return 10 ** 20

def get_eps():
    return 1.0 / 10 ** 10

def get_mod():
    return 10 ** 9 + 7

def get_dd():
    return [(-1, 0), (0, 1), (1, 0), (0, -1)]

def get_ddn():
    return [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def li():
    return [int(x) for x in sys.stdin.readline().split()]

def li_():
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def lf():
    return [float(x) for x in sys.stdin.readline().split()]

def ls():
    return sys.stdin.readline().split()

def i():
    return int(sys.stdin.readline())

def f():
    return float(sys.stdin.readline())

def s():
    return input()

def pf(s):
    return print(s, flush=True)

def read_n():
    return i()

def read_a(n):
    return [ls() for _ in range(n)]

def create_d_and_ed(a, n):
    d = collections.defaultdict(int)
    ed = collections.defaultdict(lambda: None)
    for i in range(n):
        x, y, di = a[i]
        x = int(x)
        y = int(y)
        d[(x, y)] = i + 1
        if di == 'x':
            d[(x + 1, y)] = i + 1
            ed[(x, y)] = (x + 1, y)
            ed[(x + 1, y)] = (x, y)
        else:
            d[(x, y + 1)] = i + 1
            ed[(x, y)] = (x, y + 1)
            ed[(x, y + 1)] = (x, y)
    return d, ed

def build_ee(d):
    ee = collections.defaultdict(set)
    dd = get_dd()
    for x, y in list(d.keys()):
        dt = d[(x, y)]
        for di, dj in dd:
            ni = x + di
            nj = y + dj
            if d[(ni, nj)] > 0 and d[(ni, nj)] != dt:
                ee[(x, y)].add((ni, nj))
    return ee

def process_component(k, ee, ed, v):
    s1 = set()
    s2 = set()
    ns1 = set([k])
    ns2 = set()
    while ns1:
        na = list(ns1)
        s1 |= ns1
        ns1 = set()
        for k1 in na:
            ns1 |= ee[k1]
            ns2.add(ed[k1])
        ns2 -= s2
        while ns2:
            na2 = list(ns2)
            s2 |= ns2
            ns2 = set()
            for k2 in na2:
                ns2 |= ee[k2]
                ns1.add(ed[k2])
            ns2 -= s2
        ns1 -= s1
    return s1, s2

def mark_visited(s1, s2, v):
    for k in s1:
        v[k] = 1
    for k in s2:
        v[k] = 1

def is_valid_configuration(dka, ee, ed):
    v = collections.defaultdict(bool)
    for k in dka:
        if v[k]:
            continue
        s1, s2 = process_component(k, ee, ed, v)
        if s1 & s2:
            return False, v
        mark_visited(s1, s2, v)
    return True, v

def process_case(n):
    a = read_a(n)
    d, ed = create_d_and_ed(a, n)
    ee = build_ee(d)
    dka = list(d.keys())
    valid, v = is_valid_configuration(dka, ee, ed)
    return 'Yes' if valid else 'No'

def gather_results():
    results = []
    while True:
        n = read_n()
        if n == 0:
            break
        result = process_case(n)
        results.append(result)
    return results

def format_results(results):
    return '\n'.join(map(str, results))

def main():
    set_sys_recursion_limit()
    results = gather_results()
    return format_results(results)

print(main())