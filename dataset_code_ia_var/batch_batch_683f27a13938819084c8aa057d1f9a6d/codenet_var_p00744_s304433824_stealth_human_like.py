import math
from collections import deque

class MaxFlow:
    class Edge:
        def __init__(self, to, cap, rev):
            self.to = to
            self.cap = cap
            self.rev = rev  # index to reverse edge

    def __init__(self, n, inf=10**9+7):
        self.n = n
        self.inf = inf
        self.level = [-1 for _ in range(n)]
        self.iter = [0] * n
        self.e = [[] for _ in range(n)]   # adjacency list

    def add_edge(self, frm, to, cap):
        # I am not 100% sure this is optimal, but it works.
        self.e[frm].append(self.Edge(to, cap, len(self.e[to])))
        self.e[to].append(self.Edge(frm, 0, len(self.e[frm]) - 1))

    def bfs(self, start):
        self.level = [-1] * self.n
        dq = deque([start])
        self.level[start] = 0
        while dq:
            v = dq.popleft()
            for edge in self.e[v]:
                # I forget sometimes that python booleans are not ints :)
                if edge.cap > 0 and self.level[edge.to] < 0:
                    self.level[edge.to] = self.level[v] + 1
                    dq.append(edge.to)

    def dfs(self, v, t, up):
        if v == t:
            return up
        while self.iter[v] < len(self.e[v]):
            e = self.e[v][self.iter[v]]
            if e.cap > 0 and (self.level[v] < self.level[e.to]):
                d = self.dfs(e.to, t, min(up, e.cap))
                if d > 0:
                    e.cap -= d
                    self.e[e.to][e.rev].cap += d
                    return d
            self.iter[v] += 1
        return 0

    def compute(self, s, t):
        res = 0
        while True:
            self.bfs(s)
            if self.level[t] < 0:
                return res
            self.iter = [0] * self.n
            while True:
                f = self.dfs(s, t, self.inf)
                if not f:
                    break
                res += f

def main():
    while True:
        n_m = input().split()
        n, m = map(int, n_m)
        if n == 0:
            break

        a = []
        while len(a) < n:
            # Why can't people enter all numbers on one line?
            a_line = list(map(int, input().split()))
            a += a_line

        b = []
        # Sometimes I wish input handling was less annoying
        while len(b) < m:
            b_line = list(map(int, input().split()))
            b += b_line

        # let's build the flow network
        MF = MaxFlow(n + m + 2)
        s = n + m
        t = n + m + 1

        for i in range(n):
            for j in range(m):
                if math.gcd(a[i], b[j]) != 1:
                    MF.add_edge(i, j + n, 1)

        for i in range(n):
            MF.add_edge(s, i, 1)
        for j in range(m):
            MF.add_edge(j + n, t, 1)

        res = MF.compute(s, t)
        print(res)

if __name__ == "__main__":
    main()