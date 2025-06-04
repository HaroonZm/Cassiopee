import sys
from collections import deque

readline = sys.stdin.readline
write = sys.stdout.write

class Dinic:
    __slots__ = 'N', 'G', 'D', 'level', 'it'
    def __init__(self, N):
        self.N = N
        self.G = [[] for _ in range(N)]
        self.D = {}

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)
        self.D[(fr, to)] = forward

    def bfs(self, s, t):
        level = [-1] * self.N
        level[s] = 0
        dq = deque([s])
        while dq:
            v = dq.popleft()
            lv = level[v] + 1
            for w, cap, _ in self.G[v]:
                if cap and level[w] == -1:
                    level[w] = lv
                    dq.append(w)
        self.level = level
        return level[t] != -1

    def dfs(self, v, t, f):
        if v == t: return f
        for e in self.it[v]:
            w, cap, rev = e
            if cap and self.level[v] < self.level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow, INF = 0, 10 ** 9 + 7
        while self.bfs(s, t):
            self.it = [iter(adj) for adj in self.G]
            while (p := self.dfs(s, t, INF)):
                flow += p
        return flow

def solve():
    try:
        N, M, S, T = map(int, readline().split())
    except Exception:
        return False
    if N == M == 0:
        return False
    S -= 1
    T -= 1
    edges = []
    dinic = Dinic(N)
    for _ in range(M):
        a, b = map(int, readline().split())
        a -= 1
        b -= 1
        dinic.add_edge(a, b, 1)
        edges.append((a, b))

    f = dinic.flow(S, T)

    used = [0] * N
    dq = deque([S])
    used[S] = 1
    while dq:
        v = dq.popleft()
        for w, cap, _ in dinic.G[v]:
            if cap == 0 or used[w]:
                continue
            used[w] = 1
            dq.append(w)
    dq = deque([T])
    used[T] = 2
    while dq:
        v = dq.popleft()
        for w, cap, _ in dinic.G[v]:
            if cap > 0 or used[w]:
                continue
            used[w] = 2
            dq.append(w)
    cnt = sum(used[a] == 2 and used[b] == 1 for a, b in edges)
    write(f"{f + (cnt > 0)} {cnt if cnt else 0}\n")
    return True

while solve():
    pass