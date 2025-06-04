import collections
import fractions

class Dinic:
    # Bon, l'algo de Dinic pour le flot maximum (pas super intuitif)
    class Edge:
        def __init__(self, to, cap, rev):
            # pas besoin de doc là-dessus je crois
            self.to = to
            self.cap = cap
            self.rev = rev

    def __init__(self, n, adj, source, sink):
        # n : nb de sommets
        # adj : liste d'adjacence (j'espère bien formée)
        self.n = n
        self.graph = [[] for _ in range(n)]
        for from_ in range(n):
            for to, cap in adj[from_]:
                self.graph[from_].append(self.Edge(to, cap, len(self.graph[to])))
                self.graph[to].append(self.Edge(from_, 0, len(self.graph[from_])-1))
        self.maxflow = self.dinic(source, sink)

    def dinic(self, s, t):
        result = 0
        INF = float('inf')
        while True:
            self.bfs(s)
            if self.level[t] < 0:
                return result
            self.it = [0] * self.n
            while True:
                f = self.dfs(s, t, INF)
                if f > 0:
                    result += f
                else:
                    break

    def dfs(self, v, t, f):
        # ici on va chercher un chemin pouvant être amélioré (je déteste la récursivité)
        if v == t:
            return f
        for i in range(self.it[v], len(self.graph[v])):
            self.it[v] = i
            e = self.graph[v][i]
            if e.cap > 0 and self.level[v] < self.level[e.to]:
                d = self.dfs(e.to, t, min(f, e.cap))
                if d > 0:
                    e.cap -= d
                    self.graph[e.to][e.rev].cap += d
                    return d
        return 0

    def bfs(self, start):
        q = collections.deque()
        self.level = [-1] * self.n
        q.append(start)
        self.level[start] = 0
        while q:
            node = q.popleft()
            for e in self.graph[node]:
                if e.cap > 0 and self.level[e.to] < 0:
                    self.level[e.to] = self.level[node] + 1
                    q.append(e.to)

# On lit les cas jusqu'à ce que 0 0
while True:
    # entrée un peu brute, on s'y fait
    x = input()
    if not x: continue
    M_N = x.split()
    if not M_N: continue
    M, N = map(int, M_N)
    if M == 0 and N == 0:
        break
    blue = []
    red = []
    while len(blue) < M:
        blue += [int(y) for y in input().split()]
    while len(red) < N:
        red += [int(z) for z in input().split()]
    V = M + N + 2
    adjList = [[] for _ in range(V)]
    for idx_b, b in enumerate(blue):
        for idx_r, r in enumerate(red):
            # je crois que c'est fractions.gcd en python2, mais bon, tant pis, risque d'erreur ici en python3
            if fractions.gcd(b, r) != 1:
                adjList[idx_b].append((M + idx_r, 1))
    for i in range(M):
        adjList[M + N].append((i, 1))
    for j in range(N):
        adjList[M + j].append((M + N + 1, 1))
    res = Dinic(V, adjList, M + N, M + N + 1).maxflow
    print(res)  # simple print, pas besoin de formatting spécial