import heapq
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass(order=True, slots=True, frozen=True)
class Edge:
    dst: int
    weight: int
    cost: int

class Graph:
    __slots__ = ('V', 'E')
    def __init__(self, V: int):
        self.V: int = V
        self.E: List[List[Edge]] = [[] for _ in range(V)]

    def add_edge(self, src: int, dst: int, weight: int, cost: int):
        self.E[src].append(Edge(dst, weight, cost))

class ShortestPath:
    __slots__ = 'G', 'INF', 'dist', 'prev'

    def __init__(self, G: Graph, INF: int = 10**9):
        self.G, self.INF = G, INF
        self.dist: List[int] = []
        self.prev: List[int] = []

    def dijkstra(self, start: int, goal: Optional[int] = None):
        self.dist = [self.INF] * self.G.V
        self.prev = [-1] * self.G.V
        self.dist[start] = 0
        heap = [(0, start)]
        while heap:
            cost, u = heapq.heappop(heap)
            if self.dist[u] < cost:
                continue
            if goal is not None and u == goal:
                break
            for e in self.G.E[u]:
                alt = self.dist[u] + e.weight
                if alt < self.dist[e.dst]:
                    self.dist[e.dst] = alt
                    self.prev[e.dst] = u
                    heapq.heappush(heap, (alt, e.dst))

    def get_path(self, end: int) -> List[int]:
        path = []
        while end != -1:
            path.append(end)
            end = self.prev[end]
        return path[::-1]

def run():
    import sys
    input_iter = iter(sys.stdin.read().split())
    def nexti():
        return int(next(input_iter))
    while True:
        N, M = nexti(), nexti()
        if N == 0 and M == 0:
            break
        g = Graph(N)
        for _ in range(M):
            u, v, d, c = nexti(), nexti(), nexti(), nexti()
            u -= 1; v -= 1
            g.add_edge(u, v, d, c)
            g.add_edge(v, u, d, c)
        sp = ShortestPath(g)
        sp.dijkstra(0)
        total = sum(
            min((e.cost for e in g.E[i] if sp.dist[e.dst] + e.weight == sp.dist[i]), default=0)
            for i in range(1, N)
        )
        print(total)

if __name__ == "__main__":
    run()