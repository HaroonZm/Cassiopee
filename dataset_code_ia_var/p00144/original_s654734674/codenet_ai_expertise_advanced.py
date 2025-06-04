from heapq import heappush, heappop
from typing import List, NamedTuple

class Pair(NamedTuple):
    cost: int
    point: int

class Graph:
    __slots__ = ('_n', '_adj')

    def __init__(self, n: int):
        self._n = n
        self._adj: List[List[Pair]] = [[] for _ in range(n)]

    def add_edge(self, u: int, v: int, cost: int):
        self._adj[u].append(Pair(cost, v))

    def dijkstra(self, start: int) -> List[int]:
        MAX = float('inf')
        dist = [MAX] * self._n
        dist[start] = 0
        visited = [False] * self._n
        heap = [Pair(0, start)]
        while heap:
            curr = heappop(heap)
            u = curr.point
            if visited[u]:
                continue
            visited[u] = True
            for edge in self._adj[u]:
                v, w = edge.point, edge.cost
                if not visited[v] and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heappush(heap, Pair(dist[v], v))
        return dist

def main():
    n = int(input())
    g = Graph(n)
    for _ in range(n):
        data = list(map(int, input().split()))
        u, k = data[0] - 1, data[1]
        for v in data[2:2+k]:
            g.add_edge(u, v - 1, 1)
    for _ in range(int(input())):
        u, v, ttl = map(int, input().split())
        cost = g.dijkstra(u - 1)[v - 1] + 1
        print(cost if cost <= ttl else "NA")

if __name__ == "__main__":
    main()