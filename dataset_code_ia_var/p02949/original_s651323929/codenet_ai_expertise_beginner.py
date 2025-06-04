import sys

N, M, P = map(int, sys.stdin.readline().split())
ABC = []
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    ABC.append((a, b, c))

edges = []
for a, b, c in ABC:
    edges.append((a, b, P - c))

INF = 10 ** 18
dist = [INF] * (N + 1)
dist[1] = 0

for t in range(N + N + 10):
    updated = False
    for a, b, cost in edges:
        if dist[a] < INF and dist[b] > dist[a] + cost and dist[a] + cost < INF // 2:
            if t > N:
                dist[b] = -INF
            else:
                dist[b] = dist[a] + cost
            updated = True
    # (A simple break could be added if no update, but keeping basic, we skip)

answer = -dist[N]
if answer < 0:
    answer = 0
elif dist[N] == INF:
    answer = -1
print(answer)