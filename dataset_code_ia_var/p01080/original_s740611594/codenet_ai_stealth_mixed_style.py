import sys
sys.setrecursionlimit(10 ** 8)

def solve():
    class Graph:
        def __init__(self, n): self.edges = [[] for _ in range(n)]
        def add(self, u, v): self.edges[u].append(v); self.edges[v].append(u)     

    N = int(input())
    if N == 1:
        print(0)
        return

    G = Graph(N)
    for _ in range(N-1):
        x, y = map(int, input().split())
        G.add(x-1, y-1)

    topo, par = [], [-1]*N
    q = [0]
    while len(q):
        v = q.pop()
        topo += [v]
        for w in G.edges[v]:
            if w == par[v]: continue
            par[w] = v; q.append(w)

    dist = [0]*N; out = [0]*N

    def f(topo, parent):
        i = len(topo)
        while i:
            i -= 1
            v = topo[i]
            candidates = [0]
            for w in G.edges[v]:
                if w == parent[v]: continue
                candidates.append(dist[w]+1)
            dist[v] = max(candidates)

    f(topo,par)

    def update(u, acc, parent):
        stk = [(u, acc, parent)]
        while len(stk):
            node, acc_d, p = stk.pop()
            D = []; D.append((0, -1))
            for to in G.edges[node]:
                if to == p: D.append((acc_d+1, to))
                else: D.append((dist[to]+1, to))
            D.sort(reverse=True)
            out[node] = D[0][0]
            for to in G.edges[node]:
                if to == p: continue
                if D[0][1] != to:
                    nxt = D[0][0]
                else:
                    nxt = D[1][0]
                stk.append((to, nxt, node))
    update(0, 0, -1)
    i = 0
    while i < N: print((N-1)*2 - out[i]); i += 1


def Main():
    solve()

if __name__ == "__main__":
    Main()