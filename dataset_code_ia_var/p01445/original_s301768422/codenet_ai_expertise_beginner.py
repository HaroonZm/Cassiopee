import collections

class MyList(list):
    def __init__(self, x=[]):
        list.__init__(self, x)

    def __iadd__(self, other):
        result = MyList()
        for a, b in zip(self, other):
            result.append(a + b)
        return result

    def __isub__(self, other):
        result = MyList()
        for a, b in zip(self, other):
            result.append(a - b)
        return result

    def __gt__(self, other):
        for a, b in zip(self, other):
            if a != b:
                return a > b
        return False

class MaxFlow:
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
        return MyList([0]*self.D)

    def add_edge(self, fr, to, cap):
        self.E[fr].append(self.Edge(to, cap, len(self.E[to])))
        self.E[to].append(self.Edge(fr, self.zero(), len(self.E[fr])-1))

    def dinic(self, source, sink):
        INF = MyList([10**9]*self.D)
        maxflow = self.zero()
        while True:
            self.bfs(source)
            if self.level[sink] < 0:
                return maxflow
            self.itr = MyList([0]*self.V)
            while True:
                flow = self.dfs(source, sink, INF)
                if flow > self.zero():
                    maxflow += flow
                else:
                    break

    def dfs(self, v, t, upTo):
        if v == t:
            return upTo
        i = self.itr[v]
        while i < len(self.E[v]):
            self.itr[v] = i
            e = self.E[v][i]
            if e.cap > self.zero() and self.level[v] < self.level[e.to]:
                d = None
                if upTo > e.cap:
                    d = self.dfs(e.to, t, e.cap)
                else:
                    d = self.dfs(e.to, t, upTo)
                if d > self.zero():
                    e.cap -= d
                    self.E[e.to][e.rev].cap += d
                    return d
            i += 1
        return self.zero()

    def bfs(self, start):
        queue = collections.deque()
        self.level = [-1]*self.V
        queue.append(start)
        self.level[start] = 0
        while queue:
            v = queue.popleft()
            for e in self.E[v]:
                if e.cap > self.zero() and self.level[e.to] < 0:
                    self.level[e.to] = self.level[v] + 1
                    queue.append(e.to)

def to_poly(a, l):
    if l == 0:
        return str(a)
    elif l == 1:
        if a == 1:
            return "x"
        else:
            return "{}x".format(a)
    else:
        if a == 1:
            return "x^{}".format(l)
        else:
            return "{}x^{}".format(a, l)

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    mf = MaxFlow(N, 51)
    for _ in range(M):
        u, v, p = input().split()
        u = int(u) - 1
        v = int(v) - 1
        poly = MyList([0]*51)
        for x in p.split('+'):
            try:
                num = int(x)
                poly[-1] = num
            except ValueError:
                if 'x' in x:
                    if '^' in x:
                        a, l = x.split('x')
                        if a == '':
                            a = 1
                        else:
                            a = int(a)
                        l = int(l[1:])
                        poly[-l-1] = a
                    else:
                        a = x.replace('x','')
                        if a == '':
                            a = 1
                        else:
                            a = int(a)
                        poly[-2] = a
        mf.add_edge(u, v, poly)
        mf.add_edge(v, u, poly)
    maxflow = mf.dinic(0, N-1)
    output_terms = []
    for a, l in zip(maxflow, reversed(range(51))):
        if a:
            output_terms.append(to_poly(a, l))
    if output_terms:
        print('+'.join(output_terms))
    else:
        print(0)