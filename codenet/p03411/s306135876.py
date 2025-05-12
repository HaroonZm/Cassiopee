from collections import deque

class Dinic:
    def __init__(self, v, inf=float('inf')):
        self.V = v
        self.inf = inf
        # self.G = {i:[] for i in range(self.V)}
        self.G = [[] for _ in range(self.V)]
        self.level = [0] * self.V
        self.iter = [0] * self.V

    def add_edge(self, from_v, to_v, cap):
        self.G[from_v].append({'to': to_v, 'cap': cap, 'rev': len(self.G[to_v])})
        self.G[to_v].append({'to': from_v, 'cap': 0, 'rev': len(self.G[from_v]) - 1})

    def bfs(self, s):
        self.level = [-1] * self.V
        self.level[s] = 0
        que = deque()
        que.appendleft(s)

        while len(que) > 0:
            v = que.pop()
            for i in range(len(self.G[v])):
                e = self.G[v][i]
                if e['cap'] > 0 and self.level[e['to']] < 0:
                    self.level[e['to']] = self.level[v] + 1
                    que.appendleft(e['to'])

    def dfs(self, v, t, f):
        if v == t:
            return f

        for i in range(self.iter[v], len(self.G[v])):
            self.iter[v] = i
            e = self.G[v][i]
            if e['cap'] > 0 and self.level[v] < self.level[e['to']]:
                d = self.dfs(e['to'], t, min(f, e['cap']))
                if d > 0:
                    e['cap'] -= d
                    self.G[e['to']][e['rev']]['cap'] += d
                    return d

        return 0

    def maxflow(self, s, t):
        flow = 0
        while True:
            self.bfs(s)
            if self.level[t] < 0:
                return flow

            self.iter = [0] * self.V
            f = self.dfs(s, t, self.inf)
            while f > 0:
                flow += f
                f = self.dfs(s, t, self.inf)

def read_input():
    n = int(input())

    red = []
    for i in range(n):
        a, b = map(int, input().split())
        red.append((a, b))

    blue = []
    for i in range(n):
        c, d = map(int, input().split())
        blue.append((c, d))

    return n, red, blue

def submit():
    n, red, blue = read_input()
    dinic = Dinic(2*n+2)

    for i in range(n):
        dinic.add_edge(2*n, i, 1)
        dinic.add_edge(n+i, 2*n+1, 1)

    for i,b in enumerate(blue):
        for j,r in enumerate(red):
            if r[0] < b[0] and r[1] < b[1]:
                dinic.add_edge(j, n+i, 1)

    print(dinic.maxflow(2*n, 2*n+1))

if __name__ == '__main__':
    submit()