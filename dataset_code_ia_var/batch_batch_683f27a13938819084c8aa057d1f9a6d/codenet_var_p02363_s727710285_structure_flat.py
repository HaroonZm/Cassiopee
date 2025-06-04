import sys

inf = float('inf')

N, M = map(int, sys.stdin.readline().split())
cost = [[inf]*N for _ in range(N)]
for u in range(N):
    cost[u][u] = 0

for _ in range(M):
    si, ti, di = map(int, sys.stdin.readline().split())
    cost[si][ti] = di

dist = [[cost[i][j] for j in range(N)] for i in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

has_negative_cycle = False
for i in range(N):
    if dist[i][i] < 0:
        has_negative_cycle = True
        break

if has_negative_cycle:
    print('NEGATIVE CYCLE')
else:
    for i in range(N):
        row = []
        for j in range(N):
            if dist[i][j] < inf:
                row.append(str(dist[i][j]))
            else:
                row.append('INF')
        print(' '.join(row))