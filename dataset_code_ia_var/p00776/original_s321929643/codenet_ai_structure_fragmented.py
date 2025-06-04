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
    sys.setrecursionlimit(10**7)

def init_constants():
    return 10**20, 1.0/10**10, 10**9+7

def get_directions():
    dd = [(-1,0),(0,1),(1,0),(0,-1)]
    ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    return dd, ddn

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
    print(s, flush=True)

def build_char_dicts():
    ac = {}
    ca = {}
    for i in range(26):
        t = int(2**i)
        c = chr(ord('a') + i)
        ac[t] = c
        ca[c] = t
    return ac, ca

def string_to_vals(s, ca):
    return [ca[c] for c in s]

def get_ca_z(ca):
    return ca['z']

def get_char_double(c):
    return c * 2

def make_ndict():
    return collections.defaultdict(int)

def update_d_for_char(a, ca):
    z = get_ca_z(ca)
    d = collections.defaultdict(int)
    d[0] = 1

    for c in a:
        nd = make_ndict()
        c2 = get_char_double(c)
        for k, v in d.items():
            if k & c or c == 1:
                nd[k] += v
            if c != z and k & c2 == 0:
                nd[k | c2] += v
        d = nd
    return d

def calc_d_sum(d):
    return sum(d.values())

def update_ss_set(ss, t):
    ns = set()
    t2 = chr(ord(t) + 1)
    for si in ss:
        if t in si or t == 'a':
            ns.add(si + t)
        if t != 'z' and t2 not in si:
            ns.add(si + t2)
    return ns

def keep_top5(ss):
    return set(sorted(ss)[:5])

def keep_rev_top5(ss):
    return set(sorted(ss, reverse=True)[:5])

def build_rs1(s):
    ss = set([''])
    for t in s:
        ns = update_ss_set(ss, t)
        ss = keep_top5(ns)
    return ss

def build_rs2(s):
    ss = set([''])
    for t in s:
        ns = update_ss_set(ss, t)
        ss = keep_rev_top5(ns)
    return ss

def join_sets(a, b):
    return a | b

def sort_rs(rs):
    return sorted(rs)

def f(s):
    ac, ca = build_char_dicts()
    a = string_to_vals(s, ca)
    d = update_d_for_char(a, ca)
    r0 = [calc_d_sum(d)]

    rs1 = build_rs1(s)
    rs2 = build_rs2(s)
    rs = join_sets(rs1, rs2)
    r_rest = sort_rs(rs)
    return r0 + r_rest

def input_loop(f):
    rr = []
    while True:
        s = S()
        if s == '#':
            break
        rr.extend(f(s))
    return rr

def to_output_str(arr):
    return '\n'.join(map(str, arr))

def main():
    set_recursion_limit()
    inf, eps, mod = init_constants()
    dd, ddn = get_directions()
    rr = input_loop(f)
    return to_output_str(rr)

print(main())