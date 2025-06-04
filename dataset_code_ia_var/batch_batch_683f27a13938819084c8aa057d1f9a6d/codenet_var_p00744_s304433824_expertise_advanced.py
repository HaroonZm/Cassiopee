import math
from collections import deque

class MaxFlow:
    class Edge:
        __slots__ = 'to', 'cap', 'rev'
        def __init__(self, to, cap, rev):
            self.to, self.cap, self.rev = to, cap, rev

    def __init__(self, n, inf=float('inf')):
        self.n = n
        self.inf = inf
        self.level = [0] * n
        self.iter = [0] * n
        self.graph = [[] for _ in range(n)]

    def add_edge(self, u, v, cap):
        self.graph[u].append(self.Edge(v, cap, len(self.graph[v])))
        self.graph[v].append(self.Edge(u, 0, len(self.graph[u])-1))

    def bfs(self, s, t):
        level = self.level
        for i in range(self.n): level[i] = -1
        q = deque([s])
        level[s] = 0
        while q:
            v = q.popleft()
            for e in self.graph[v]:
                if e.cap and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    q.append(e.to)
        return level[t] != -1

    def dfs(self, v, t, upTo):
        if v == t: return upTo
        graph_v = self.graph[v]
        level = self.level
        iter_ = self.iter
        for i in range(iter_[v], len(graph_v)):
            e = graph_v[i]
            if e.cap and level[v] < level[e.to]:
                d = self.dfs(e.to, t, min(upTo, e.cap))
                if d:
                    e.cap -= d
                    self.graph[e.to][e.rev].cap += d
                    return d
            iter_[v] += 1
        return 0

    def compute(self, s, t):
        flow = 0
        while self.bfs(s, t):
            iter_ = self.iter
            for i in range(self.n): iter_[i] = 0
            while (f := self.dfs(s, t, self.inf)):
                flow += f
        return flow

def read_numbers(n):
    res = []
    while len(res) < n:
        res += map(int, input().split())
    return res

def main():
    import sys
    input = sys.stdin.readline
    while True:
        n, m = map(int, input().split())
        if n == 0: break
        a = read_numbers(n)
        b = read_numbers(m)
        size = n + m + 2
        s, t = n + m, n + m + 1
        mf = MaxFlow(size)
        for i in range(n):
            for j in range(m):
                if math.gcd(a[i], b[j]) != 1:
                    mf.add_edge(i, j + n, 1)
        for i in range(n):
            mf.add_edge(s, i, 1)
        for j in range(m):
            mf.add_edge(j + n, t, 1)
        print(mf.compute(s, t))

if __name__ == '__main__':
    main()