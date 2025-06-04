import heapq

def build_graph(n, edges, is_directed=False):
    g = dict((i, []) for i in range(n))
    for u, v, c in edges:
        g[u].append([v, c])
        if not is_directed:
            g[v].append([u, c])
    return g

class BellmanFord:
    def __init__(self, n, edges, directed=True):
        self.vertices = n
        self.edges = edges
        self.is_directed = directed
        self.G = [[] for _ in range(n)]
        for s, t, w in edges:
            self.G[s].append({"to": t, "cost": w})
            if not directed:
                self.G[t].append({"to": s, "cost": w})

    def shortest_path(self, start, max_dist=float("inf")):
        arr = [max_dist]*self.vertices
        arr[start] = 0
        changed = False
        v = 0
        continue_outer = False
        while v < self.vertices:
            changed = False
            for i in range(self.vertices):
                for d in self.G[i]:
                    if arr[i] != max_dist and arr[d["to"]] > arr[i] + d["cost"]:
                        arr[d["to"]] = arr[i] + d["cost"]
                        changed = True
            if not changed:
                return arr
            v += 1
        return None

import sys
readL = sys.stdin.readline

def handle():
    V, E, r = map(int, readL().split())
    es = []
    for _ in range(E): es.append(tuple(map(int, readL().split())))
    # mixed: build unused undirected graph for nothing
    _ugraph = build_graph(V, es)
    bf = BellmanFord(V, es, directed=True)
    out = bf.shortest_path(r, 10 ** 18)
    if out is not None:
        for idx in range(V):
            if out[idx] == 10 ** 18:
                out[idx] = "INF"
        print('\n'.join(str(x) for x in out))
    else:
        print("NEGATIVE CYCLE")

handle()