import sys
from collections import deque

def read_input():
    return sys.stdin.readline()

class SimpleDinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
    
    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        backward = [fr, 0, forward]
        forward[2] = backward
        self.graph[fr].append(forward)
        self.graph[to].append(backward)
    
    def add_multi_edge(self, a, b, ca, cb):
        edge1 = [b, ca, None]
        edge2 = [a, cb, edge1]
        edge1[2] = edge2
        self.graph[a].append(edge1)
        self.graph[b].append(edge2)
    
    def bfs(self, start, end):
        self.level = [None] * self.n
        queue = deque()
        queue.append(start)
        self.level[start] = 0
        while queue:
            node = queue.popleft()
            for to, cap, rev in self.graph[node]:
                if cap > 0 and self.level[to] is None:
                    self.level[to] = self.level[node] + 1
                    queue.append(to)
        return self.level[end] is not None
    
    def dfs(self, v, t, flow):
        if v == t:
            return flow
        for edge in self.it[v]:
            to, cap, rev = edge
            if cap > 0 and self.level[v] < self.level[to]:
                d = self.dfs(to, t, min(flow, cap))
                if d > 0:
                    edge[1] -= d
                    rev[1] += d
                    return d
        return 0
    
    def max_flow(self, s, t):
        total = 0
        INF = 10**9+7
        while self.bfs(s, t):
            self.it = list(map(iter, self.graph))
            flow = INF
            while flow:
                flow = self.dfs(s, t, INF)
                total += flow
        return total

def parse_poly(s, L=50):
    s = s + '$'
    E = [0]*(L+1)
    cur = 0
    while True:
        if s[cur].isdigit():
            k = 0
            while s[cur].isdigit():
                k = k*10 + int(s[cur])
                cur += 1
        else:
            k = 1
        if s[cur] == 'x':
            cur += 1
            if s[cur] == '^':
                cur += 1
                p = 0
                while s[cur].isdigit():
                    p = p*10 + int(s[cur])
                    cur += 1
            else:
                p = 1
        else:
            p = 0
        E[p] = k
        if s[cur] != '+':
            break
        cur += 1
    return E

def solve():
    line = read_input()
    if not line:
        return False
    N_M = line.strip().split()
    if not N_M or N_M[0] == '0':
        return False
    N, M = int(N_M[0]), int(N_M[1])
    L = 50
    dinics = []
    for _ in range(L+1):
        dinics.append(SimpleDinic(N))
    for _ in range(M):
        row = read_input().strip().split()
        u = int(row[0]) - 1
        v = int(row[1]) - 1
        poly = parse_poly(row[2], L)
        for j in range(L+1):
            if poly[j] > 0:
                dinics[j].add_multi_edge(u, v, poly[j], poly[j])
    INF = 10**9
    res = [0]*(L+1)
    for i in range(L+1):
        res[i] = dinics[i].max_flow(0, N-1)
    E = [[0]*N for _ in range(N)]
    for j in range(L-1, -1, -1):
        dinic = dinics[j]
        G = dinics[j+1].graph
        for x in range(N):
            for y, cap, _ in G[x]:
                if cap > 0:
                    E[x][y] = 1
        for x in range(N):
            for y in range(N):
                if E[x][y]:
                    dinic.add_edge(x, y, INF)
        res[j] += dinic.max_flow(0, N-1)
    answer = []
    if res[0] > 0:
        answer.append(str(res[0]))
    if res[1] > 0:
        if res[1] > 1:
            answer.append(str(res[1]) + "x")
        else:
            answer.append("x")
    for i in range(2, L+1):
        if res[i] > 0:
            if res[i] > 1:
                answer.append(str(res[i]) + "x^" + str(i))
            else:
                answer.append("x^" + str(i))
    if not answer:
        answer.append("0")
    answer.reverse()
    sys.stdout.write("+".join(answer) + "\n")
    return True

while solve():
    pass