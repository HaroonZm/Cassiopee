import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    x, y, t = map(int, input().split())
    graph[x-1].append((y-1, t))
    graph[y-1].append((x-1, t))
v0 = int(input())
a, b, c = map(int, input().split())

# Precompute all possible velocities
velocities = [0]*c
velocities[0] = v0
for i in range(1, c):
    velocities[i] = (a * velocities[i-1] + b) % c

INF = 10**18
dist = [[INF]*c for _ in range(n)]
# state: (cost_so_far, node, velocity_index)
dist[0][0] = 0
pq = [(0, 0, 0)]  # cost, node, velocity_index (number of edges taken mod c)

while pq:
    cost, u, j = heapq.heappop(pq)
    if dist[u][j] < cost:
        continue
    if u == 0 and j != 0 and cost != 0:
        # Returning to start after some edges
        print(cost)
        sys.exit()
    v_j = velocities[j]
    nj = (j + 1) % c
    for w, t in graph[u]:
        nd = cost + t * v_j
        if nd < dist[w][nj]:
            dist[w][nj] = nd
            heapq.heappush(pq, (nd, w, nj))

print(-1)  # If no such path found (should not happen, graph is connected)