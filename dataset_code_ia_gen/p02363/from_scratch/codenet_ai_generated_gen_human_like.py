import sys
input = sys.stdin.readline

V, E = map(int, input().split())
INF = 10**15
dist = [[INF]*V for _ in range(V)]
for i in range(V):
    dist[i][i] = 0

for _ in range(E):
    s, t, d = map(int, input().split())
    dist[s][t] = d

for k in range(V):
    for i in range(V):
        for j in range(V):
            if dist[i][k] != INF and dist[k][j] != INF:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

# Check for negative cycles
for i in range(V):
    if dist[i][i] < 0:
        print("NEGATIVE CYCLE")
        sys.exit()

for i in range(V):
    row = []
    for j in range(V):
        if dist[i][j] == INF:
            row.append("INF")
        else:
            row.append(str(dist[i][j]))
    print(" ".join(row))