import sys
from collections import defaultdict, deque
from functools import partial

input = sys.stdin.readline

N, Q = map(int, input().split())
EDGE = [tuple(map(int, input().split())) for _ in range(N - 1)]
Query = [tuple(map(int, input().split())) for _ in range(Q)]
mod = 10**9 + 7

# Adjacency list with edge data
EDGELIST = [defaultdict(tuple) for _ in range(N + 1)]
for x, y, c, l in EDGE:
    EDGELIST[x][y] = (c, l)
    EDGELIST[y][x] = (c, l)

# -- Euler Tour + Segment Tree for LCA

DEPTH = [-1] * (N + 1)
DEPTH[1] = 0

EULER, FIRST = [], [None] * (N + 1)

def dfs(u, parent, d):
    DEPTH[u] = d
    FIRST[u] = len(EULER)
    EULER.append((d, u))
    for v in EDGELIST[u]:
        if v != parent:
            dfs(v, u, d + 1)
            EULER.append((d, u))

dfs(1, -1, 0)
LEN = len(EULER)

# Segment tree for RMQ (on (depth, node))
size = 1 << LEN.bit_length()
SEG = [(1 << 30, 0)] * (2 * size)
SEG[size:size + LEN] = EULER
for i in range(size - 1, 0, -1):
    SEG[i] = min(SEG[i << 1], SEG[i << 1 | 1])

def lca(u, v):
    l, r = FIRST[u], FIRST[v]
    if l > r: l, r = r, l
    l += size
    r += size + 1
    res = (1 << 30, 0)
    while l < r:
        if l & 1:
            res = min(res, SEG[l])
            l += 1
        if r & 1:
            r -= 1
            res = min(res, SEG[r])
        l >>= 1
        r >>= 1
    return res[1]

# -- Preprocessing for queries

# Find which edge-color pairs need in-out sums
nodes_to_col = [set() for _ in range(N + 1)]
for c, l, x, y in Query:
    nodes_to_col[x].add(c)
    nodes_to_col[y].add(c)
    nodes_to_col[lca(x, y)].add(c)

# DP for sum of lengths and color-specific values up to current node
LENGTH = [0] * (N + 1)
tot_len = 0
color_len = defaultdict(int)
color_cnt = defaultdict(int)
C_LDICT = dict()
C_SDICT = dict()

def dfs2(u, parent):
    global tot_len
    for c in nodes_to_col[u]:
        C_LDICT[(u, c)] = color_len[c]
        C_SDICT[(u, c)] = color_cnt[c]
    for v in EDGELIST[u]:
        if v != parent:
            c, l = EDGELIST[u][v]
            tot_len += l
            color_len[c] += l
            color_cnt[c] += 1
            LENGTH[v] = tot_len
            dfs2(v, u)
            tot_len -= l
            color_len[c] -= l
            color_cnt[c] -= 1

dfs2(1, -1)

# -- Answer queries
out = []
for c, pl, x, y in Query:
    anc = lca(x, y)
    tot = LENGTH[x] + LENGTH[y] - 2 * LENGTH[anc]
    n_c = (
        C_SDICT.get((x, c), 0) + C_SDICT.get((y, c), 0) - 2 * C_SDICT.get((anc, c), 0)
    )
    l_c = (
        C_LDICT.get((x, c), 0) + C_LDICT.get((y, c), 0) - 2 * C_LDICT.get((anc, c), 0)
    )
    ans = tot + n_c * pl - l_c
    print(ans)