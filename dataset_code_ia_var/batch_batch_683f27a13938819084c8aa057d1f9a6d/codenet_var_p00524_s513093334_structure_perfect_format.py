import sys
import heapq as q

sys.setrecursionlimit(10 ** 8)

n, m, x = [int(i) for i in input().split()]
H = [0] + [int(input()) for _ in range(n)]
A = [[int(i) for i in input().split()] for _ in range(m)]

INF = 10 ** 16

Q = []
path = [[] for _ in range(n + 1)]
used = [False] * (n + 1)

def bfs():
    q.heappush(Q, (0, 1, x))  # (cost, node, high)
    while Q:
        cost, node, h = q.heappop(Q)
        if node == n:
            if h == H[n]:
                return cost
            q.heappush(Q, (cost + H[n] - h, n, H[n]))
            continue
        if used[node]:
            continue
        used[node] = True
        for a, t in path[node]:
            if 0 <= h - t <= H[a]:
                q.heappush(Q, (cost + t, a, h - t))
            elif h - t > H[a]:
                q.heappush(Q, (cost + h - H[a], a, H[a]))
            elif H[node] - t >= 0:
                q.heappush(Q, (cost + t - h + t, a, 0))
    return -1

for a, b, t in A:
    path[a].append((b, t))
    path[b].append((a, t))

print(bfs())