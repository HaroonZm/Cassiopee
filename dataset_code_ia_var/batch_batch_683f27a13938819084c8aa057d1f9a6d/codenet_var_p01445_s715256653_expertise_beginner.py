import collections

class SimpleList(list):
    def __init__(self, values=[]):
        list.__init__(self, values)
    def __iadd__(self, other):
        return SimpleList([a + b for a, b in zip(self, other)])
    def __isub__(self, other):
        return SimpleList([a - b for a, b in zip(self, other)])
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

    def __init__(self, n, d):
        self.n = n
        self.d = d
        self.graph = [[] for _ in range(n)]

    def zero(self):
        return SimpleList([0] * self.d)

    def add_edge(self, fr, to, cap):
        self.graph[fr].append(MaxFlow.Edge(to, cap, len(self.graph[to])))
        self.graph[to].append(MaxFlow.Edge(fr, self.zero(), len(self.graph[fr])-1))

    def dinic(self, s, t):
        maxflow = self.zero()
        while True:
            self.bfs(s)
            if self.level[t] < 0:
                return maxflow
            self.iter = [0] * self.n
            while True:
                flow = self.dfs(s, t, SimpleList([10**9]*self.d))
                if flow > self.zero():
                    maxflow += flow
                else:
                    break

    def dfs(self, v, t, upTo):
        if v == t:
            return upTo
        while self.iter[v] < len(self.graph[v]):
            i = self.iter[v]
            self.iter[v] += 1
            e = self.graph[v][i]
            if e.cap > self.zero() and self.level[v] < self.level[e.to]:
                mincap = e.cap
                if upTo > mincap:
                    d = self.dfs(e.to, t, mincap)
                else:
                    d = self.dfs(e.to, t, upTo)
                if d > self.zero():
                    e.cap -= d
                    self.graph[e.to][e.rev].cap += d
                    return d
        return self.zero()

    def bfs(self, s):
        self.level = [-1] * self.n
        queue = collections.deque()
        queue.append(s)
        self.level[s] = 0
        while queue:
            v = queue.popleft()
            for e in self.graph[v]:
                if e.cap > self.zero() and self.level[e.to] < 0:
                    self.level[e.to] = self.level[v] + 1
                    queue.append(e.to)

def poly_to_str(a, l):
    if l == 0:
        return str(a)
    elif l == 1:
        if a == 1:
            return 'x'
        else:
            return '{}x'.format(a)
    else:
        if a == 1:
            return 'x^{}'.format(l)
        else:
            return '{}x^{}'.format(a, l)

while True:
    line = input()
    N, M = map(int, line.split())
    if N == 0 and M == 0:
        break
    mf = MaxFlow(N, 51)
    for i in range(M):
        u, v, p = input().split()
        u = int(u) - 1
        v = int(v) - 1
        poly = SimpleList([0]*51)
        polys = p.split('+')
        for monom in polys:
            if 'x' not in monom:
                poly[-1] = int(monom)
            else:
                if '^' in monom:
                    if monom[0] == 'x':
                        a = 1
                        l = int(monom.split('^')[1])
                    else:
                        a, xdegree = monom.split('x')
                        a = int(a) if a not in ('', '+') else 1
                        l = int(xdegree.replace('^',''))
                    poly[-l-1] = a
                elif monom.endswith('x'):
                    if monom == 'x':
                        a = 1
                    else:
                        a = int(monom[:-1]) if monom[:-1] else 1
                    poly[-2] = a
        mf.add_edge(u, v, poly)
        mf.add_edge(v, u, poly)
    maxf = mf.dinic(0, N-1)
    result = []
    for a, l in zip(maxf, reversed(range(51))):
        if a:
            result.append(poly_to_str(a, l))
    if result:
        print('+'.join(result))
    else:
        print(0)