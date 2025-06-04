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

def set_recursion_limit():
    sys.setrecursionlimit(10**7)

def get_inf():
    return 10**20

def get_eps():
    return 1.0 / 10**10

def get_mod():
    return 10**9 + 7

def get_mod2():
    return 998244353

def get_dd():
    return [(-1,0),(0,1),(1,0),(0,-1)]

def get_ddn():
    return [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI():
    return list(map(int, sys.stdin.readline().split()))

def read_int_list():
    return list(map(int, sys.stdin.readline().split()))

def LLI():
    return [list(map(int, l.split())) for l in sys.stdin.readlines()]

def read_lines_of_int_lists():
    return [list(map(int, l.split())) for l in sys.stdin.readlines()]

def LI_():
    return [int(x)-1 for x in sys.stdin.readline().split()]

def read_int_list_minus_1():
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    return [float(x) for x in sys.stdin.readline().split()]

def read_float_list():
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    return sys.stdin.readline().split()

def read_str_list():
    return sys.stdin.readline().split()

def I():
    return int(sys.stdin.readline())

def read_int():
    return int(sys.stdin.readline())

def F():
    return float(sys.stdin.readline())

def read_float():
    return float(sys.stdin.readline())

def S():
    return input()

def read_input():
    return input()

def pf(s):
    return print(s, flush=True)

def pe(s):
    return print(str(s), file=sys.stderr)

def JA(a, sep):
    return sep.join(map(str, a))

def JAA(a, s, t):
    return s.join(t.join(map(str, b)) for b in a)

def parse_first_input():
    return LI()

def parse_lrc(m):
    lrc = [LI() for _ in range(m)]
    return lrc

def lrc_sort_key(x):
    return (x[0], x[2], -x[1])

def append_inf_lrc(lrc, inf):
    lrc.append([inf, inf, inf])
    return lrc

def initialize_index():
    return 0

def initialize_q(inf):
    return [(1, 0), (inf, inf)]

def update_index1(lrc, i, l):
    while lrc[i][0] < l:
        i += 1
    return i

def update_index2(lrc, i, l, q):
    while lrc[i][0] == l:
        i, q = process_lrc_entry(lrc, i, q, l)
    return i, q

def process_lrc_entry(lrc, i, q, l):
    _, r, c = lrc[i]
    i += 1
    qi = q_find_index(q, l)
    _, cc = q[qi]
    t = compute_new_tuple(r, cc, c)
    q = update_q(q, t, r)
    return i, q

def q_find_index(q, l):
    return bisect.bisect_left(q, (l, -1))

def compute_new_tuple(r, cc, c):
    return (r, cc + c)

def update_q(q, t, r):
    ti = bisect.bisect_left(q, t)
    if q_must_update(q, ti, t, r):
        q, ti = update_q_insert(q, ti, t, r)
        q = remove_less_optimal(q, ti, t)
    return q

def q_must_update(q, ti, t, r):
    return q[ti][1] > t[1] and q[ti-1][0] < r

def update_q_insert(q, ti, t, r):
    if q[ti][0] == r:
        q[ti] = t
    else:
        q.insert(ti, t)
    return q, ti

def remove_less_optimal(q, ti, t):
    while q[ti-1][1] > t[1]:
        del q[ti-1]
        ti -= 1
    return q

def calc_result(q, n):
    t = q[-2]
    if t[0] < n:
        return -1
    return t[1]

def wrapped_main():
    set_recursion_limit()
    inf = get_inf()
    n, m = parse_first_input()
    lrc = parse_lrc(m)
    lrc = sorted(lrc, key=lrc_sort_key)
    lrc = append_inf_lrc(lrc, inf)
    i = initialize_index()
    q = initialize_q(inf)
    for l in range(1, n):
        i = update_index1(lrc, i, l)
        i, q = update_index2(lrc, i, l, q)
    result = calc_result(q, n)
    return result

print(wrapped_main())