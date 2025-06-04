import sys

def input():
    return sys.stdin.readline().strip()
def list2d(a, b, c):
    return [[c] * b for _ in range(a)]
def list3d(a, b, c, d):
    return [[[d] * c for _ in range(b)] for _ in range(a)]
def list4d(a, b, c, d, e):
    return [[[[e] * d for _ in range(c)] for _ in range(b)] for _ in range(a)]
def ceil(x, y=1):
    return int(-(-x // y))
def INT():
    return int(input())
def MAP():
    return map(int, input().split())
def LIST(N=None):
    return list(MAP()) if N is None else [INT() for _ in range(N)]
def Yes():
    print('Yes')
def No():
    print('No')
def YES():
    print('YES')
def NO():
    print('NO')
sys.setrecursionlimit(10 ** 9)
INF = 10 ** 18
MOD = 10 ** 9 + 7

class MinCostFlow:
    INF = 10 ** 18

    def __init__(self, N):
        self.N = N
        self.G = [[] for _ in range(N)]

    def add_edge(self, fr, to, cap, cost):
        G = self.G
        G[fr].append([to, cap, cost, len(G[to])])
        G[to].append([fr, 0, -cost, len(G[fr]) - 1])

    def flow(self, s, t, f):
        N = self.N
        G = self.G
        INF = MinCostFlow.INF

        res = 0
        prv_v = [0] * N
        prv_e = [0] * N

        while f:
            dist = [INF] * N
            dist[s] = 0
            update = True

            while update:
                update = False
                for v in range(N):
                    if dist[v] == INF:
                        continue
                    for i, (to, cap, cost, _) in enumerate(G[v]):
                        if cap > 0 and dist[to] > dist[v] + cost:
                            dist[to] = dist[v] + cost
                            prv_v[to] = v
                            prv_e[to] = i
                            update = True
            if dist[t] == INF:
                return -1

            d = f
            v = t
            while v != s:
                d = min(d, G[prv_v[v]][prv_e[v]][1])
                v = prv_v[v]
            f -= d
            res += d * dist[t]
            v = t
            while v != s:
                e = G[prv_v[v]][prv_e[v]]
                e[1] -= d
                G[v][e[3]][1] += d
                v = prv_v[v]
        return res

def build_grid(H, W, intv, _type, space=True, padding=False):
    if space:
        _input = lambda: input().split()
    else:
        _input = lambda: input()
    _list = lambda: list(map(_type, _input()))
    if padding:
        offset = 1
    else:
        offset = 0
    grid = list2d(H + offset * 2, W + offset * 2, intv)
    for i in range(offset, H + offset):
        row = _list()
        for j in range(offset, W + offset):
            grid[i][j] = row[j - offset]
    return grid

N = INT()
write = build_grid(N, N, 0, int)
erase = build_grid(N, N, 0, int)
grid = build_grid(N, N, '', str, space=False)

mcf = MinCostFlow(N * 2 + 2)
s = N * 2
t = N * 2 + 1
erasesm = 0
for i in range(N):
    mcf.add_edge(s, i, 1, 0)
    mcf.add_edge(N + i, t, 1, 0)
    for j in range(N):
        if grid[i][j] == 'o':
            erasesm += erase[i][j]
            mcf.add_edge(i, N + j, 1, -erase[i][j])
        else:
            mcf.add_edge(i, N + j, 1, write[i][j])

res = erasesm + mcf.flow(s, t, N)
written = set()
for fr in range(N):
    for to, cap, cost, _ in mcf.G[fr]:
        if cap == 0 and N <= to < N * 2:
            written.add((fr, to - N))
            break

ans = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 'o' and (i, j) not in written:
            ans.append((i + 1, j + 1, 'erase'))
        if grid[i][j] == '.' and (i, j) in written:
            ans.append((i + 1, j + 1, 'write'))
print(res)
print(len(ans))
for i, j, s in ans:
    print(i, j, s)