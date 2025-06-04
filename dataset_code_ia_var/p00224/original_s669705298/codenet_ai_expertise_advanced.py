from functools import lru_cache
import sys
import heapq
from collections import defaultdict
from itertools import permutations, chain

def getid(node, m, n):
    match node:
        case 'H':
            return 0
        case 'D':
            return m + n + 1
        case str() if node[0] == 'C':
            return int(node[1:])
        case _:
            return m + int(node[1:])

def ex_dijkstra(graph, m, size, start=0):
    dist = [float('inf')] * size
    dist[start] = 0
    hq = [(0, start)]
    while hq:
        du, u = heapq.heappop(hq)
        if du > dist[u]:
            continue
        for length, v in graph[u]:
            alt = dist[u] + length
            if alt < dist[v]:
                dist[v] = alt
                if 1 <= v <= m:
                    continue
                heapq.heappush(hq, (alt, v))
    return dist

def solve():
    f = sys.stdin
    while True:
        m, n, k, d = map(int, f.readline().split())
        if m == 0:
            break
        cake = [0] + list(map(int, f.readline().split()))
        graph = defaultdict(list)
        for _ in range(d):
            a, b, dist = f.readline().split()
            a, b = getid(a, m, n), getid(b, m, n)
            dist = int(dist) * k
            graph[a].append((dist, b))
            graph[b].append((dist, a))
        # Precompute all pairs shortest for cakes and H
        node_cnt = m + n + 2
        compressed = [ex_dijkstra(graph, m, node_cnt, i) for i in range(m + 1)]
        min_cost = float('inf')
        ids = range(1, m + 1)
        # To avoid recomputing sums of cake, precompute prefix sums
        cake_sum = [0] * (m + 1)
        for i in range(1, m + 1):
            cake_sum[i] = cake_sum[i - 1] + cake[i]
        # For all combinations/permutations of cake visits
        for comb in chain.from_iterable(permutations(ids, i) for i in range(m + 1)):
            path = (0,) + comb + (node_cnt - 1,)
            cost = sum(compressed[s][e] for s, e in zip(path, path[1:])) - sum(cake[x] for x in comb)
            if cost < min_cost:
                min_cost = cost
        print(min_cost)

if __name__ == '__main__':
    solve()