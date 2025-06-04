import sys

def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
sys.setrecursionlimit(10 ** 9)
INF = 10 ** 18
MOD = 10 ** 9 + 7

class MinCostFlow:
    INF = 10 ** 18

    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self, fr, to, cap, cost):
        G = self.G
        G[fr].append([to, cap, cost, len(G[to])])
        G[to].append([fr, 0, -cost, len(G[fr])-1])

    def flow(self, s, t, f):
        from heapq import heappush, heappop

        N = self.N; G = self.G
        INF = MinCostFlow.INF

        res = 0
        H = [0] * N
        prv_v = [0] * N
        prv_e = [0] * N

        while f:
            dist = [INF] * N
            dist[s] = 0
            que = [(0, s)]

            while que:
                c, v = heappop(que)
                if dist[v] < c:
                    continue
                for i, (to, cap, cost, _) in enumerate(G[v]):
                    if cap > 0 and dist[to] > dist[v] + cost + H[v] - H[to]:
                        dist[to] = r = dist[v] + cost + H[v] - H[to]
                        prv_v[to] = v; prv_e[to] = i
                        heappush(que, (r, to))
            if dist[t] == INF:
                return INF

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

def compress(S):
    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S)):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped

N = INT()
S = set()
AB = []
for i in range(N):
    a, b = MAP()
    AB.append((a, b))
    S.add(a)
    S.add(b)

zipped, unzipped = compress(S)
M = len(zipped)
mcf = MinCostFlow(N+M+2)
s = N + M
t = N + M + 1
MAX = 10 ** 6
for i, (a, b) in enumerate(AB):
    mcf.add_edge(s, i, 1, 0)
    mcf.add_edge(i, N+zipped[a], 1, MAX-b)
    mcf.add_edge(i, N+zipped[b], 1, MAX-a)

mcf.add_edge(s, t, N, MAX)

for i in range(M):
    mcf.add_edge(N+i, t, 1, 0)

res = MAX * N - mcf.flow(s, t, N)
print(res)