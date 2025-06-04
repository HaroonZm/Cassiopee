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
    return print(s, flush=True)

def create_zero_matrix(n):
    return [[0] * n for _ in range(n)]

def read_edges(m):
    return [LI_() for _ in range(m)]

def read_source_and_sink():
    return LI_()

def update_edge_matrix(e, x, y):
    e[x][y] = 1
    e[y][x] = 1

def build_edge_matrix(n, a):
    e = create_zero_matrix(n)
    for x, y in a:
        update_edge_matrix(e, x, y)
    return e

def find_used_edges(e, a):
    re = []
    for i in range(len(a)):
        x, y = a[i]
        if e[y][x] == 0:
            re.append(i + 1)
    return re

class Flow():
    def __init__(self, e, N):
        self.E = e
        self.N = N

    def max_flow(self, s, t):
        r = 0
        e = self.E

        def create_visited():
            return [0] * self.N

        def augmenting_path(c):
            v = self.v
            v[c] = 1
            if c == t:
                return 1
            for i in range(self.N):
                if v[i] == 0 and e[c][i] > 0 and augmenting_path(i) > 0:
                    e[c][i] -= 1
                    e[i][c] += 1
                    return 1
            return 0

        def process_augment(s):
            self.v = create_visited()
            return augmenting_path(s)

        while True:
            if process_augment(s) == 0:
                break
            r += 1
        return r

def compute_flow_and_edges(n, m):
    a = read_edges(m)
    s, t = read_source_and_sink()
    e = build_edge_matrix(n, a)
    fl = Flow(e, n)
    r = fl.max_flow(s, t)
    used_edges = find_used_edges(e, a)
    return [r, len(used_edges)] + used_edges

def read_n_m():
    return LI()

def should_break(n):
    return n == 0

def process_main_loop():
    results = []
    while True:
        n, m = read_n_m()
        if should_break(n):
            break
        results.extend(compute_flow_and_edges(n, m))
        break
    return results

def result_to_str(rr):
    return '\n'.join(map(str, rr))

def main():
    set_recursion_limit()
    rr = process_main_loop()
    return result_to_str(rr)

print(main())