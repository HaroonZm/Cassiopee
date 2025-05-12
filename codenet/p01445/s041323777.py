import sys
readline = sys.stdin.readline
write = sys.stdout.write
from string import digits

from collections import deque
class Dinic:
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def bfs(self, s, t):
        self.level = level = [None]*self.N
        deq = deque([s])
        level[s] = 0
        G = self.G
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        return level[t] is not None

    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        INF = 10**9 + 7
        G = self.G
        while self.bfs(s, t):
            *self.it, = map(iter, self.G)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow

def parse(S, L=50):
    S = S + "$"
    E = [0]*(L+1)
    cur = 0
    while 1:
        if S[cur] in digits:
            k = 0
            while S[cur] in digits:
                k = 10*k + int(S[cur])
                cur += 1 # '0' ~ '9'
        else:
            k = 1
        if S[cur] == 'x':
            cur += 1 # 'x'
            if S[cur] == '^':
                cur += 1 # '^'
                p = 0
                while S[cur] in digits:
                    p = 10*p + int(S[cur])
                    cur += 1 # '0' ~ '9'
            else:
                p = 1
        else:
            p = 0
        E[p] = k
        if S[cur] != '+':
            break
        cur += 1 # '+'
    return E

def solve():
    N, M = map(int, readline().split())
    if N == 0:
        return False
    L = 50
    ds = [Dinic(N) for i in range(L+1)]
    for i in range(M):
        u, v, p = readline().split()
        u = int(u)-1; v = int(v)-1
        poly = parse(p, L)
        for j in range(L+1):
            if poly[j] > 0:
                ds[j].add_multi_edge(u, v, poly[j], poly[j])
    INF = 10**9
    res = [0]*(L+1)
    for j in range(L+1):
        f = ds[j].flow(0, N-1)
        res[j] = f
    E = [[0]*N for i in range(N)]
    for j in range(L-1, -1, -1):
        d = ds[j]
        used = [0]*N
        used[N-1] = 1
        que = deque([N-1])
        G = ds[j+1].G
        for v in range(N):
            for w, cap, _ in G[v]:
                if cap:
                    E[v][w] = 1
        for v in range(N):
            for w in range(N):
                if E[v][w]:
                    d.add_edge(v, w, INF)
        f = d.flow(0, N-1)
        res[j] += f
    ans = []
    if res[0] > 0:
        ans.append(str(res[0]))
    if res[1] > 0:
        ans.append(("%dx" % res[1]) if res[1] > 1 else "x")
    for i in range(2, L+1):
        if res[i] > 0:
            ans.append(("%dx^%d" % (res[i], i)) if res[i] > 1 else ("x^%d" % i))
    if not ans:
        ans.append("0")
    ans.reverse()
    write("+".join(ans))
    write("\n")
    return True
while solve():
    ...