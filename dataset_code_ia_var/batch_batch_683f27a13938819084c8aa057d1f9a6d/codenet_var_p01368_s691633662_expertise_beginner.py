import sys

def read_line():
    return sys.stdin.readline()

def write_line(s):
    sys.stdout.write(s)

from collections import deque

class SimpleHopcroftKarp:
    def __init__(self, left_size, right_size):
        self.left_size = left_size
        self.right_size = right_size
        self.n = 2 + left_size + right_size
        self.graph = [[] for _ in range(self.n)]
        # Create source and sink connections
        for i in range(left_size):
            self.graph[0].append([2+i, 1, None])  # source to left
            self.graph[2+i].append([0, 0, self.graph[0][-1]])  # left to source
            self.graph[0][-1][2] = self.graph[2+i][-1]  # link
        self.back_edges = []
        for i in range(right_size):
            self.graph[2+left_size+i].append([1, 1, None])  # right to sink
            self.graph[1].append([2+left_size+i, 0, self.graph[2+left_size+i][-1]])  # sink to right
            self.graph[2+left_size+i][-1][2] = self.graph[1][-1]  # link
            self.back_edges.append(self.graph[1][-1])

    def add_edge(self, left, right):
        fr = 2 + left
        to = 2 + self.left_size + right
        forward = [to, 1, None]
        backward = [fr, 0, forward]
        forward[2] = backward
        self.graph[fr].append(forward)
        self.graph[to].append(backward)

    def bfs(self):
        queue = deque()
        level = [None] * self.n
        queue.append(0)
        level[0] = 0
        while queue:
            v = queue.popleft()
            for edge in self.graph[v]:
                w, cap, _ = edge
                if cap > 0 and level[w] is None:
                    level[w] = level[v] + 1
                    queue.append(w)
        self.level = level
        return level[1] is not None

    def dfs(self, v, t):
        if v == t:
            return True
        for edge in self.iters[v]:
            w, cap, rev = edge
            if cap > 0 and self.level[v] < self.level[w]:
                if self.dfs(w, t):
                    edge[1] = 0
                    rev[1] = 1
                    return True
        return False

    def max_flow(self):
        result = 0
        while self.bfs():
            self.iters = [iter(lst) for lst in self.graph]
            while self.dfs(0, 1):
                result += 1
        return result

    def get_matching(self):
        return [edge[1] for edge in self.back_edges]

def floyd_warshall(dist, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

def solve():
    parts = read_line()
    if not parts:
        return False
    tmp = parts.strip()
    if not tmp:
        return False
    NML = list(map(int, tmp.split()))
    if len(NML) < 3:
        return False
    N, M, L = NML
    if N == 0:
        return False
    INF = 10 ** 9
    dist = [[INF] * N for _ in range(N)]
    for i in range(M):
        u, v, d = map(int, read_line().split())
        dist[u][v] = d
        dist[v][u] = d
    for i in range(N):
        dist[i][i] = 0
    floyd_warshall(dist, N)
    points = []
    for _ in range(L):
        points.append(list(map(int, read_line().split())))
    points.sort(key=lambda x: x[1])
    hk = SimpleHopcroftKarp(L, L)
    for i in range(L):
        a, t1 = points[i]
        for j in range(i+1, L):
            b, t2 = points[j]
            if t1 + dist[a][b] <= t2:
                hk.add_edge(i, j)
    answer = L - hk.max_flow()
    write_line(str(answer) + "\n")
    return True

while solve():
    pass