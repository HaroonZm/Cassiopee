from heapq import heappush, heappop
from operator import add
from itertools import repeat

def readint():
    return map(int, input().split())

SENTINEL = float('inf')
while True:
    n, m, s, g1, g2 = readint()
    if not n:
        break
    s, g1, g2 = (x - 1 for x in (s, g1, g2))
    pipes = [set() for _ in repeat(None, n)]
    rpipes = [set() for _ in repeat(None, n)]
    for _ in range(m):
        b1, b2, c = readint()
        b1 -= 1; b2 -= 1
        pipes[b1].add((c, b2))
        rpipes[b2].add((c, b1))

    def dijkstra(start, graph):
        dist = [SENTINEL] * n
        dist[start] = 0
        heap = list(graph[start])
        visited = {start}
        while heap:
            cost, u = heappop(heap)
            if u in visited:
                continue
            visited.add(u)
            dist[u] = cost
            heap.extend((cost + nc, nv) for nc, nv in graph[u] if nv not in visited)
        for v in set(range(n)) - visited:
            dist[v] = SENTINEL
        return dist

    dist1 = dijkstra(g1, rpipes)
    dist2 = dijkstra(g2, rpipes)
    distsum = list(map(add, dist1, dist2))

    best = distsum[s]
    heap, visited = list(pipes[s]), {s}
    while heap:
        cost, u = heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        best = min(best, cost + distsum[u])
        heap.extend((cost + nc, nv) for nc, nv in pipes[u] if nv not in visited)

    print(int(best if best < SENTINEL else SENTINEL))