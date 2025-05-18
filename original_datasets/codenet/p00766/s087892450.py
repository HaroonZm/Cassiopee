# Dinic algorithm
from collections import deque
class Dinic:
    def __init__(self, n):
        self.n = n
        self.g = [[] for i in xrange(n)]
    def add_edge(self, fr, to, cap):
        self.g[fr].append([to, cap, len(self.g[to])])
        self.g[to].append([fr, 0, len(self.g[fr])-1])
    def add_multi_edge(self, v1, v2, cap1, cap2):
        self.g[v1].append([v2, cap1, len(self.g[v2])])
        self.g[v2].append([v1, cap2, len(self.g[v1])-1])
    def bfs(self, s):
        level = [-1]*self.n
        deq = deque()
        level[s] = 0
        deq.append(s)
        while deq:
            v = deq.popleft()
            for e in self.g[v]:
                if e[1]>0 and level[e[0]]<0:
                    level[e[0]] = level[v] + 1
                    deq.append(e[0])
        self.level = level
    def dfs(self, v, t, f):
        if v==t: return f
        es = self.g[v]
        level = self.level
        for i in xrange(self.it[v], len(self.g[v])):
            e = es[i]
            if e[1]>0 and level[v]<level[e[0]]:
                d = self.dfs(e[0], t, min(f, e[1]))
                if d>0:
                    e[1] -= d
                    self.g[e[0]][e[2]][1] += d
                    self.it[v] = i
                    return d
        self.it[v] = len(self.g[v])
        return 0
    def max_flow(self, s, t):
        flow = 0
        while True:
            self.bfs(s)
            if self.level[t]<0: break
            self.it = [0]*self.n
            while True:
                f = self.dfs(s, t, 10**9+7)
                if f>0:
                    flow += f
                else:
                    break
        return flow

while 1:
    h, w = map(int, raw_input().split())
    if h == w == 0:
        break

    R = [raw_input() for i in xrange(h)]

    conn = [[0 for i in xrange(w)] for i in xrange(h)]

    P = []
    Q = []
    dep = 0

    for i in xrange(h-1):
        for j in xrange(w-1):
            first = R[i][j:j+2]; second = R[i+1][j:j+2]

            #                       .#    ##
            # if R[i:i+2][j:j+2] is ## or .#
            if (first == '.#' and second == '##') or (first == '##' and second == '.#'):
                k = j
                #                              #.     #.     ##
                # while R[i:i+2][k:k+2] is not ## and #. and #.
                while k+1 < w and R[i][k+1] != '.' and R[i+1][k+1] != '.':
                    k += 1
                #                       #.    ##
                # if R[i:i+2][k:k+2] is ## or #.
                if k+1 < w and ((R[i][k+1] == '#') ^ (R[i+1][k+1] == '#')):
                    P.append(((i, j), (i, k))) # (P)
                    conn[i][j] += 1
                    conn[i][k] += 1

            #                       .#    #.
            # if R[i:i+2][j:j+2] is ## or ##
            if first in ['.#', '#.'] and second == '##':
                k = i
                #                              ##     ##     ##
                # while R[k:k+2][j:j+2] is not #. and .. and .#
                while k+1 < h and R[k+1][j] != '.' and R[k+1][j+1] != '.':
                    k += 1
                #                       ##    ##
                # if R[k:k+2][j:j+2] is #. or .#
                if k+1 < h and ((R[k+1][j] == '#') ^ (R[k+1][j+1] == '#')):
                    Q.append(((i, j), (k, j))) # (Q)
                    conn[i][j] += 1
                    conn[k][j] += 1

            if first.count('#') + second.count('#') == 3:
                dep += 1

    # Bipartite graph
    dinic = Dinic(2 + len(P) + len(Q))
    # (s) -> (P)
    for i in xrange(len(P)):
        dinic.add_edge(0, i+2, 1)
    # (Q) -> (t)
    for i in xrange(len(Q)):
        dinic.add_edge(len(P)+i+2, 1, 1)
    # (P) -> (Q)
    for i, p in enumerate(P):
        (a, b), (a, s) = p
        for j, q in enumerate(Q):
            (c, d), (t, d) = q

            # check if two line segments intersect
            if c <= a <= t and b <= d <= s:
                dinic.add_edge(i+2, len(P) + j+2, 1)
    print dep - (len(P) + len(Q) - dinic.max_flow(0, 1)) + 1