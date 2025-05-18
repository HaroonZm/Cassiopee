import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)

class Edge():
    def __init__(self,t,f,r,ca,co):
        self.to = t
        self.fron = f
        self.rev = r
        self.cap = ca
        self.cost = co

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
            return inf

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

        return dist[t]

    def calc_min_cost_flow(self, s, t, flow):
        total_cost = 0
        for i in range(flow):
            c = self.min_path(s, t)
            if c == inf:
                return c
            total_cost += c

        return total_cost

def main():
    n = I()
    mcf = MinCostFlow(4096)
    s = 4094
    t = 4095
    for i in range(n):
        mcf.add_edge(s, i, 1, 0)
        mcf.add_edge(i, 4093, 1, 0)

    a = []
    b = []
    ss = set()
    for _ in range(n):
        ai,bi = LI()
        a.append(ai)
        b.append(bi)
        ss.add(ai)
        ss.add(bi)
    d = {}
    for i,v in zip(range(len(ss)), sorted(ss)):
        d[v] = i + n
        mcf.add_edge(i+n, t, 1, 0)
    mcf.add_edge(4093, t, inf, 0)
    for i in range(n):
        mcf.add_edge(i, d[a[i]], 1, -b[i])
        mcf.add_edge(i, d[b[i]], 1, -a[i])
    res = mcf.calc_min_cost_flow(s, t, n)
    return -res

print(main())