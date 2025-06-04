import sys
input = sys.stdin.readline

# Variables globales
INF = 10 ** 18
l = 0

def merge(d, cost):
    total = d + cost
    refill, use = divmod(total, 10 ** 15)
    if use > l:
        refill += 1
        new_total = refill * 10 ** 15 + cost
    else:
        new_total = total
    return new_total

def dijkstra(start, matrix):
    n = len(matrix)
    used = [False] * n
    dist = [INF] * n
    dist[start] = 0
    while True:
        v = -1
        for u in range(n):
            if not used[u] and (v == -1 or dist[u] < dist[v]):
                v = u
        if v == -1:
            break
        used[v] = True
        for nxt in range(n):
            temp = merge(dist[v], matrix[v][nxt])
            if dist[nxt] > temp:
                dist[nxt] = temp
    return dist

n, m, l = map(int, input().split())
info = []
for i in range(m):
    info.append(list(map(int, input().split())))

q = int(input())
query = []
for i in range(q):
    query.append(list(map(int, input().split())))

# Matrice d'adjacence (graphe)
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(0)
        else:
            row.append(INF)
    matrix.append(row)

for edge in info:
    a, b, cost = edge
    a -= 1
    b -= 1
    if cost > l:
        continue
    matrix[a][b] = cost
    matrix[b][a] = cost

ans = []
for i in range(n):
    ans.append([0] * n)
for i in range(n):
    tmp = dijkstra(i, matrix)
    for j in range(n):
        ans[i][j] = tmp[j] // (10 ** 15)

for pair in query:
    a, b = pair
    a -= 1
    b -= 1
    if ans[a][b] == 1000:
        print(-1)
    else:
        print(ans[a][b])