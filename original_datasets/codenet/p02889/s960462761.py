import sys
input = sys.stdin.readline

def dijkstra(start, matrix):
    # O(V^2)ダイクストラ
    INF = 10 ** 18
    n = len(matrix)
    used = [False] * n
    # 補給回数: 少ないほうがいい
    # 使用燃料: 少ないほうがいい
    # 補給回数が少ないほうがより嬉しい
    # dist[v] = 補給回数 * (10 ** 15) + 使用燃料
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
        for nxt_v in range(n):
            tmp = merge(dist[v], matrix[v][nxt_v])
            dist[nxt_v] = min(dist[nxt_v], tmp)
    return dist

def merge(d, cost):
    div_d, mod_d = divmod(d + cost, 10 ** 15)
    if mod_d > l:
        new_d = (div_d + 1) * 10 ** 15 + cost
    else:
        new_d = d + cost
    return new_d

n, m, l = map(int, input().split())
info = [list(map(int, input().split())) for i in range(m)]
q = int(input())
query = [list(map(int, input().split())) for i in range(q)]
INF = 10 ** 18

# 隣接行列
matrix = [[INF] * n for i in range(n)]
for i in range(n):
    matrix[i][i] = 0
for a, b, cost in info:
    a -= 1
    b -= 1
    if cost > l:
        continue
    matrix[a][b] = cost
    matrix[b][a] = cost

ans = [[0] * n for i in range(n)] 
for i in range(n):
    tmp = dijkstra(i, matrix)
    for j in range(n):
        ans[i][j] = tmp[j] // (10 ** 15)

for a, b in query:
    a -= 1
    b -= 1
    if ans[a][b] == 1000:
        print(-1)
    else:
        print(ans[a][b])