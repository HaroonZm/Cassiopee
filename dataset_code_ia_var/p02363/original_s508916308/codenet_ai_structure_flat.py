from collections import defaultdict

INF = 999999999999999999999

G = {}
n, m = [int(v) for v in input().strip().split(' ')]
for i in range(n):
    G[i] = {}
for _ in range(m):
    s, t, c = [int(v) for v in input().strip().split(' ')]
    G[s][t] = c

d = {}
for i in range(n):
    d[i] = {}
    for j in range(n):
        if i in G and j in G[i]:
            d[i][j] = G[i][j]
        else:
            d[i][j] = INF
    d[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][k] == INF or d[k][j] == INF:
                continue
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]

for i in range(n):
    if d[i][i] < 0:
        print("NEGATIVE CYCLE")
        exit()

for i in range(n):
    row = []
    for j in range(n):
        if d[i][j] != INF:
            row.append(str(d[i][j]))
        else:
            row.append("INF")
    print(" ".join(row))