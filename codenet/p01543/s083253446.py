import sys

from heapq import heappush, heappop
class MinCostFlow:
    INF = 10**18

    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self, fr, to, cap, cost):
        G = self.G
        G[fr].append([to, cap, cost, len(G[to])])
        G[to].append([fr, 0, -cost, len(G[fr])-1])

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

def solve():
    readline = sys.stdin.readline
    write = sys.stdout.write

    N = int(readline())
    W = [list(map(int, readline().split())) for i in range(N)]
    E = [list(map(int, readline().split())) for i in range(N)]
    F = [readline() for i in range(N)]
    mcf = MinCostFlow(2*N+2)
    for i in range(N):
        Wi = W[i]; Ei = E[i]; Fi = F[i]
        s0 = sum(Ei[j] for j in range(N) if Fi[j] == "o")
        for j in range(N):
            s = (s0 - Ei[j] if Fi[j] == "o" else s0 + Wi[j])
            mcf.add_edge(i, N+j, 1, s)
        mcf.add_edge(2*N, i, 1, 0)
        mcf.add_edge(N+i, 2*N+1, 1, 0)
    res = mcf.flow(2*N, 2*N+1, N)
    write("%d\n" % res)
    ans = []
    for i in range(N):
        Gi = mcf.G[i]
        Wi = W[i]; Ei = E[i]; Fi = F[i]
        for j in range(N):
            if Gi[j][1] == 0:
                for k in range(N):
                    if j == k or Fi[k] == ".":
                        continue
                    ans.append("%d %d erase" % (i+1, k+1))
                if Fi[j] == ".":
                    ans.append("%d %d write" % (i+1, j+1))
                break
    write("%d\n" % len(ans))
    if ans:
        write("\n".join(ans))
        write("\n")
solve()