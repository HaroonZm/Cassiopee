import sys
from collections import Counter, deque
from functools import partial

sys.setrecursionlimit(1 << 25)
input = partial(next, sys.stdin)
INF = float('inf')
MOD = 10 ** 9 + 7

def list2d(a, b, c): return [[c] * b for _ in range(a)]
def list3d(a, b, c, d): return [[[d] * c for _ in range(b)] for _ in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for _ in range(c)] for _ in range(b)] for _ in range(a)]
def ceil(x, y=1): return -(-x // y)
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(N=None): return list(MAP()) if N is None else [INT() for _ in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')

class Dinic:
    __slots__ = ('n', 'links', 'level', 'iter')
    def __init__(self, n):
        self.n = n
        self.links = [[] for _ in range(n)]
        self.level = [0] * n
        self.iter = [0] * n

    def add_edge(self, fr, to, cap):
        forward = [cap, to, None]
        backward = [0, fr, forward]
        forward[2] = backward
        self.links[fr].append(forward)
        self.links[to].append(backward)

    def bfs(self, s, t):
        level = [-1] * self.n
        q = deque([s])
        level[s] = 0
        while q:
            v = q.popleft()
            for cap, to, rev in self.links[v]:
                if cap and level[to] < 0:
                    level[to] = level[v] + 1
                    q.append(to)
        self.level = level
        return level[t] != -1

    def dfs(self, v, t, upTo):
        if v == t: return upTo
        for i in range(self.iter[v], len(self.links[v])):
            e = self.links[v][i]
            cap, to, rev = e
            if cap and self.level[v] < self.level[to]:
                d = self.dfs(to, t, min(upTo, cap))
                if d:
                    e[0] -= d
                    rev[0] += d
                    return d
            self.iter[v] += 1
        return 0

    def max_flow(self, s, t):
        flow = 0
        while self.bfs(s, t):
            self.iter = [0] * self.n
            f = self.dfs(s, t, INF)
            while f:
                flow += f
                f = self.dfs(s, t, INF)
        return flow

N = INT()
A = [input().strip() for _ in range(N)]
M = 26
C = Counter()
outdeg = [0] * M
indeg = [0] * M
for s in A:
    a, b = ord(s[0])-97, ord(s[-1])-97
    C[(a, b)] += 1
    outdeg[a] += 1
    indeg[b] += 1

size = M * 2
dinic = Dinic(size)
for x in range(M):
    dinic.add_edge(x, M + x, INF)
    for y in range(M):
        cap = C[(x, y)]
        if cap:
            dinic.add_edge(M + x, y, cap)

ans = [chr(x + 97) for x in range(M)
       if indeg[x] and dinic.max_flow(M + x, x) >= outdeg[x]]

print(*ans, sep='\n')