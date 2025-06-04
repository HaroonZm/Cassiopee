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
eps = 1.0 / 10**13
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

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

def read_grid_dimensions():
    r, c, m = LI()
    return r, c, m

def read_grid_rows(r, c):
    grid = []
    for _ in range(r):
        row = S()
        grid.append([None if ch == '.' else 1 for ch in row])
    return grid

def add_padding(matrix, pad_value=1):
    if not matrix:
        return [[pad_value, pad_value], [pad_value, pad_value]]
    rows = len(matrix)
    cols = len(matrix[0])
    padded = [[pad_value]*(cols+2)]
    for row in matrix:
        padded.append([pad_value]+row+[pad_value])
    padded.append([pad_value]*(cols+2))
    return padded

def read_int_matrix(r, c):
    matrix = []
    for _ in range(r):
        matrix.append(LI())
    return matrix

def pad_and_read_matrix(r, c):
    return add_padding(read_int_matrix(r, c))

def read_positions(m):
    positions = []
    for _ in range(m):
        positions.append(tuple(map(lambda x: x+1, LI())))
    return positions

def is_wall(cell):
    return cell is not None

def make_adjacency(r, c, a):
    e = collections.defaultdict(list)
    for i in range(1, r+1):
        for j in range(1, c+1):
            if is_wall(a[i][j]):
                continue
            for di, dj in dd:
                ni, nj = i+di, j+dj
                if is_wall(a[ni][nj]):
                    continue
                e[(i, j)].append(((ni, nj), 1))
    return e

def dijkstra_search(s, e):
    d = collections.defaultdict(lambda: inf)
    d[s] = 0
    q = []
    heapq.heappush(q, (0, s))
    v = collections.defaultdict(bool)
    while q:
        k, u = heapq.heappop(q)
        if v[u]:
            continue
        v[u] = True
        for uv, ud in e[u]:
            if v[uv]:
                continue
            vd = k + ud
            if d[uv] > vd:
                d[uv] = vd
                heapq.heappush(q, (vd, uv))
    return d

def get_all_distances(ms, e):
    ad = {}
    for k in ms:
        if k in ad:
            continue
        ad[k] = dijkstra_search(k, e)
    return ad

def get_next_in_path(ad, start, end):
    c = start
    t = end
    path = []
    ti = 0
    td = collections.defaultdict(list)
    td[c].append(0)
    while c != t:
        cc = ad[t][c]
        for di, dj in dd:
            ni, nj = c[0]+di, c[1]+dj
            n = (ni, nj)
            if ad[t][n] == cc - 1:
                ti += 1
                td[n].append(ti)
                c = n
                break
    return td

def merge_path_dicts(dict1, dict2):
    for k, v in dict2.items():
        dict1[k].extend(v)
    return dict1

def build_full_path(ms, ad):
    if not ms:
        return collections.defaultdict(list)
    td = collections.defaultdict(list)
    c = ms[0]
    td[c].append(0)
    last = c
    ti = 0
    for t in ms[1:]:
        subt = get_next_in_path(ad, last, t)
        if t not in subt or len(subt[t]) == 0:
            td[t].append(ti+1)
        else:
            ti = max([max(lst) for lst in subt.values()] + [ti])
            td = merge_path_dicts(td, subt)
        last = t
    return td

def compute_tr_for_cell(v, cost, on, off):
    cs = cost
    onf = on + off
    tr = onf
    for vi in range(len(v)-1):
        sa = v[vi+1] - v[vi]
        tr += min(cs * sa, onf)
    return tr

def compute_result(td, cost, on, off):
    r = 0
    for k, v in sorted(td.items()):
        i, j = k
        r += compute_tr_for_cell(v, cost[i][j], on[i][j], off[i][j])
    return r

def solve_instance():
    r, c, m = read_grid_dimensions()
    grid_rows = read_grid_rows(r, c)
    a = add_padding(grid_rows)
    cost = pad_and_read_matrix(r, c)
    on = pad_and_read_matrix(r, c)
    off = pad_and_read_matrix(r, c)
    ms = read_positions(m)
    e = make_adjacency(r, c, a)
    ad = get_all_distances(ms, e)
    td = build_full_path(ms, ad)
    res = compute_result(td, cost, on, off)
    return res

def main():
    rr = []
    def run_once():
        return solve_instance()
    while True:
        rr.append(run_once())
        break
    return '\n'.join(map(str, rr))

print(main())