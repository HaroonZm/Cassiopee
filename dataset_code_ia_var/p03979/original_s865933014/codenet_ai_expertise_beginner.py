import sys
from collections import deque, defaultdict

# Lecture des entrées
H, W = map(int, sys.stdin.readline().split())
S = []
for _ in range(H):
    S += list(sys.stdin.readline().strip())

INF = 10 ** 12

def get_index(h, w):
    return h * W + w

# Création du graphe comme dictionnaire imbriqué
graph = defaultdict(dict)
source = -1
sink = -2

# On crée les sommets et les arêtes
for h in range(H):
    for w in range(W):
        i = get_index(h, w)
        vin = i * 2      # v_in
        vout = i * 2 + 1 # v_out
        if S[i] == '.':
            graph[vin][vout] = 1
            graph[vout][vin] = 0
        else:
            graph[source][vout] = INF
            graph[vout][source] = 0
        for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nh = h + dh
            nw = w + dw
            if 0 <= nh < H and 0 <= nw < W:
                j = get_index(nh, nw)
                jin = j * 2
                graph[vout][jin] = 1
                graph[jin][vout] = 0
            else:
                graph[vout][sink] = INF
                graph[sink][vout] = 0

# Algorithme de flot maximum (DINIC simple)
class Dinic:
    def __init__(self, graph, source, sink):
        self.graph = defaultdict(dict)
        self.nodes = set()
        for u in graph:
            for v in graph[u]:
                self.graph[u][v] = graph[u][v]
                self.nodes.add(u)
                self.nodes.add(v)
        self.source = source
        self.sink = sink

    def bfs(self, level):
        queue = deque()
        queue.append(self.source)
        level[self.source] = 0
        while queue:
            v = queue.popleft()
            for to in self.graph[v]:
                if self.graph[v][to] > 0 and level[to] < 0:
                    level[to] = level[v] + 1
                    queue.append(to)
        return level[self.sink] != -1

    def dfs(self, v, flow, level, iter):
        if v == self.sink:
            return flow
        for i in range(iter[v], len(self.graph[v])):
            iter[v] = i
            to = list(self.graph[v].keys())[i]
            if self.graph[v][to] > 0 and level[v] < level[to]:
                d = self.dfs(to, min(flow, self.graph[v][to]), level, iter)
                if d > 0:
                    self.graph[v][to] -= d
                    if to not in self.graph or v not in self.graph[to]:
                        self.graph[to][v] = 0
                    self.graph[to][v] += d
                    return d
        return 0

    def max_flow(self):
        flow = 0
        while True:
            level = {v: -1 for v in self.nodes}
            if not self.bfs(level):
                break
            iter = {v:0 for v in self.nodes}
            while True:
                f = self.dfs(self.source, INF, level, iter)
                if f == 0:
                    break
                flow += f
        return flow

dinic = Dinic(graph, source, sink)
result = dinic.max_flow()
if result >= INF:
    print(-1)
else:
    print(result)