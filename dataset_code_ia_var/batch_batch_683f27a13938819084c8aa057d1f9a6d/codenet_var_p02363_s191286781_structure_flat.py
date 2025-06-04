from math import isinf

V, E = map(int, input().split())
D = [[float('inf')] * V for _ in range(V)]

for i in range(V):
    D[i][i] = 0

for _ in range(E):
    s, t, d = map(int, input().split())
    D[s][t] = d

for k in range(V):
    for i in range(V):
        for j in range(V):
            if D[i][j] > D[i][k] + D[k][j]:
                D[i][j] = D[i][k] + D[k][j]

cycle_found = False
for i in range(V):
    if D[i][i] < 0:
        print("NEGATIVE CYCLE")
        cycle_found = True
        break

if not cycle_found:
    for di in D:
        print(' '.join('INF' if isinf(dij) else str(dij) for dij in di))