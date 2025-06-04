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
    return 1.0 / 10 ** 13

def get_mod():
    return 10 ** 9 + 7

def get_dd():
    return [(-1, 0), (0, 1), (1, 0), (0, -1)]

def get_ddn():
    return [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

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

class Edge():
    def __init__(self, t, f, r, ca, co):
        self.to = t
        self.fron = f
        self.rev = r
        self.cap = ca
        self.cost = co

def create_mcf_graph(size):
    return [[] for _ in range(size)]

def init_mcf(size):
    return MinCostFlow(size)

def make_edge_list(graph, f, t, ca, co):
    graph[f].append(Edge(t, f, len(graph[t]), ca, co))
    graph[t].append(Edge(f, t, len(graph[f])-1, 0, -co))

def update_edge_cap(edge, flow):
    edge.cap -= flow

def update_rev_edge(mcf, edge, flow):
    mcf.graph[edge.to][edge.rev].cap += flow

def add_edge_to_mcf(mcf, f, t, ca, co):
    mcf.add_edge(f, t, ca, co)

def find_min_dist_path(mcf, s, t, inf):
    return mcf.min_path(s, t)

def update_total_cost(total_cost, c):
    total_cost += c
    return total_cost

def make_set():
    return set()

def add_edges_initial(n, mcf, s, node_end):
    for i in range(n):
        add_edge_to_mcf(mcf, s, i, 1, 0)
        add_edge_to_mcf(mcf, i, node_end, 1, 0)

def collect_ab_ss(n):
    a = []
    b = []
    ss = set()
    for _ in range(n):
        ai, bi = LI()
        a.append(ai)
        b.append(bi)
        ss.add(ai)
        ss.add(bi)
    return a, b, ss

def make_d_and_edges(mcf, n, ss, t):
    d = {}
    sorted_ss = sorted(ss)
    for i, v in zip(range(len(sorted_ss)), sorted_ss):
        d[v] = i + n
        add_edge_to_mcf(mcf, i + n, t, 1, 0)
    return d

def add_main_connection(mcf, node_end, t, inf):
    add_edge_to_mcf(mcf, node_end, t, inf, 0)

def add_pair_edges(mcf, n, d, a, b):
    for i in range(n):
        add_edge_to_mcf(mcf, i, d[a[i]], 1, -b[i])
        add_edge_to_mcf(mcf, i, d[b[i]], 1, -a[i])

class MinCostFlow():
    def __init__(self, size):
        self.size = size
        self.graph = create_mcf_graph(size)

    def add_edge(self, f, t, ca, co):
        make_edge_list(self.graph, f, t, ca, co)

    def min_path(self, s, t):
        inf = get_inf()
        dist, route, que, inq = self._init_min_path_vars(s, inf)
        self._bfs_min_path(s, dist, route, que, inq)
        if dist[t] == inf:
            return inf
        return self._calc_flow_and_cost(s, t, route, dist)

    def _init_min_path_vars(self, s, inf):
        dist = [inf] * self.size
        route = [None] * self.size
        que = collections.deque()
        inq = [False] * self.size
        dist[s] = 0
        que.append(s)
        inq[s] = True
        return dist, route, que, inq

    def _bfs_min_path(self, s, dist, route, que, inq):
        while que:
            u = que.popleft()
            inq[u] = False
            self._iterate_edges(u, dist, route, que, inq)

    def _iterate_edges(self, u, dist, route, que, inq):
        for e in self.graph[u]:
            self._handle_edge(e, u, dist, route, que, inq)

    def _handle_edge(self, e, u, dist, route, que, inq):
        if e.cap == 0:
            return
        v = e.to
        if dist[v] > dist[u] + e.cost:
            dist[v] = dist[u] + e.cost
            route[v] = e
            if not inq[v]:
                que.append(v)
                inq[v] = True

    def _calc_flow_and_cost(self, s, t, route, dist):
        inf = get_inf()
        flow = inf
        v = t
        while v != s:
            e = route[v]
            if flow > e.cap:
                flow = e.cap
            v = e.fron
        c = 0
        v = t
        while v != s:
            e = route[v]
            update_edge_cap(e, flow)
            update_rev_edge(self, e, flow)
            c += e.cost * flow
            v = e.fron
        return dist[t]

    def calc_min_cost_flow(self, s, t, flow):
        inf = get_inf()
        total_cost = 0
        for i in range(flow):
            c = self.min_path(s, t)
            if c == inf:
                return c
            total_cost = update_total_cost(total_cost, c)
        return total_cost

def prepare_main_variables():
    n = I()
    mcf = init_mcf(4096)
    s = 4094
    t = 4095
    node_end = 4093
    return n, mcf, s, t, node_end

def main():
    set_recursion_limit()
    inf = get_inf()
    n, mcf, s, t, node_end = prepare_main_variables()
    add_edges_initial(n, mcf, s, node_end)
    a, b, ss = collect_ab_ss(n)
    d = make_d_and_edges(mcf, n, ss, t)
    add_main_connection(mcf, node_end, t, inf)
    add_pair_edges(mcf, n, d, a, b)
    res = mcf.calc_min_cost_flow(s, t, n)
    return -res

print(main())