from collections import deque
from functools import partial
import sys

class Dinic:
    __slots__ = ('n', 'g', 'level', 'it')
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]
    def add_edge(self, fr, to, cap):
        forward = [to, cap, len(self.g[to])]
        backward = [fr, 0, len(self.g[fr])]
        self.g[fr].append(forward)
        self.g[to].append(backward)
    def add_multi_edge(self, v1, v2, cap1, cap2):
        forward = [v2, cap1, len(self.g[v2])]
        backward = [v1, cap2, len(self.g[v1])]
        self.g[v1].append(forward)
        self.g[v2].append(backward)
    def bfs(self, s):
        level = [-1] * self.n
        level[s] = 0
        deq = deque((s,))
        g = self.g
        while deq:
            v = deq.popleft()
            for to, cap, _ in g[v]:
                if cap and level[to] < 0:
                    level[to] = level[v] + 1
                    deq.append(to)
        self.level = level
    def dfs(self, v, t, upTo):
        if v == t:
            return upTo
        g_v, level, it = self.g[v], self.level, self.it
        for i in range(it[v], len(g_v)):
            to, cap, rev = g_v[i]
            if cap and level[v] < level[to]:
                d = self.dfs(to, t, min(upTo, cap))
                if d:
                    g_v[i][1] -= d
                    self.g[to][rev][1] += d
                    it[v] = i
                    return d
            it[v] = i+1
        return 0
    def max_flow(self, s, t, INF=10**9+7):
        flow = 0
        while True:
            self.bfs(s)
            if self.level[t] < 0:
                break
            self.it = [0]*self.n
            while True:
                f = self.dfs(s, t, INF)
                if not f: break
                flow += f
        return flow

def parse_board(h, w, lines):
    grid = [list(row) for row in lines]
    P, Q = [], []
    conn = [[0]*w for _ in range(h)]
    dep = 0
    for i in range(h-1):
        for j in range(w-1):
            first = ''.join(grid[i][j:j+2])
            second = ''.join(grid[i+1][j:j+2])
            if (first == '.#' and second == '##') or (first == '##' and second == '.#'):
                k = j
                while k+1 < w and grid[i][k+1] != '.' and grid[i+1][k+1] != '.':
                    k += 1
                if k+1 < w and (grid[i][k+1] == '#') != (grid[i+1][k+1] == '#'):
                    P.append(((i,j), (i,k)))
                    conn[i][j] += 1
                    conn[i][k] += 1
            if first in ('.#', '#.') and second == '##':
                k = i
                while k+1 < h and grid[k+1][j] != '.' and grid[k+1][j+1] != '.':
                    k += 1
                if k+1 < h and (grid[k+1][j] == '#') != (grid[k+1][j+1] == '#'):
                    Q.append(((i,j), (k,j)))
                    conn[i][j] += 1
                    conn[k][j] += 1
            if first.count('#') + second.count('#') == 3:
                dep += 1
    return P, Q, dep

def main():
    input_stream = sys.stdin
    readline = partial(next, iter(input_stream))
    while True:
        h, w = map(int, readline().split())
        if h == w == 0:
            break
        R = [readline().rstrip('\n') for _ in range(h)]
        P, Q, dep = parse_board(h, w, R)
        N, M = len(P), len(Q)
        dinic = Dinic(2 + N + M)
        for i in range(N):
            dinic.add_edge(0, i+2, 1)
        for i in range(M):
            dinic.add_edge(N+i+2, 1, 1)
        for i, ((a, b), (a_, s)) in enumerate(P):
            for j, ((c, d), (t, d_)) in enumerate(Q):
                if c <= a <= t and b <= d <= s:
                    dinic.add_edge(i+2, N+j+2, 1)
        res = dep - (N + M - dinic.max_flow(0, 1)) + 1
        print(res)
if __name__ == "__main__":
    main()