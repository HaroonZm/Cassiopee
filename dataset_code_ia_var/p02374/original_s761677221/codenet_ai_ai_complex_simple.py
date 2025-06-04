import operator, itertools, functools, collections, bisect, heapq, types, sys

class Edge:
    __slots__ = 'v', 'w'
    def __init__(self, v, w):
        self.v, self.w = v, w
    def __iter__(self):
        return iter((self.v, self.w))
    def either(self): return (lambda: self.v)()
    def other(self, x): return self.w if x == self.v else self.v if x == self.w else (1//0)

class Graph:
    def __init__(self, v):
        self.v = v
        self._edges = [collections.deque() for _ in range(v)]
    def add(self, e):
        (lambda x:self._edges[e.v].append(e) or self._edges[e.w].append(e))(e)
    def adj(self, v):
        return map(lambda e: e, list(self._edges[v]))
    def edges(self):
        return (e for es in self._edges for e in es)

class RAQ:
    def __init__(self, n, initial=0):
        self.N = functools.reduce(lambda x,_: x<<1, range((n-1).bit_length()), 1)
        self.size = self.N*2-1
        self.seg = [initial]*self.size
    def add(self, l, r, val):
        stack = [(0,0,self.N-1)]
        actions = []
        while stack:
            k, s, t = stack.pop()
            if r < s or t < l: continue
            if l <= s and t <= r: actions.append((k,val))
            else:
                m = (s+t)//2
                stack.extend([(2*k+1,s,m),(2*k+2,m+1,t)])
        for idx,v in actions: self.seg[idx] += v
    def get(self, i):
        idx, s, t, v = 0, 0, self.N-1, 0
        while True:
            v += self.seg[idx]
            if s == t: return v
            m = (s+t)//2
            if i <= m: idx,s,t = 2*idx+1,s,m
            else: idx,s,t = 2*idx+2,m+1,t

class PathSum:
    def __init__(self, graph, root):
        self.__map = {}
        self.seg = RAQ(graph.v)
        self._in = [None]*graph.v
        self._out = [None]*graph.v
        self._dfs(graph, root)
    def _dfs(self, g, r):
        freezing = [r]
        visited = [0]*g.v
        time = [0]
        parent = [-1]*g.v
        while freezing:
            v = freezing.pop()
            if not visited[v]:
                self._in[v] = time[0]
                visited[v] = 1
                freezing.append(v)
                for e in reversed(list(g.adj(v))):
                    w = e.other(v)
                    if not visited[w]: parent[w]=v; freezing.append(w)
                time[0] += 1
            elif self._out[v] is None:
                self._out[v] = time[0]-1
    def add(self, v, val):
        self.seg.add(self._in[v], self._out[v], val)
    def get(self, v):
        return self.seg.get(self._in[v])

def run():
    def ints(): return list(map(int, sys.stdin.readline().split()))
    n = int(sys.stdin.readline())
    g = Graph(n)
    for i in range(n):
        arr = ints()
        if arr[0]>0:
            for j in arr[1:]:
                g.add(Edge(i,j))
    raq = PathSum(g, 0)
    q = int(sys.stdin.readline())
    for _ in range(q):
        arr = ints()
        if arr[0]==0: raq.add(arr[1], arr[2])
        elif arr[0]==1: print(raq.get(arr[1]))
        else: (lambda: (_ for _ in ()).throw(ValueError('invalid command')))()
if __name__ == '__main__': run()