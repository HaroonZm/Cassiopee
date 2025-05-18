from string import ascii_lowercase, ascii_uppercase
import sys
readline = sys.stdin.readline
write = sys.stdout.write

from heapq import heappush, heappop
class MinCostFlow:
    INF = 10**100

    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]
        self.D = {}

    def add_edge(self, fr, to, cap, cost):
        G = self.G
        G[fr].append([to, cap, cost, len(G[to])])
        G[to].append([fr, 0, -cost, len(G[fr])-1])
        self.D[fr, to] = G[fr][-1]
        self.D[to, fr] = G[to][-1]

    def flow(self, s, t, f):
        N = self.N; G = self.G
        INF = MinCostFlow.INF

        res = 0
        H = [0]*N
        prv_v = [0]*N
        prv_e = [0]*N

        while f:
            dist = [INF]*N
            dist[s] = 0
            que = [(0, s)]

            while que:
                c, v = heappop(que)
                if dist[v] < c:
                    continue
                for i, (w, cap, cost, _) in enumerate(G[v]):
                    if cap > 0 and dist[w] > dist[v] + cost + H[v] - H[w]:
                        dist[w] = r = dist[v] + cost + H[v] - H[w]
                        prv_v[w] = v; prv_e[w] = i
                        heappush(que, (r, w))
            if dist[t] == INF:
                return -1

            for i in range(N):
                H[i] += dist[i]

            d = f; v = t
            while v != s:
                d = min(d, G[prv_v[v]][prv_e[v]][1])
                v = prv_v[v]
            f -= d
            res += d * H[t]
            v = t
            while v != s:
                e = G[prv_v[v]][prv_e[v]]
                e[1] -= d
                G[v][e[3]][1] += d
                v = prv_v[v]
        return res

cs = ascii_uppercase + ascii_lowercase
L = len(cs)
def solve():
    N = int(readline())

    g = N*2
    mcf = MinCostFlow(N*2+2)
    for i in range(N):
        mcf.add_edge(g, i, 1, 0)
        mcf.add_edge(N+i, g+1, 1, 0)

    S = []
    for i in range(N):
        *Si, = map(cs.index, readline().strip())
        for j in range(N):
            mcf.add_edge(i, j+N, 1, -L**(L-Si[j]))
        S.append(Si)

    mcf.flow(g, g+1, N)
    ans = []
    for i in range(N):
        Si = S[i]
        for j in range(N):
            if mcf.D[i, j+N][1] == 0:
                ans.append(Si[j])
    ans.sort()

    write("".join(map(cs.__getitem__, ans)))
    write("\n")
solve()