import sys

INF = float("inf")

class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = []
        for i in range(n):
            self.edges.append([])

    def add_edge(self, u, v, w=1):
        self.edges[u].append((v, w))
        self.edges[v].append((u, w))

def warshall_floyd(graph):
    n = graph.n
    dist = []
    for i in range(n):
        dist.append([INF]*n)
    for i in range(n):
        for (j, w) in graph.edges[i]:
            dist[i][j] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

def solve(n, m, l, a, b, c, q, s, t):
    g = Graph(n)
    for i in range(m):
        g.add_edge(a[i]-1, b[i]-1, c[i])
    dist = warshall_floyd(g)

    g2 = Graph(n)
    for i in range(n):
        for j in range(i+1, n):
            if dist[i][j] <= l:
                g2.add_edge(i, j, 1)
    dist2 = warshall_floyd(g2)

    for i in range(q):
        ans = dist2[s[i]-1][t[i]-1] - 1
        if ans == INF - 1:
            print(-1)
        elif dist2[s[i]-1][t[i]-1] == INF:
            print(-1)
        else:
            print(ans)

def main():
    inputs = []
    for line in sys.stdin:
        for word in line.strip().split():
            inputs.append(word)
    idx = 0
    n = int(inputs[idx])
    idx += 1
    m = int(inputs[idx])
    idx += 1
    l = int(inputs[idx])
    idx += 1
    a = []
    b = []
    c = []
    for i in range(m):
        a.append(int(inputs[idx]))
        idx += 1
        b.append(int(inputs[idx]))
        idx += 1
        c.append(int(inputs[idx]))
        idx += 1
    q = int(inputs[idx])
    idx += 1
    s = []
    t = []
    for i in range(q):
        s.append(int(inputs[idx]))
        idx += 1
        t.append(int(inputs[idx]))
        idx += 1
    solve(n, m, l, a, b, c, q, s, t)

if __name__ == "__main__":
    main()