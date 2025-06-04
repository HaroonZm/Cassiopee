import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product, groupby, combinations_with_replacement
from operator import itemgetter, mul
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from heapq import heappush, heappop
from functools import reduce
from typing import List, Tuple, Callable

input = lambda: sys.stdin.readline().strip()
INT = lambda: int(input())
MAP = lambda: map(int, input().split())
LIST = lambda: list(map(int, input().split()))
ZIP = lambda n: zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(1 << 25)
INF = float('inf')
mod = 10 ** 9 + 7

class Dinic:
    __slots__ = ('v', 'inf', 'G', 'level', 'ite')
    def __init__(self, v: int, inf: int = 10 ** 10) -> None:
        self.v = v
        self.inf = inf
        self.G = [[] for _ in range(v)]
        self.level = [-1] * v
        self.ite = [0] * v

    def add_edge(self, fr: int, to: int, cap: int) -> None:
        self.G[fr].append([to, cap, len(self.G[to])])
        self.G[to].append([fr, 0, len(self.G[fr]) - 1])

    def bfs(self, s: int) -> None:
        lv = self.level
        lv[:] = [-1] * self.v
        lv[s] = 0
        Q = deque([s])
        G = self.G
        while Q:
            v = Q.popleft()
            for to, cap, rev in G[v]:
                if cap > 0 and lv[to] < 0:
                    lv[to] = lv[v] + 1
                    Q.append(to)

    def dfs(self, v: int, t: int, f: int) -> int:
        if v == t:
            return f
        Gv, lv, ite = self.G[v], self.level, self.ite
        for i in range(ite[v], len(Gv)):
            ite[v] = i
            to, cap, rev = Gv[i]
            if cap and lv[v] < lv[to]:
                d = self.dfs(to, t, min(f, cap))
                if d:
                    Gv[i][1] -= d
                    self.G[to][rev][1] += d
                    return d
        return 0

    def max_flow(self, s: int, t: int) -> int:
        flow = 0
        inf = self.inf
        while True:
            self.bfs(s)
            if self.level[t] < 0:
                return flow
            self.ite[:] = [0] * self.v
            while (f := self.dfs(s, t, inf)):
                flow += f

ctoi = lambda c: ord(c) - ord('a')

N = INT()
S = [input() for _ in range(N)]

ans = []
num_letters = len(ascii_lowercase)
for i, alpha in enumerate(ascii_lowercase):
    D = Dinic(num_letters + 2)
    s, t = num_letters, num_letters + 1
    deg_in = deg_out = 0
    for x in S:
        u, v = ctoi(x[0]), ctoi(x[-1])
        if u == i:
            u = s
            deg_out += 1
        if v == i:
            v = t
            deg_in += 1
        D.add_edge(u, v, 1)
    f = D.max_flow(s, t)
    if f >= deg_out and deg_in:
        ans.append(alpha)

print(*ans, sep="\n")