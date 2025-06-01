import sys
import heapq

sys.setrecursionlimit(10**8)
n, m, x = map(int, input().split())
H = [0, *map(int, (input() for _ in range(n)))]
edges = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    edges[a].append((b, t))
    edges[b].append((a, t))

def dijkstra():
    heap = [(0, 1, x)]
    visited = set()
    while heap:
        cost, node, h = heapq.heappop(heap)
        if node == n:
            if h == H[n]:
                return cost
            heapq.heappush(heap, (cost + H[n] - h, n, H[n]))
            continue
        if (node, h) in visited:
            continue
        visited.add((node, h))
        for nxt, t in edges[node]:
            nh = h - t
            if 0 <= nh <= H[nxt]:
                heapq.heappush(heap, (cost + t, nxt, nh))
            elif nh > H[nxt]:
                heapq.heappush(heap, (cost + h - H[nxt], nxt, H[nxt]))
            elif H[node] - t >= 0:
                heapq.heappush(heap, (cost + t - h + t, nxt, 0))
    return -1

print(dijkstra())