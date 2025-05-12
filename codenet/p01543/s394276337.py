import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import time,random

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
mod2 = 998244353
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def pe(s): return print(str(s), file=sys.stderr)
def JA(a, sep): return sep.join(map(str, a))
def JAA(a, s, t): return s.join(t.join(map(str, b)) for b in a)

class Edge():
    def __init__(self,t,f,r,ca,co):
        self.to = t
        self.fron = f
        self.rev = r
        self.cap = ca
        self.cost = co

    def __str__(self):
        return f"Edge[{self.fron}, {self.to}, {self.rev}, {self.cap}, {self.cost}]"

class MinCostFlow():
    size = 0
    graph = []

    def __init__(self, s):
        self.size = s
        self.graph = [[] for _ in range(s)]

    def add_edge(self, f, t, ca, co):
        self.graph[f].append(Edge(t, f, len(self.graph[t]), ca, co))
        self.graph[t].append(Edge(f, t, len(self.graph[f])-1, 0, -co))

    def min_path(self, s, t):
        dist = [inf] * self.size
        route = [None] * self.size
        que = collections.deque()
        inq = [False] * self.size
        dist[s] = 0
        que.append(s)
        inq[s] = True
        while que:
            u = que.popleft()
            inq[u] = False
            for e in self.graph[u]:
                if e.cap == 0:
                    continue
                v = e.to
                if dist[v] > dist[u] + e.cost:
                    dist[v] = dist[u] + e.cost
                    route[v] = e
                    if not inq[v]:
                        que.append(v)
                        inq[v] = True

        if dist[t] == inf:
            return inf, 0

        flow = inf
        v = t
        while v != s:
            e = route[v]
            if flow > e.cap:
                flow = e.cap
            v = e.fron

        c = 0
        v = t
        while v != s:
            e = route[v]
            e.cap -= flow
            self.graph[e.to][e.rev].cap += flow
            c += e.cost * flow
            v = e.fron

        return dist[t], flow

    def calc_min_cost_flow(self, s, t, flow):
        total_cost = 0
        while flow > 0:
            c,f = self.min_path(s, t)
            if f == 0:
                return inf
            f = min(flow, f)
            total_cost += c * f
            flow -= f

        return total_cost

def main():
    n = I()
    wa = [LI() for _ in range(n)]
    ea = [LI() for _ in range(n)]
    fa = [[c == 'o' for c in S()] for _ in range(n)]

    s = n*2
    t = n*2 + 1
    mf = MinCostFlow(n*2+2)
    for i in range(n):
        mf.add_edge(s,i,1,0)
        mf.add_edge(i+n,t,1,0)
        fs = set([j for j in range(n) if fa[i][j]])
        fc = sum([ea[i][j] for j in fs])
        for j in range(n):
            if j in fs:
                mf.add_edge(i,j+n,1,fc-ea[i][j])
            else:
                mf.add_edge(i,j+n,1,fc+wa[i][j])

    r = mf.calc_min_cost_flow(s,t,n)
    ra = [[False]*n for _ in range(n)]
    for gr in mf.graph:
        for g in gr:
            if g.fron >= n or g.cap > 0:
                continue
            ra[g.fron][g.to-n] = True

    rr = []
    for i in range(n):
        for j in range(n):
            if fa[i][j] == ra[i][j]:
                continue
            if fa[i][j]:
                rr.append("{} {} erase".format(i+1, j+1))
            else:
                rr.append("{} {} write".format(i+1, j+1))

    return JA([r, len(rr)] + rr, "\n")

# start = time.time()
print(main())
# pe(time.time() - start)