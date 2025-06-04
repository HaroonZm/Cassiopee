from collections import deque
from math import gcd

class Dinic:
    """Optimized Dinic's Algorithm for Max Flow (O(EV^2))"""
    __slots__ = ('V', 'graph', 'level', 'ptr')

    class Edge:
        __slots__ = ('to', 'cap', 'rev')
        def __init__(self, to, cap, rev):
            self.to = to
            self.cap = cap
            self.rev = rev

    def __init__(self, V, adj, source, sink):
        self.V = V
        self.graph = [[] for _ in range(V)]
        for fr, elist in enumerate(adj):
            for to, cap in elist:
                fwd = self.Edge(to, cap, len(self.graph[to]))
                bwd = self.Edge(fr, 0, len(self.graph[fr]))
                self.graph[fr].append(fwd)
                self.graph[to].append(bwd)
        self.maxflow = self._dinic(source, sink)

    def _bfs(self, s, t):
        self.level = [-1] * self.V
        self.level[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for e in self.graph[v]:
                if e.cap and self.level[e.to] < 0:
                    self.level[e.to] = self.level[v] + 1
                    q.append(e.to)
        return self.level[t] != -1

    def _dfs(self, v, t, upTo):
        if v == t or not upTo:
            return upTo
        for i in range(self.ptr[v], len(self.graph[v])):
            e = self.graph[v][i]
            if e.cap and self.level[v] < self.level[e.to]:
                pushed = self._dfs(e.to, t, min(upTo, e.cap))
                if pushed:
                    e.cap -= pushed
                    self.graph[e.to][e.rev].cap += pushed
                    return pushed
            self.ptr[v] += 1
        return 0

    def _dinic(self, s, t):
        flow, INF = 0, float('inf')
        while self._bfs(s, t):
            self.ptr = [0] * self.V
            while (pushed := self._dfs(s, t, INF)):
                flow += pushed
        return flow

def read_ints_until_size(size):
    data = []
    while len(data) < size:
        data += map(int, input().split())
    return data

while True:
    M, N = map(int, input().split())
    if not (M or N):
        break

    blue = read_ints_until_size(M)
    red = read_ints_until_size(N)
    V = M + N + 2
    adj = [[] for _ in range(V)]
    source, sink = V - 2, V - 1

    # Edges between blue and red nodes if not coprime
    for i, b in enumerate(blue):
        for j, r in enumerate(red):
            if gcd(b, r) != 1:
                adj[i].append((M + j, 1))
    # Source to blue
    for i in range(M):
        adj[source].append((i, 1))
    # Red to sink
    for j in range(N):
        adj[M + j].append((sink, 1))

    print(Dinic(V, adj, source, sink).maxflow)