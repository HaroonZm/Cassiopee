from collections import deque
from math import isqrt

class Dinic:
    __slots__ = 'V', 'E', 'level', 'itr', 'maxflow'
    class Edge:
        __slots__ = 'to', 'cap', 'rev'
        def __init__(self, to, cap, rev):
            self.to = to; self.cap = cap; self.rev = rev

    def __init__(self, V, edge_lists, source, sink):
        self.V = V
        self.E = [[] for _ in range(V)]
        for u, edges in enumerate(edge_lists):
            for v, c in edges:
                self.E[u].append(e := self.Edge(v, c, len(self.E[v])))
                self.E[v].append(self.Edge(u, 0, len(self.E[u])-1))
        self.maxflow = self._dinic(source, sink)

    def _dinic(self, s, t):
        INF = float('inf')
        flow = 0
        while self._bfs(s, t):
            self.itr = [0]*self.V
            while True:
                f = self._dfs(s, t, INF)
                if not f: break
                flow += f
        return flow

    def _dfs(self, v, t, upTo):
        if v == t: return upTo
        E, level, itr = self.E, self.level, self.itr
        for i in range(itr[v], len(E[v])):
            itr[v] = i
            e = E[v][i]
            if e.cap > 0 and level[v] < level[e.to]:
                d = self._dfs(e.to, t, min(upTo, e.cap))
                if d:
                    e.cap -= d
                    E[e.to][e.rev].cap += d
                    return d
        return 0

    def _bfs(self, s, t):
        self.level = lvl = [-1]*self.V
        lvl[s] = 0
        queue = deque([s])
        while queue:
            v = queue.popleft()
            for e in self.E[v]:
                if e.cap > 0 and lvl[e.to] == -1:
                    lvl[e.to] = lvl[v] + 1
                    queue.append(e.to)
        return lvl[t] != -1

def readints():
    while True:
        yield from map(int, input().split())

input_iter = readints()
while True:
    M, N = next(input_iter), next(input_iter)
    if M == 0 and N == 0: break
    blue = [next(input_iter) for _ in range(M)]
    red  = [next(input_iter) for _ in range(N)]
    V, src, sink = M+N+2, M+N, M+N+1
    edges = [set() for _ in range(V)]

    for i, b in enumerate(blue):
        if b > 1:
            for j, r in enumerate(red):
                if r % b == 0: edges[i].add((M+j, 1))
        limit = isqrt(b)
        for j in range(2, limit+1):
            if b % j == 0:
                for k, r in enumerate(red):
                    if r % j == 0 or r % (b//j) == 0:
                        edges[i].add((M+k, 1))
    for i in range(M): edges[src].add((i, 1))
    for j in range(N): edges[M+j].add((sink, 1))
    dinic = Dinic(V, edges, src, sink)
    print(dinic.maxflow)