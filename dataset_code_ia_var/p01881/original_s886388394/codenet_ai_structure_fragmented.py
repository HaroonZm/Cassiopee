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

def get_dd():
    return [(0,-1),(1,0),(0,1),(-1,0)]

def get_ddn():
    return [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1)]

def read_line():
    return sys.stdin.readline()

def LI():
    return [int(x) for x in read_line().split()]

def LI_():
    return [int(x)-1 for x in read_line().split()]

def LF():
    return [float(x) for x in read_line().split()]

def LS():
    return read_line().split()

def I():
    return int(read_line())

def F():
    return float(read_line())

def S():
    return input()

def pf(s):
    return print(s, flush=True)

def prepare_input_lines(h):
    return [S() for _ in range(h)]

def is_inside_grid(i, j, h, w):
    return 0 <= i < h and 0 <= j < w

def is_wall(mp, i, j):
    return mp[i][j] == '#'

def maybe_update_distance(d, node, new_dist, q):
    if d[node] > new_dist:
        d[node] = new_dist
        heapq.heappush(q, (new_dist, node))

def get_initial_nodes(h, w, mp):
    sources = []
    person = None
    end = None
    for i in range(h):
        for j in range(w):
            if mp[i][j] == '$':
                sources.append((i, j))
            elif mp[i][j] == '@':
                person = (i, j)
            elif mp[i][j] == '%':
                end = (i, j)
    return sources, person, end

def get_neighbors(u, dd, h, w, mp):
    result = []
    for di, dj in dd:
        ni, nj = u[0] + di, u[1] + dj
        if is_inside_grid(ni, nj, h, w) and not is_wall(mp, ni, nj):
            result.append((ni, nj))
    return result

def node_visited(v, u):
    return v[u]

def set_visited(v, u):
    v[u] = True

def bfs_search(ss, h, w, mp, dd):
    inf = get_inf()
    d = collections.defaultdict(lambda: inf)
    q = []
    for s in ss:
        d[s] = 0
        heapq.heappush(q, (0, s))
    v = collections.defaultdict(bool)
    while len(q):
        k, u = heapq.heappop(q)
        if node_visited(v, u):
            continue
        set_visited(v, u)
        neighbors = get_neighbors(u, dd, h, w, mp)
        for uv in neighbors:
            if node_visited(v, uv):
                continue
            vd = k + 1
            maybe_update_distance(d, uv, vd, q)
    return d

def compare_person_and_sources(pd, d, es):
    return d[es] < pd[es]

def answer_yes():
    return 'Yes'

def answer_no():
    return 'No'

def main():
    set_recursion_limit()
    inf = get_inf()
    dd = get_dd()
    h, w = LI()
    mp = prepare_input_lines(h)
    ss, ps, es = get_initial_nodes(h, w, mp)
    pd = bfs_search(ss, h, w, mp, dd)
    d = bfs_search([ps], h, w, mp, dd)
    if compare_person_and_sources(pd, d, es):
        return answer_yes()
    return answer_no()

print(main())