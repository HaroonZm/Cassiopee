from sys import stdin
from collections import defaultdict
from itertools import permutations, chain
import heapq

def getid(node, m, n):
    return {'H': 0, 'D': m + n + 1}.get(node) or (int(node[1:]) if node[0] == 'C' else m + int(node[1:]))

def ex_dijkstra(graph, m, size, start=0):
    dist = [float('inf')] * size
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        cur_dist, u = heapq.heappop(heap)
        if cur_dist > dist[u]:
            continue
        for length, v in graph[u]:
            nd = cur_dist + length
            if dist[v] > nd:
                dist[v] = nd
                if not (1 <= v <= m):
                    heapq.heappush(heap, (nd, v))
    return dist

input = iter(stdin)
for line in input:
    m,n,k,d = map(int, line.split())
    if m == 0:
        break
    cake = [0, *map(int, next(input).split())]
    graph = defaultdict(list)
    for _ in range(d):
        a,b,dist = next(input).split()
        a, b = getid(a,m,n), getid(b,m,n)
        dist = int(dist)*k
        graph[a].append((dist,b))
        graph[b].append((dist,a))
    size = m + n + 2
    compressed = [ex_dijkstra(graph, m, size, i) for i in range(m+1)]

    calorie = [
        sum(compressed[s][e] for s, e in zip(path, path[1:])) - sum(cake[i] for i in path[:-1])
        for r in range(m+1)
        for path in ((0, *perm, m+n+1) for perm in permutations(range(1,m+1), r))
    ]
    print(min(calorie))