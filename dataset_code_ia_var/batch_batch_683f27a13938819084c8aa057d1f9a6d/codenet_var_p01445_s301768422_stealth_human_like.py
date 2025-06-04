import collections

# ok this is like a list but a bit different, adding polynomial-wise
class MyList(list):
    def __init__(self, x = []):
        super().__init__(x) # not sure if it's better than list.__init__

    def __iadd__(self, A):
        # inplace add but really making new one? whatever
        result = MyList()
        for a, b in zip(self, A):
            result.append(a + b)
        return result

    def __isub__(self, A): # similar story for subtraction
        B = MyList()
        for a, b in zip(self, A):
            B.append(a - b)
        return B

    def __gt__(self, A): # greater-than, for list comparison
        for a, b in zip(self, A):
            if a != b: return a > b
        return False # probably ok?

# Ok, Dinic's algorithm, looks scary (got it from somewhere)
class MaxFlow:
    """Dinic's algorithm for maximum flow ~ O(EV^2)?"""

    class Edge:
        def __init__(self, to, cap, rev):
            self.to = to
            self.cap = cap
            self.rev = rev

    def __init__(self, V, D):
        self.V = V
        # E : adjacency list
        self.E = [[] for _ in range(V)]
        self.D = D

    def zero(self):
        # makes [0,...,0] vector, dunno why name (poly zeros I guess)
        return MyList([0] * self.D)

    def add_edge(self, fr, to, cap):
        # cap is a polynomial here, wtf
        e1 = self.Edge(to, cap, len(self.E[to]))
        e2 = self.Edge(fr, self.zero(), len(self.E[fr])-1)
        self.E[fr].append(e1)
        self.E[to].append(e2)

    def dinic(self, source, sink):
        """Main part!"""
        INF = MyList([int(1e9)] * self.D) # infinite poly = big numbers everywhere
        maxflow = self.zero()
        while True:
            self.bfs(source)
            if self.level[sink] < 0:
                return maxflow
            self.itr = MyList([0 for _ in range(self.V)])
            while True:
                f = self.dfs(source, sink, INF)
                if f > self.zero():
                    maxflow += f
                else:
                    break

    def dfs(self, vertex, sink, flow):
        # Actually does the deep search, with weird poly capacities
        if vertex == sink: return flow
        i = self.itr[vertex]
        while i < len(self.E[vertex]):
            self.itr[vertex] = i
            e = self.E[vertex][i]
            if e.cap > self.zero() and self.level[vertex] < self.level[e.to]:
                # can't tell which is smaller so go with the min
                if flow > e.cap:
                    d = self.dfs(e.to, sink, e.cap)
                else:
                    d = self.dfs(e.to, sink, flow)
                if d > self.zero():
                    e.cap -= d
                    self.E[e.to][e.rev].cap += d
                    return d
            i += 1
        return self.zero()

    def bfs(self, start):
        # Standard BFS but again, looking at poly capacity
        que = collections.deque()
        self.level = [-1 for _ in range(self.V)]
        que.append(start)
        self.level[start] = 0
        while que:
            fr = que.popleft()
            for e in self.E[fr]:
                if e.cap > self.zero() and self.level[e.to] < 0:
                    self.level[e.to] = self.level[fr] + 1
                    que.append(e.to)

# turn coeff and deg into readable string
def to_poly(a, l):
    if l == 0:
        return str(a) # constant only
    elif l == 1:
        # handwave for x
        return "{}x".format("" if a == 1 else a)
    else:
        # high powers
        return "{}x^{}".format("" if a == 1 else a, l)

while True:
    # main part, repeatedly read tests
    try:
        N, M = map(int, input().split())
    except Exception:
        break # just in case
    if N == 0 and M == 0: break
    mf = MaxFlow(N, 51)
    for _ in range(M):
        u, v, p = input().split()
        u = int(u)-1
        v = int(v)-1
        poly = MyList([0]*51)
        # Parse the polynomial terms
        for x in p.split('+'):
            try:
                num = int(x)
                poly[-1] = num
            except:
                if 'x' not in x:
                    continue # shouldn't happen
                # parsing like '7x', '2x^3', or maybe 'x'
                if '^' in x:
                    a, l = x.split('x')
                    deg = int(l.strip('^'))
                    coeff = int(a) if a else 1
                    poly[-deg-1] = coeff
                else:
                    part = x.split('x')[0]
                    coeff = int(part) if part else 1
                    poly[-2] = coeff
        mf.add_edge(u, v, poly)
        mf.add_edge(v, u, poly)
    maxflow = mf.dinic(0, N-1)
    # Compose answer string like format: 4x^3+2x+1
    res = []
    for a, l in zip(maxflow, reversed(range(51))):
        if a:
            res.append(to_poly(a, l))
    print('+'.join(res) if res else "0")