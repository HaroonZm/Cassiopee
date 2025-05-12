# https://atcoder.jp/contests/practice2/submissions/16805552 から拝借
# https://atcoder.jp/contests/acl1/submissions/16916932 を書き直し

import heapq

class mcf_graph_int_cost:
    """
    頂点数、及び、costの総和が、4294967295 (== (1 << 32) - 1) を超えない前提下での高速な実装。
    後者は超えても一応動く。
    """

    def __init__(self, n):
        self.n = n
        self.pos = []
        self.g = [[] for _ in range(n)]

    def add_edge(self, from_, to, cap, cost):
        # assert 0 <= from_ < self.n
        # assert 0 <= to < self.n
        m = len(self.pos)
        self.pos.append((from_, len(self.g[from_])))
        self.g[from_].append(self.__class__._edge(to, len(self.g[to]), cap, cost))
        self.g[to].append(self.__class__._edge(from_, len(self.g[from_]) - 1, 0, -cost))
        return m

    class edge:
        def __init__(self, from_, to, cap, flow, cost):
            self.from_ = from_
            self.to = to
            self.cap = cap
            self.flow = flow
            self.cost = cost

    def get_edge(self, i):
        _e = self.g[self.pos[i][0]][self.pos[i][1]]
        _re = self.g[_e.to][_e.rev]
        return self.__class__.edge(self.pos[i][0], _e.to, _e.cap + _re.cap, _re.cap, _e.cost)

    def edges(self):
        ret = []
        for i in range(len(self.pos)):
            _e = self.g[self.pos[i][0]][self.pos[i][1]]
            _re = self.g[_e.to][_e.rev]
            ret.append(self.__class__.edge(self.pos[i][0], _e.to, _e.cap + _re.cap, _re.cap, _e.cost))
        return ret

    def _dual_ref(self):
            self.dist = [4294967295] * self.n
            self.pv = [-1] * self.n
            self.pe = [-1] * self.n
            self.vis = [False] * self.n

            que = [s]
            self.dist[s] = 0
            while que:
                v = heapq.heappop(que) & 4294967295
                if self.vis[v]:
                    continue
                self.vis[v] = True
                if v == t:
                    break
                for i in range(len(self.g[v])):
                    e = self.g[v][i]
                    if self.vis[e.to] or e.cap == 0:
                        continue
                    cost = e.cost - self.dual[e.to] + self.dual[v]
                    if self.dist[e.to] > self.dist[v] + cost:
                        self.dist[e.to] = self.dist[v] + cost
                        self.pv[e.to] = v
                        self.pe[e.to] = i
                        heapq.heappush(que, ((self.dist[e.to] << 32) + e.to))
            if not self.vis[t]:
                return False

            for v in range(self.n):
                if not self.vis[v]:
                    continue
                self.dual[v] -= self.dist[t] - self.dist[v]
            
            return True

    def slope(self, s, t, flow_limit=4294967295):
        # assert 0 <= s < self.n
        # assert 0 <= t < self.n
        # assert s != t
        
        self.dual = [0] * self.n
        self.dist = [4294967295] * self.n
        self.pv = [-1] * self.n
        self.pe = [-1] * self.n
        self.vis = [False] * self.n

        
        flow = 0
        cost = 0
        prev_cost = -1
        result = [(flow, cost)]
        while flow < flow_limit:
            if not self._dual_ref():
                break
            c = flow_limit - flow
            v = t
            while v != s:
                c = min(c, self.g[self.pv[v]][self.pe[v]].cap)
                v = self.pv[v]
            v = t
            while v != s:
                e = self.g[self.pv[v]][self.pe[v]]
                e.cap -= c
                self.g[v][e.rev].cap += c
                v = self.pv[v]
            d = -self.dual[s]
            flow += c
            cost += c * d
            if prev_cost == d:
                result.pop()
            result.append((flow, cost))
            prev_cost = cost
        return result

    def flow(self, s, t, flow_limit=4294967295):
        return self.slope(s, t, flow_limit)[-1]

    
    class _edge:
        def __init__(self, to, rev, cap, cost):
            self.to = to
            self.rev = rev
            self.cap = cap
            self.cost = cost

from collections import deque
N, M = map(int, input().split())
X = [[0 if a == "#" else 1 if a == "." else 2 for a in input()] for _ in range(N)]

def BFS(i0=0):
    Q = deque([i0])
    D = [-1] * (N * M)
    D[i0] = 0
    while Q:
        x = Q.popleft()
        i, j = x // M, x % M
        for di, dj in ((0, 1), (1, 0)):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if X[ni][nj]:
                    y = ni * M + nj
                    if D[y] == -1:
                        D[y] = D[x] + 1
                        Q.append(y)
    return D

E = []
ma = 0
for i in range(N):
    for j in range(M):
        if X[i][j] < 2: continue
        s = i * M + j
        b = BFS(s)
        for t in [a for a in range(N * M) if b[a] >= 0]:
            i2, j2 = t // M, t % M
            d = i2 - i + j2 - j
            ma = max(ma, d)
            E.append((s, t + N * M, d))
cnt = sum(sum([1 if a == 2 else 0 for a in x]) for x in X)

s = 2 * N * M
t = s + 1
g = mcf_graph_int_cost(t + 1)
for i in range(N):
    for j in range(M):
        if X[i][j] == 0: continue
        a = i*M+j+N*M
        if X[i][j] == 2:
            g.add_edge(s, i*M+j, 1, 0)
        g.add_edge(a, t, 1, 0)
for v, w, d in E:
    g.add_edge(v, w, 1, ma - d)

print(ma * cnt - g.flow(s, t, cnt)[1])