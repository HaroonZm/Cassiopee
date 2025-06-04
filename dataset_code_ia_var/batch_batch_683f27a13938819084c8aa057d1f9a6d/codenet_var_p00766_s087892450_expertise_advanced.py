import sys
from collections import deque
from itertools import count

class Dinic:
    __slots__ = 'n', 'g', 'level', 'it'
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]
    def add_edge(self, fr, to, cap):
        forward = [to, cap, len(self.g[to])]
        backward = [fr, 0, len(self.g[fr])]
        self.g[fr].append(forward)
        self.g[to].append(backward)
    def add_multi_edge(self, u, v, cap1, cap2):
        forward = [v, cap1, len(self.g[v])]
        backward = [u, cap2, len(self.g[u])]
        self.g[u].append(forward)
        self.g[v].append(backward)
    def bfs(self, s):
        level = self.level = [-1] * self.n
        q = deque([s])
        level[s] = 0
        append = q.append
        pop = q.popleft
        while q:
            v = pop()
            for to, cap, _ in self.g[v]:
                if cap and level[to] < 0:
                    level[to] = level[v] + 1
                    append(to)
    def dfs(self, v, t, upTo):
        if v == t: return upTo
        g_v = self.g[v]; level = self.level; it = self.it
        for i in range(it[v], len(g_v)):
            e = g_v[i]
            to, cap, rev = e
            if cap and level[v] < level[to]:
                d = self.dfs(to, t, min(upTo, cap))
                if d:
                    e[1] -= d
                    self.g[to][rev][1] += d
                    it[v] = i
                    return d
            it[v] = i+1
        return 0
    def max_flow(self, s, t):
        result = 0
        INF = 10**9+7
        while True:
            self.bfs(s)
            if self.level[t] < 0: break
            self.it = [0]*self.n
            while True:
                f = self.dfs(s, t, INF)
                if not f: break
                result += f
        return result

def read_input():
    return sys.stdin.readline()

def process():
    while True:
        h_w = read_input()
        if not h_w: break
        h, w = map(int, h_w.split())
        if h == 0 and w == 0: break
        R = [read_input().strip() for _ in range(h)]
        conn = [[0]*w for _ in range(h)]
        P, Q, dep = [], [], 0

        for i in range(h-1):
            for j in range(w-1):
                first = R[i][j:j+2]; second = R[i+1][j:j+2]

                # Horizontal check
                if (first == '.#' and second == '##') or (first == '##' and second == '.#'):
                    k = j
                    while k+1 < w and R[i][k+1] != '.' and R[i+1][k+1] != '.':
                        k += 1
                    if k+1 < w and ((R[i][k+1] == '#') ^ (R[i+1][k+1] == '#')):
                        P.append( ((i, j), (i, k)) )
                        conn[i][j] += 1
                        conn[i][k] += 1

                # Vertical check
                if first in ('.#', '#.') and second == '##':
                    k = i
                    while k+1 < h and R[k+1][j] != '.' and R[k+1][j+1] != '.':
                        k += 1
                    if k+1 < h and ((R[k+1][j] == '#') ^ (R[k+1][j+1] == '#')):
                        Q.append( ((i, j), (k, j)) )
                        conn[i][j] += 1
                        conn[k][j] += 1

                if first.count('#') + second.count('#') == 3:
                    dep += 1

        nP, nQ = len(P), len(Q)
        S, T = 0, 1
        offsetP, offsetQ = 2, 2 + nP

        dinic = Dinic(2 + nP + nQ)
        for idx in range(nP):
            dinic.add_edge(S, offsetP+idx, 1)
        for idx in range(nQ):
            dinic.add_edge(offsetQ+idx, T, 1)
        for i, (p_from, p_to) in enumerate(P):
            ai, aj = p_from; _, ak = p_to
            for j, (q_from, q_to) in enumerate(Q):
                bi, bj = q_from; bk, _ = q_to
                if bi <= ai <= bk and aj <= bj <= ak:
                    dinic.add_edge(offsetP+i, offsetQ+j, 1)
        print(dep - (nP + nQ - dinic.max_flow(S, T)) + 1)

if __name__ == "__main__":
    process()