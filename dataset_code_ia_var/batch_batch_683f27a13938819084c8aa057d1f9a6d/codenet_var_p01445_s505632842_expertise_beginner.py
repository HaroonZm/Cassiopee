import collections

class MyList(list):
    def __init__(self, x=None):
        if x is None:
            x = []
        list.__init__(self, x)

    def __iadd__(self, other):
        result = []
        for a, b in zip(self, other):
            result.append(a + b)
        return MyList(result)

    def __isub__(self, other):
        result = []
        for a, b in zip(self, other):
            result.append(a - b)
        return MyList(result)

    def __gt__(self, other):
        for a, b in zip(self, other):
            if a != b:
                return a > b
        return False

class Edge:
    def __init__(self, to, cap, rev):
        self.to = to
        self.cap = cap
        self.rev = rev

class MaxFlow:
    def __init__(self, V, D):
        self.V = V
        self.D = D
        self.E = []
        for _ in range(V):
            self.E.append([])

    def zero(self):
        return MyList([0] * self.D)

    def add_edge(self, fr, to, cap):
        self.E[fr].append(Edge(to, cap, len(self.E[to])))
        self.E[to].append(Edge(fr, self.zero(), len(self.E[fr])-1))

    def dinic(self, source, sink):
        INF = MyList([10**9] * self.D)
        maxflow = self.zero()
        while True:
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

    def dfs(self, v, t, upTo):
        if v == t:
            return upTo
        for i in range(self.itr[v], len(self.E[v])):
            self.itr[v] = i
            e = self.E[v][i]
            if e.cap > self.zero() and self.level[v] < self.level[e.to]:
                if upTo > e.cap:
                    d = self.dfs(e.to, t, e.cap)
                else:
                    d = self.dfs(e.to, t, upTo)
                if d > self.zero():
                    e.cap = MyList([x - y for x, y in zip(e.cap, d)])
                    self.E[e.to][e.rev].cap = MyList([x + y for x, y in zip(self.E[e.to][e.rev].cap, d)])
                    return d
        return self.zero()

    def bfs(self, start):
        self.level = [-1] * self.V
        que = collections.deque()
        que.append(start)
        self.level[start] = 0
        while que:
            v = que.popleft()
            for e in self.E[v]:
                if e.cap > self.zero() and self.level[e.to] < 0:
                    self.level[e.to] = self.level[v] + 1
                    que.append(e.to)

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

def parse_poly(p):
    poly = MyList([0]*51)
    terms = p.split('+')
    for term in terms:
        term = term.strip()
        if 'x' not in term:
            num = int(term)
            poly[-1] = num
        else:
            if '^' in term:
                if term.startswith('x'):
                    a = 1
                    l = int(term.split('^')[1])
                else:
                    a, x = term.split('x')
                    if a == '':
                        a = 1
                    else:
                        a = int(a)
                    l = int(x.split('^')[1])
                poly[-(l+1)] = a
            else:
                if term == 'x':
                    poly[-2] = 1
                elif term.endswith('x'):
                    a = term[:-1]
                    if a == '':
                        a = 1
                    else:
                        a = int(a)
                    poly[-2] = a
                else:
                    a = term.split('x')[0]
                    if a == '':
                        a = 1
                    else:
                        a = int(a)
                    poly[-2] = a
    return poly

while True:
    try:
        line = input()
    except EOFError:
        break
    if not line.strip():
        continue
    N_and_M = list(map(int, line.strip().split()))
    if len(N_and_M) < 2:
        continue
    N, M = N_and_M
    if N == 0 and M == 0:
        break
    mf = MaxFlow(N, 51)
    for _ in range(M):
        parts = input().strip().split()
        u, v, p = parts[0], parts[1], ' '.join(parts[2:])
        u = int(u) - 1
        v = int(v) - 1
        poly = parse_poly(p)
        mf.add_edge(u, v, poly)
        mf.add_edge(v, u, poly)
    maxflow = mf.dinic(0, N-1)
    terms = []
    for a, l in zip(maxflow, reversed(range(51))):
        if a != 0:
            terms.append(to_poly(a, l))
    if terms:
        print('+'.join(terms))
    else:
        print(0)