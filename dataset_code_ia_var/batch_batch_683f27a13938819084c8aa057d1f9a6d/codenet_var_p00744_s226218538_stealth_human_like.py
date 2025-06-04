import collections
import math

class Dinic:
    # Dinic algorithm, I hope I wrote this correctly... should find max-flow
    class Edge:
        def __init__(self, to, cap, rev):
            self.to = to
            self.cap = cap
            self.rev = rev  # Reverse edge index

    def __init__(self, V, adjlist, source, sink):
        self.V = V
        self.graph = [[] for _ in range(V)]
        # Build the network; not so pretty but does the job
        for u in range(V):
            for t in adjlist[u]:
                if isinstance(t, tuple):
                    v, c = t
                else:
                    v, c = t, 1  # Fallback just in case?
                self.graph[u].append(self.Edge(v, c, len(self.graph[v])))
                self.graph[v].append(self.Edge(u, 0, len(self.graph[u])-1))
        # Kick off the Dinic routine right away
        self.maxflow = self._dinic(source, sink)

    def _dinic(self, src, snk):
        INF = float('inf')
        flow = 0
        while True:
            self._bfs(src)
            if self.level[snk] < 0:
                return flow
            self.iter = [0] * self.V
            while True:
                f = self._dfs(src, snk, INF)
                if f > 0:
                    flow += f
                else:
                    break

    def _dfs(self, v, t, up):
        if v == t:
            return up
        # okay, iter-style might be better but whatever
        for idx in range(self.iter[v], len(self.graph[v])):
            self.iter[v] = idx
            e = self.graph[v][idx]
            if e.cap > 0 and self.level[v] < self.level[e.to]:
                d = self._dfs(e.to, t, min(up, e.cap))
                if d > 0:
                    e.cap -= d
                    self.graph[e.to][e.rev].cap += d
                    return d
        return 0  # dead end

    def _bfs(self, start):
        q = collections.deque()
        self.level = [-1] * self.V
        q.append(start)
        self.level[start] = 0
        # Setup levels
        while q:
            u = q.popleft()
            for e in self.graph[u]:
                if e.cap > 0 and self.level[e.to] < 0:
                    self.level[e.to] = self.level[u] + 1
                    q.append(e.to)

while True:
    try:
        M, N = map(int, input().split())
    except:  # probably EOF
        break
    if M == 0 and N == 0:
        break
    blue = []
    red = []
    # Read blue (again, maybe too verbose)
    while len(blue) < M:
        blue += [int(x) for x in input().split()]
    while len(red) < N:
        red += [int(x) for x in input().split()]

    V = M + N + 2  # vertices: blue, red, src, sink
    adj = [set() for _ in range(V)]

    # Build the edges (should maybe be faster, but ok)
    for i, b in enumerate(blue):
        if b != 1:
            for j, r in enumerate(red):
                if r % b == 0:
                    adj[i].add((M + j, 1))
        # Probably overkill with sqrt(b) but oh well
        for div in range(2, int(math.sqrt(b)) + 1):
            if b % div == 0:
                partner = b // div
                for k, r in enumerate(red):
                    if r % div == 0 or r % partner == 0:
                        adj[i].add((M + k, 1))

    # Connect source to all blue
    for i in range(M):
        adj[M + N].add((i, 1))
    # Connect all red to sink
    for j in range(N):
        adj[M + j].add((M + N + 1, 1))

    d = Dinic(V, adj, M + N, M + N + 1)
    print(d.maxflow)