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
    sys.setrecursionlimit(10**7)

def get_inf():
    return 10**20

def get_eps():
    return 1.0 / 10**13

def get_mod():
    return 10**9 + 7

def get_dd():
    return [(-1,0),(0,1),(1,0),(0,-1)]

def get_ddn():
    return [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

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

def multiply_by_ten(x):
    return x * 10

def get_input_pair():
    return LS()

def read_graph_edges(n):
    edges = []
    for _ in range(n):
        a, b, c = LS()
        edges.append((a, b, int(c)))
    return edges

def build_graph(edges):
    e = collections.defaultdict(list)
    for a, b, c in edges:
        e[a].append((b, c))
        e[b].append((a, c))
    return e

def read_cs(m):
    cs = set()
    for _ in range(m):
        cs.add(S())
    return cs

def node_state(node, capacity):
    return (node, capacity)

def default_dict_inf():
    return collections.defaultdict(lambda: get_inf())

def default_dict_bool():
    return collections.defaultdict(bool)

def heap_push(q, value):
    heapq.heappush(q, value)

def heap_pop(q):
    return heapq.heappop(q)

def valid_uc(uc):
    return uc >= 0

def update_capacity_if_cs(uv, cs, cap, uc):
    if uv in cs:
        return cap
    return uc

def should_skip_visited(v, u):
    return v[u]

def update_if_better_distance(d, uv, vd):
    if d[uv] > vd:
        d[uv] = vd
        return True
    return False

def build_result_list():
    return []

def string_join_newline(lst):
    return '\n'.join(map(str, lst))

def break_if_zero(n):
    return n == 0

def search_path(s, t, e, cap, cs):
    d = default_dict_inf()
    d[node_state(s, cap)] = 0
    q = []
    v = default_dict_bool()
    heap_push(q, (0, node_state(s, cap)))
    while queue_not_empty(q):
        k, u = heap_pop(q)
        if should_skip_visited(v, u):
            continue
        v[u] = True
        if is_target_node(u, t):
            return k
        for uv, ud in e[u[0]]:
            uc = u[1] - ud
            if not valid_uc(uc):
                continue
            uc = update_capacity_if_cs(uv, cs, cap, uc)
            uv_state = node_state(uv, uc)
            if should_skip_visited(v, uv_state):
                continue
            vd = k + ud
            if update_if_better_distance(d, uv_state, vd):
                heap_push(q, (vd, uv_state))
    return None

def queue_not_empty(q):
    return len(q) > 0

def is_target_node(u, t):
    return u[0] == t

def return_negative_if_none(r):
    if r is None:
        return -1
    return r

def handle_case(n, m, cap):
    cap = multiply_by_ten(cap)
    s, t = get_input_pair()
    edges = read_graph_edges(n)
    e = build_graph(edges)
    cs = read_cs(m)
    result = search_path(s, t, e, cap, cs)
    return return_negative_if_none(result)

def main():
    set_sys_recursion_limit()
    rr = build_result_list()
    while True:
        n, m, l = LI()
        if break_if_zero(n):
            break
        rr.append(handle_case(n, m, l))
    return string_join_newline(rr)

print(main())