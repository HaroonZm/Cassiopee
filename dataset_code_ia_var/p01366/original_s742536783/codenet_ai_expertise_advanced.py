from heapq import heappush, heappop
from functools import partial
from itertools import repeat, starmap

def dijkstra(edges, size, source):
    inf = float('inf')
    distance = [inf] * size
    distance[source] = 0
    visited = set()
    pq = [(0, source)]
    while pq:
        dist_u, u = heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        for v, weight, _ in edges[u]:
            if v not in visited:
                new_dist = dist_u + weight
                if distance[v] > new_dist:
                    distance[v] = new_dist
                    heappush(pq, (new_dist, v))
    return distance

def main():
    input_iter = iter(input, '')
    while True:
        try:
            N, M = map(int, next(input_iter).split())
            if N == M == 0:
                break
            edges = [[] for _ in repeat(None, N)]
            for _ in range(M):
                u, v, d, c = map(int, next(input_iter).split())
                u -= 1
                v -= 1
                edges[u].append((v, d, c))
                edges[v].append((u, d, c))
            dist = dijkstra(edges, N, 0)
            ans = sum(
                min(
                    (c for v, d, c in edges[u] if dist[u] == dist[v] + d),
                    default=1000
                ) for u in range(1, N)
            )
            print(ans)
        except StopIteration:
            break

main()