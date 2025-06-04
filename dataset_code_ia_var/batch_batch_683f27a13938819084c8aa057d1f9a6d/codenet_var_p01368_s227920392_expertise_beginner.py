import sys
import collections

sys.setrecursionlimit(10000000)

inf = 10**20

def LI():
    return list(map(int, sys.stdin.readline().split()))

def main():
    results = []

    class WarshallFloyd:
        def __init__(self, edges, n):
            self.n = n
            self.edges = edges

        def search(self):
            d = [[inf for j in range(self.n)] for i in range(self.n)]
            for i in range(self.n):
                d[i][i] = 0
            for u in self.edges:
                for v, cost in self.edges[u]:
                    if d[u][v] > cost:
                        d[u][v] = cost
            for k in range(self.n):
                for i in range(self.n):
                    for j in range(self.n):
                        if d[i][j] > d[i][k] + d[k][j]:
                            d[i][j] = d[i][k] + d[k][j]
            return d

    class Flow:
        def __init__(self, E, N):
            self.E = E
            self.N = N

        def max_flow(self, s, t):
            flow = 0
            while True:
                used = [False] * self.N

                def dfs(v):
                    if v == t:
                        return True
                    used[v] = True
                    for u in list(self.E[v]):
                        if not used[u]:
                            if dfs(u):
                                self.E[v].remove(u)
                                self.E[u].add(v)
                                return True
                    return False

                if not dfs(s):
                    break
                flow += 1
            return flow

    while True:
        nm = LI()
        if len(nm) == 0:
            continue
        n, m, l = nm
        if n == 0:
            break

        roads = []
        for _ in range(m):
            roads.append(LI())
        points = []
        for _ in range(l):
            points.append(LI())

        edge = {}
        for i in range(n):
            edge[i] = []
        for u, v, d in roads:
            edge[u].append((v, d))
            edge[v].append((u, d))

        wf = WarshallFloyd(edge, n)
        dist = wf.search()

        G2 = collections.defaultdict(set)
        for i in range(l):
            p1, t1 = points[i]
            for j in range(l):
                if i == j:
                    continue
                p2, t2 = points[j]
                if dist[p1][p2] <= t2 - t1:
                    G2[i].add(j + l)
            G2[2 * l].add(i)
            G2[i + l].add(2 * l + 1)

        fl = Flow(G2, 2 * l + 2)
        t = fl.max_flow(2 * l, 2 * l + 1)
        results.append(str(l - t))

    print('\n'.join(results))

main()