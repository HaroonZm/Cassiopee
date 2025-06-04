import sys
import threading
from collections import defaultdict
from typing import List, Tuple

sys.setrecursionlimit(1 << 25)

class Graph:
    def __init__(self, n: int):
        self.n = n
        self.adj = defaultdict(list)  # node -> list of (neighbor, weight)
    
    def add_edge(self, u: int, v: int, w: int):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))


class LCA:
    def __init__(self, graph: Graph, root: int = 1):
        self.n = graph.n
        self.LOG = max(1, (self.n.bit_length()))
        self.depth = [0] * (self.n + 1)
        self.parent = [[-1] * (self.n + 1) for _ in range(self.LOG)]
        self.dist_to_root = [0] * (self.n + 1)
        self.graph = graph
        self._dfs(root, -1, 0, 0)
        self._build()

    def _dfs(self, node: int, par: int, dep: int, dist: int):
        self.parent[0][node] = par
        self.depth[node] = dep
        self.dist_to_root[node] = dist
        for (nxt, w) in self.graph.adj[node]:
            if nxt != par:
                self._dfs(nxt, node, dep + 1, dist + w)
    
    def _build(self):
        for k in range(1, self.LOG):
            for v in range(1, self.n + 1):
                if self.parent[k-1][v] != -1:
                    self.parent[k][v] = self.parent[k-1][self.parent[k-1][v]]

    def lca(self, u: int, v: int) -> int:
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        # Lift u up so it is at same depth with v
        for k in reversed(range(self.LOG)):
            if self.parent[k][u] != -1 and self.depth[self.parent[k][u]] >= self.depth[v]:
                u = self.parent[k][u]
        if u == v:
            return u
        for k in reversed(range(self.LOG)):
            if self.parent[k][u] != -1 and self.parent[k][u] != self.parent[k][v]:
                u = self.parent[k][u]
                v = self.parent[k][v]
        return self.parent[0][u]

    def distance(self, u: int, v: int) -> int:
        l = self.lca(u, v)
        return self.dist_to_root[u] + self.dist_to_root[v] - 2 * self.dist_to_root[l]


class MeetingInCitySolution:
    def __init__(self, n: int, edges: List[Tuple[int,int,int]], queries: List[Tuple[int,int,int]]):
        self.graph = Graph(n)
        for (u,v,w) in edges:
            self.graph.add_edge(u,v,w)
        self.lca_struct = LCA(self.graph, root=1)
        self.queries = queries

    def _dist(self,u,v):
        return self.lca_struct.distance(u,v)

    def _cost_for_theme(self, a:int,b:int,c:int) -> int:
        # Candidates for minimal cost meeting city are limited to a,b,c or the LCA nodes of pairs (a,b), (b,c), (a,c)
         # because the minimal maximum distances happen around these junction points.
        candidates = {a,b,c}
        candidates.add(self.lca_struct.lca(a,b))
        candidates.add(self.lca_struct.lca(b,c))
        candidates.add(self.lca_struct.lca(a,c))

        min_cost = float('inf')
        for city in candidates:
            # max distance for three students to this meeting city
            dist_a = self._dist(a, city)
            dist_b = self._dist(b, city)
            dist_c = self._dist(c, city)
            max_dist = max(dist_a, dist_b, dist_c)
            if max_dist < min_cost:
                min_cost = max_dist
        return min_cost

    def solve(self) -> List[int]:
        results = []
        for (a,b,c) in self.queries:
            # careful: input guarantees a < b < c but solution does not rely on that
            results.append(self._cost_for_theme(a,b,c))
        return results


def main():
    input = sys.stdin.readline
    n,q = map(int,input().split())
    edges = [tuple(map(int,input().split())) for _ in range(n-1)]
    queries = [tuple(map(int,input().split())) for _ in range(q)]
    sol = MeetingInCitySolution(n, edges, queries)
    results = sol.solve()
    print('\n'.join(map(str, results)))


threading.Thread(target=main,).start()