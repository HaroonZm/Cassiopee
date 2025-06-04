import sys
sys.setrecursionlimit(1000000)

def read_input():
    return sys.stdin.readline()

class SCC:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.rgraph = [[] for _ in range(n)]
        self.visited = [False]*n
        self.order = []
        self.component = []

    def add_edge(self, frm, to):
        if frm == to:
            return
        self.graph[frm].append(to)
        self.rgraph[to].append(frm)

    def dfs(self, v):
        self.visited[v] = True
        for to in self.graph[v]:
            if not self.visited[to]:
                self.dfs(to)
        self.order.append(v)

    def rdfs(self, v, label):
        self.visited[v] = True
        self.component[label].append(v)
        for to in self.rgraph[v]:
            if not self.visited[to]:
                self.rdfs(to, label)

    def scc(self):
        self.visited = [False]*self.n
        self.order = []
        for v in range(self.n):
            if not self.visited[v]:
                self.dfs(v)
        self.visited = [False]*self.n
        self.component = []
        for v in reversed(self.order):
            if not self.visited[v]:
                self.component.append([])
                self.rdfs(v, len(self.component)-1)
        return self.component

class UnionFind:
    def __init__(self, n):
        self.par = [-1]*(n+1)

    def find(self, x):
        if self.par[x] < 0:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.par[x] > self.par[y]:
            x, y = y, x
        self.par[x] += self.par[y]
        self.par[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

class TwoSat:
    def __init__(self, n):
        self.n = n
        self.scc = SCC(n*2)
        self.uf = UnionFind(n*2)
        self.groups = []

    def add(self, a, b):
        self.scc.add_edge(a, b)

    def build(self):
        self.groups = self.scc.scc()
        for group in self.groups:
            if len(group) > 1:
                for i in range(len(group)-1):
                    self.uf.union(group[i], group[i+1])

    def is_ok(self):
        for i in range(self.n):
            if self.uf.same(i, i+self.n):
                return False
        return True

    def judge_and_get_groups(self):
        self.build()
        return self.is_ok()

def main():
    raw = read_input()
    while raw.strip() == "":
        raw = read_input()
    n, d = map(int, raw.strip().split())
    ts = TwoSat(n*2)
    pos = []
    for _ in range(n):
        while True:
            line = read_input()
            if line.strip():
                break
        x, y = map(int, line.strip().split())
        pos.append((x, y))
    for i in range(n):
        ts.add(n*3+i, i)
        ts.add(n*2+i, n+i)
    for i in range(n):
        for j in range(i+1, n):
            if abs(pos[i][0] - pos[j][0]) < d:
                ts.add(i, n*2+j)
                ts.add(j, n*2+i)
                ts.add(i, n+j)
                ts.add(j, n+i)
            if abs(pos[i][0] - pos[j][1]) < d:
                ts.add(i, j)
                ts.add(i, n*3+j)
                ts.add(n+j, n+i)
                ts.add(n+j, n*2+i)
            if abs(pos[i][1] - pos[j][0]) < d:
                ts.add(j, i)
                ts.add(j, n*3+i)
                ts.add(n+i, n+j)
                ts.add(n+i, n*2+j)
            if abs(pos[i][1] - pos[j][1]) < d:
                ts.add(i+n, j)
                ts.add(i+n, j+n*3)
                ts.add(j+n, i)
                ts.add(j+n, i+n*3)
    ok = ts.judge_and_get_groups()
    if ok:
        print("Yes")
        used = [-1]*n
        done = 0
        for group in reversed(ts.groups):
            for v in group:
                if v >= n*2:
                    continue
                idx = v if v < n else v - n
                if used[idx] == -1:
                    done += 1
                    used[idx] = 0 if v < n else 1
                if done == n:
                    break
        for i in range(n):
            print(pos[i][used[i]])
    else:
        print("No")

if __name__ == "__main__":
    main()