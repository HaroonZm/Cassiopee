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

def set_recursive_limit():
    sys.setrecursionlimit(10**7)

def get_inf():
    return 10**20

def get_eps():
    return 1.0 / 10**13

def get_mod():
    return 10**9+7

def get_dd():
    return [(-1,0),(0,1),(1,0),(0,-1)]

def get_ddn():
    return [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def read_int_list():
    return [int(x) for x in sys.stdin.readline().split()]

def read_int_list_minus1():
    return [int(x)-1 for x in sys.stdin.readline().split()]

def read_float_list():
    return [float(x) for x in sys.stdin.readline().split()]

def read_str_list():
    return sys.stdin.readline().split()

def read_int():
    return int(sys.stdin.readline())

def read_float():
    return float(sys.stdin.readline())

def read_str():
    return input()

def print_flush(s):
    print(s, flush=True)

def read_edges(m):
    edges = []
    for _ in range(m):
        edges.append(read_int_list())
    return edges

def build_adjacency(edges):
    e = collections.defaultdict(set)
    for b, c in edges:
        e[b].add(c)
    return e

def find_max(a):
    return max(a)

def prepare_reachable_dict(n, sm, e, a):
    ed = {}
    for i in range(1, n+1):
        t = compute_reachable_for_node(i, sm, e, a)
        ed[i] = t
    return ed

def compute_reachable_for_node(i, sm, e, a):
    t = {}
    q = set([i])
    for j in range(sm):
        nq = set()
        for c in q:
            nq |= e[c]
        if (j+1) in a:
            t[j+1] = nq
        q = nq
    return t

def create_distance_dict(n):
    d = collections.defaultdict(lambda: None)
    d[n] = 0
    return d

def run_ff(i, d, ed, a, inf):
    def ff(u):
        if not d[u] is None:
            return d[u]
        d[u] = inf
        mr = 0
        for nstep in a:
            mi = inf
            for ni in ed[u][nstep]:
                t = ff(ni)
                if mi > t:
                    mi = t
            if mr < mi:
                mr = mi
        d[u] = mr + 1
        return mr + 1
    return ff(i)

def iterative_clearance_and_recalc(n, d, ed, a, inf):
    res = run_ff(1, d, ed, a, inf)
    for tt in range(n):
        for ti in range(1, n+1):
            if (not d[ti] is None) and d[ti] > tt:
                d[ti] = None
        res = run_ff(1, d, ed, a, inf)
    return res

def handle_f(n, m, a, inf):
    edges = read_edges(m)
    e = build_adjacency(edges)
    sm = find_max(a)
    ed = prepare_reachable_dict(n, sm, e, a)
    d = create_distance_dict(n)
    res = run_ff(1, d, ed, a, inf)
    res = iterative_clearance_and_recalc(n, d, ed, a, inf)
    if res >= inf:
        return 'IMPOSSIBLE'
    return res

def read_next_case():
    return read_int_list()

def is_termination_case(n):
    return n == 0

def add_result(rr, val):
    rr.append(val)

def build_result_string(rr):
    return '\n'.join(map(str, rr))

def main():
    set_recursive_limit()
    inf = get_inf()
    rr = []
    while True:
        case_params = read_next_case()
        n, m, a, b, c = case_params
        if is_termination_case(n):
            break
        add_result(rr, handle_f(n, m, [a,b,c], inf))
        break
    return build_result_string(rr)

print(main())