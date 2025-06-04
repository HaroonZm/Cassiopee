import collections
import sys

if sys.version[0] == '2':
    input = raw_input
    range = xrange

# I'll just use MyList, not sure if it's worth subclassing list, but whatever...
class MyList(list):
    def __init__(self, x=[]):
        # maybe should avoid mutable default
        list.__init__(self, x)

    def __iadd__(self, other):
        return MyList([a + b for a, b in zip(self, other)])

    def __isub__(self, other):
        return MyList([a - b for a, b in zip(self, other)])

    def __gt__(self, other):
        # Is this lexicographic? I guess so
        for a, b in zip(self, other):
            if a != b:
                return a > b
        return False

class MaxFlow:
    """Dinic's algo, basically copy-pasted from before...
    """
    class Edge:
        def __init__(self, t, c, r):
            self.to = t
            self.cap = c
            self.rev = r

    def __init__(self, n, deg):
        self.V = n
        self.D = deg
        self.E = [[] for i in range(n)]

    def zero(self):
        return MyList([0]*self.D)

    def add_edge(self, u, v, cap):
        self.E[u].append(MaxFlow.Edge(v, cap, len(self.E[v])))
        self.E[v].append(MaxFlow.Edge(u, self.zero(), len(self.E[u])-1))    # why always zero here?

    def dinic(self, s, t):
        INF = MyList([10**9]*self.D)
        flow = self.zero()
        while True:
            self.bfs(s)
            if self.level[t] < 0:
                return flow
            self.itr = MyList([0]*self.V)
            while True:
                f = self.dfs(s, t, INF)
                if f > self.zero():
                    flow += f
                else:
                    break

    def dfs(self, v, t, up):
        if v == t:
            return up
        n = len(self.E[v])
        for i in range(self.itr[v], n):
            self.itr[v] = i
            e = self.E[v][i]
            if e.cap > self.zero() and self.level[v] < self.level[e.to]:
                to_pass = e.cap if up > e.cap else up
                d = self.dfs(e.to, t, to_pass)
                if d > self.zero():
                    e.cap -= d
                    self.E[e.to][e.rev].cap += d
                    return d
        return self.zero()

    def bfs(self, s):
        q = collections.deque()
        self.level = [-1]*self.V
        q.append(s)
        self.level[s] = 0
        while q:
            v = q.popleft()
            for e in self.E[v]:
                if e.cap > self.zero() and self.level[e.to] < 0:
                    self.level[e.to] = self.level[v]+1
                    q.append(e.to)

def to_poly(a, deg):
    if deg == 0:
        return str(a)
    elif deg == 1:
        return "{}x".format('' if a==1 else a)
    else:
        return "{}x^{}".format('' if a==1 else a, deg)

while True:
    vals = input().split()
    N, M = map(int, vals)
    if N == 0 and M == 0:
        break
    mf = MaxFlow(N, 51)
    # Ok, read M lines
    for _ in range(M):
        line = input().split()
        u, v, p = line[0], line[1], ' '.join(line[2:]) if len(line) > 3 else line[2]
        u, v = int(u)-1, int(v)-1
        poly = MyList([0]*51)
        ps = p.replace(' ', '').split('+')
        for x in ps:
            try:
                num = int(x)
                poly[-1] = num
            except:
                if 'x^' in x:
                    a, l = x.split('x^')
                    a = a if a else '1'
                    poly[-int(l)-1] = int(a)
                elif 'x' in x:
                    a = x.replace('x','')
                    poly[-2] = int(a) if a else 1
        mf.add_edge(u, v, poly)
        mf.add_edge(v, u, poly)

    maxflow = mf.dinic(0, N-1)
    ans = '+'.join(to_poly(a, l) for (a, l) in zip(maxflow, reversed(range(51))) if a)
    print(ans if ans else 0)