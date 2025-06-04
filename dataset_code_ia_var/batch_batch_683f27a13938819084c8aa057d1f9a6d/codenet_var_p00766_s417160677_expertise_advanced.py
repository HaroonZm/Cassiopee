from collections import deque
from itertools import product

class Dinic:
    __slots__ = ('n', 'g', 'level', 'it')

    class Edge:
        __slots__ = ('to', 'rev', 'cap')
        def __init__(self, to, rev, cap):
            self.to = to
            self.rev = rev
            self.cap = cap

    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add_edge(self, fr, to, cap):
        forward = self.Edge(to, len(self.g[to]), cap)
        backward = self.Edge(fr, len(self.g[fr]), 0)
        self.g[fr].append(forward)
        self.g[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        forward = self.Edge(v2, len(self.g[v2]), cap1)
        backward = self.Edge(v1, len(self.g[v1]), cap2)
        self.g[v1].append(forward)
        self.g[v2].append(backward)

    def bfs(self, s):
        level = [-1] * self.n
        level[s] = 0
        dq = deque([s])
        while dq:
            v = dq.popleft()
            for e in self.g[v]:
                if e.cap and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    dq.append(e.to)
        self.level = level

    def dfs(self, v, t, up):
        if v == t:
            return up
        for i in range(self.it[v], len(self.g[v])):
            e = self.g[v][i]
            if e.cap and self.level[v] < self.level[e.to]:
                d = self.dfs(e.to, t, min(up, e.cap))
                if d:
                    e.cap -= d
                    self.g[e.to][e.rev].cap += d
                    self.it[v] = i
                    return d
            self.it[v] = i+1
        return 0

    def max_flow(self, s, t):
        flow, INF = 0, 10**18
        while True:
            self.bfs(s)
            if self.level[t] < 0: break
            self.it = [0]*self.n
            while True:
                f = self.dfs(s, t, INF)
                if not f: break
                flow += f
        return flow

def parse_input():
    try:
        while True:
            h, w = map(int, input().split())
            if h == 0 and w == 0:
                break
            R = [input() for _ in range(h)]
            yield h, w, R
    except EOFError:
        return

for h, w, R in parse_input():
    P, Q = [], []
    dep = 0
    for i, j in product(range(h - 1), range(w - 1)):
        first, second = R[i][j:j+2], R[i+1][j:j+2]
        if (first == '.#' and second == '##') or (first == '##' and second == '.#'):
            k = j
            while k+1 < w and R[i][k+1] != '.' and R[i+1][k+1] != '.':
                k += 1
            if k+1 < w and (R[i][k+1] == '#' ) ^ (R[i+1][k+1] == '#'):
                P.append(((i, j), (i, k)))
        if first in ('.#', '#.') and second == '##':
            k = i
            while k+1 < h and R[k+1][j] != '.' and R[k+1][j+1] != '.':
                k += 1
            if k+1 < h and (R[k+1][j] == '#' ) ^ (R[k+1][j+1] == '#'):
                Q.append(((i, j), (k, j)))
        if first.count('#') + second.count('#') == 3:
            dep += 1

    N, M = len(P), len(Q)
    dinic = Dinic(2 + N + M)
    for pi in range(N):
        dinic.add_edge(0, pi+2, 1)
    for qi in range(M):
        dinic.add_edge(N+qi+2, 1, 1)
    Px = [(*p[0], *p[1]) for p in P]
    Qx = [(*q[0], *q[1]) for q in Q]
    for i, (r1, c1, r2, c2) in enumerate(Px):
        for j, (rr1, cc1, rr2, cc2) in enumerate(Qx):
            # If segments intersect
            if rr1 <= r1 <= rr2 and c2 <= cc1 <= c1:
                dinic.add_edge(i+2, N+j+2, 1)
    print(dep - (N + M - dinic.max_flow(0, 1)) + 1)