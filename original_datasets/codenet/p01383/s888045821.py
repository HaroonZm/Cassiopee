import sys
from collections import defaultdict

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
    """ 最小費用流(ダイクストラ版)：O(F*E*logV) """

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

M, N, K = MAP()
A = LIST(N)
B = [b-1 for b in LIST(K)]

# 隣り合う同値を取り除いておく
B2 = [B[0]]
for i in range(1, K):
    if B[i-1] != B[i]:
        B2.append(B[i])
K2 = len(B2)

# 同じ値が次に出現する位置を調べておく
nxt = [INF] * K2
D = defaultdict(lambda: INF)
total = 0
for i in range(K2-1, -1, -1):
    b = B2[i]
    nxt[i] = D[b]
    D[b] = i
    total += A[b]

mcf = MinCostFlow(K2)
# 負コストを避けるための調整用
MAX = 10 ** 4
for i in range(K2-1):
    b = B2[i]
    # 残さない場合は利得0とする
    mcf.add_edge(i, i+1, M-1, MAX)
    j = nxt[i]
    if j != INF:
        # 残しておくと、残さない場合にかかるコスト分の利得があるとみなす
        mcf.add_edge(i+1, j, 1, MAX*(j-i-1) - A[b])

res = MAX*(K2-1)*(M-1) - mcf.flow(0, K2-1, M-1)
print(total - res)