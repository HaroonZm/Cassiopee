import collections
import sys

# python2 compat stuff, not really needed anymore?
if sys.version_info[0] == 2:
    input = raw_input
    range = xrange

class MyList(list):  # subclassing list, unsure if this is ideal
    def __init__(self, x=[]):
        list.__init__(self, x)

    def __iadd__(self, A):
        # I feel like this should mutate self instead of returning a new object, but leaving it
        return MyList([a + b for a, b in zip(self, A)])

    def __isub__(self, A):
        return MyList([a - b for a, b in zip(self, A)])

    def __gt__(self, A):
        for a, b in zip(self, A):
            if a != b:
                return a > b
        return False

class MaxFlow:
    """Dinic's algorithm - not the prettiest implementation but works
    Probably not the best complexity due to the lists of polynomials.
    """

    class Edge:
        def __init__(self, to, cap, rev):
            self.to = to
            self.cap = cap
            self.rev = rev

    def __init__(self, V, D):
        self.V = V
        self.E = []
        for i in range(V):
            self.E.append([])
        self.D = D

    def zero(self):
        # helper for a zero-array of length D, kind of ugly
        return MyList([0]*self.D)

    def add_edge(self, fr, to, cap):
        self.E[fr].append(self.Edge(to, cap, len(self.E[to])))
        self.E[to].append(self.Edge(fr, self.zero(), len(self.E[fr])-1))

    def dinic(self, source, sink):
        INF = MyList([10**9]*self.D)
        maxflow = self.zero()
        while 1:
            self.bfs(source)
            if self.level[sink] < 0:
                return maxflow
            self.itr = MyList([0] * self.V)
            while True:
                flow = self.dfs(source, sink, INF)
                if flow > self.zero():
                    maxflow += flow
                else:
                    break

    def dfs(self, v, t, flow):
        if v == t:
            return flow
        for i in range(self.itr[v], len(self.E[v])):
            self.itr[v] = i
            e = self.E[v][i]
            if e.cap > self.zero() and self.level[v] < self.level[e.to]:
                d = flow
                if flow > e.cap:
                    d = e.cap
                d = self.dfs(e.to, t, d)
                if d > self.zero():
                    e.cap -= d
                    self.E[e.to][e.rev].cap += d
                    return d
        return self.zero()

    def bfs(self, st):
        que = collections.deque()
        self.level = [-1]*self.V
        self.level[st] = 0
        que.append(st)
        while len(que) > 0:
            fr = que.popleft()
            for e in self.E[fr]:
                if e.cap > self.zero() and self.level[e.to] < 0:
                    self.level[e.to] = self.level[fr]+1
                    que.append(e.to)

def to_poly(a, l):
    # convert coefficient+degree to string, not perfect for negatives or edge cases maybe
    if l == 0:
        return str(a)
    if l == 1:
        return "{}x".format("" if a==1 else a)
    return "{}x^{}".format("" if a==1 else a, l)

while True:
    try:
        N, M = map(int, input().split())
    except Exception:
        break
    if N == 0 and M == 0:
        break
    mf = MaxFlow(N, 51)
    for i in range(M):
        u, v, p = input().split()
        u = int(u)-1
        v = int(v)-1
        poly = MyList([0]*51)
        for term in p.split('+'):
            try:
                num = int(term)
                poly[-1] = num
            except:
                num, *x = term.split('x')
                a = int(num) if num else 1
                if x:
                    if '^' in term:
                        deg = int(term.split('^')[1])
                        poly[-deg-1] = a
                    else:
                        poly[-2] = a
        mf.add_edge(u, v, poly)
        mf.add_edge(v, u, poly)
    maxflow = mf.dinic(0, N-1)
    result = []
    for a, l in zip(maxflow, reversed(range(51))):
        if a:
            result.append(to_poly(a, l))
    if result:
        print('+'.join(result))
    else:
        print(0)