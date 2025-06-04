import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product, groupby, combinations_with_replacement
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = 10**10
mod = 10 ** 9 + 7

def construct_level_vec(v):
    return [-1]*v

def construct_ite_vec(v):
    return [0]*v

def create_edge_list(v):
    return [[] for _ in range(v)]

def create_graph(v):
    return create_edge_list(v)

def get_inf():
    return 10**10

def calc_index(R, C, i, j):
    return C*i+j

def vertical_newv(R, C, i, j):
    return R*C+C*i+j

def horizontal_newv(R, C, i, j):
    return 2*R*C+C*i+j

def in_matrix(i, j, R, C):
    return 0 <= i < R and 0 <= j < C

class Dinic:
    def __init__(self, v, inf=10**10):
        self.init_vars(v, inf)

    def init_vars(self, v, inf):
        self.v = v
        self.inf = inf
        self.G = create_graph(v)
        self.level = construct_level_vec(v)
        self.ite = construct_ite_vec(v)

    def add_edge_to_g(self, fr, to, cap):
        self.G[fr].append([to, cap, len(self.G[to])])
        self.G[to].append([fr, 0, len(self.G[fr])-1])

    def add_edge(self, fr, to, cap):
        self.add_edge_to_g(fr, to, cap)

    def init_bfs(self, s):
        self.level = construct_level_vec(self.v)
        self.level[s] = 0
        Q = deque()
        Q.append(s)
        return Q

    def next_bfs_node(self, Q):
        return Q.popleft()

    def try_bfs_edge(self, e, v, Q):
        if e[1]>0 and self.level[e[0]]<0:
            self.level[e[0]] = self.level[v]+1
            Q.append(e[0])

    def process_bfs_edges(self, v, Q):
        for i in range(len(self.G[v])):
            e = self.G[v][i]
            self.try_bfs_edge(e, v, Q)

    def bfs(self, s):
        Q = self.init_bfs(s)
        while Q:
            v = self.next_bfs_node(Q)
            self.process_bfs_edges(v, Q)

    def found_flow_end(self, v, t):
        return v == t

    def update_ite(self, v, i):
        self.ite[v] = i

    def forward_dfs(self, e, v):
        return e[1]>0 and self.level[v]<self.level[e[0]]

    def update_cap(self, e, d):
        e[1] -= d

    def update_rev_cap(self, e, d):
        self.G[e[0]][e[2]][1] += d

    def process_dfs_edges(self, v, t, f):
        for i in range(self.ite[v], len(self.G[v])):
            self.update_ite(v, i)
            e = self.G[v][i]
            if self.forward_dfs(e, v):
                d = self.dfs(e[0], t, min(f, e[1]))
                if d>0:
                    self.update_cap(e, d)
                    self.update_rev_cap(e, d)
                    return d
        return 0

    def dfs(self, v, t, f):
        if self.found_flow_end(v, t):
            return f
        return self.process_dfs_edges(v, t, f)

    def reset_ite(self):
        self.ite = construct_ite_vec(self.v)

    def set_bfs(self, s):
        self.bfs(s)

    def bfs_unreachable(self, t):
        return self.level[t]<0

    def dfs_flow(self, s, t):
        return self.dfs(s,t,self.inf)

    def max_flow_loop(self, s, t, flow):
        while True:
            self.set_bfs(s)
            if self.bfs_unreachable(t):
                return flow
            self.reset_ite()
            f = self.dfs_flow(s, t)
            while f>0:
                flow += f
                f = self.dfs_flow(s, t)

    def max_flow(self, s, t):
        return self.max_flow_loop(s, t, 0)

def read_dims():
    return list(MAP())

def read_matrix(R):
    return [input() for _ in range(R)]

def get_Dinic_nodes(R, C):
    return 3*R*C+2

def get_source_sink(R, C):
    s = 3*R*C
    t = s+1
    return s, t

def is_block(cell):
    return cell != '.'

def skip_block(cell):
    return cell == '.'

def vertical_possible(i, R):
    return i+1 < R

def horizontal_possible(j, C):
    return j+1 < C

def is_sharp(cell):
    return cell == '#'

def update_block(block):
    return block + 1

def update_adj(adj):
    return adj + 1

def add_vertical_edge(D, R, C, i, j, t):
    newv = vertical_newv(R, C, i, j)
    D.add_edge(newv, t, 1)
    D.add_edge(calc_index(R, C, i, j), newv, INF)
    D.add_edge(calc_index(R, C, i+1, j), newv, INF)

def add_horizontal_edge(D, R, C, i, j, s):
    newv = horizontal_newv(R, C, i, j)
    D.add_edge(s, newv, 1)
    D.add_edge(newv, calc_index(R, C, i, j), INF)
    D.add_edge(newv, calc_index(R, C, i, j+1), INF)

def process_cell(D, S, i, j, R, C, s, t, block, adj):
    if skip_block(S[i][j]):
        return block, adj
    block = update_block(block)
    if vertical_possible(i, R) and is_sharp(S[i+1][j]):
        adj = update_adj(adj)
        add_vertical_edge(D, R, C, i, j, t)
    if horizontal_possible(j, C) and is_sharp(S[i][j+1]):
        adj = update_adj(adj)
        add_horizontal_edge(D, R, C, i, j, s)
    return block, adj

def process_grid(D, S, R, C, s, t):
    block = 0
    adj = 0
    for i in range(R):
        for j in range(C):
            block, adj = process_cell(D, S, i, j, R, C, s, t, block, adj)
    return block, adj

def final_output(block, adj, flow):
    print(block-(adj-flow))

def main():
    R, C = read_dims()
    S = read_matrix(R)
    dinic_nodes = get_Dinic_nodes(R, C)
    D = Dinic(dinic_nodes)
    s, t = get_source_sink(R, C)
    block, adj = process_grid(D, S, R, C, s, t)
    flow = D.max_flow(s, t)
    final_output(block, adj, flow)

main()