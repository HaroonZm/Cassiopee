from itertools import permutations

def warshall_floyd(d, n):
    # d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

N, M, R = map(int, input().split())
r = list(map(int, input().split()))
d = [[float('inf')] * N for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    d[a-1][b-1] = c
    d[b-1][a-1] = c

d = warshall_floyd(d, N)

ans = float('inf')
for p in permutations(r):
    total = 0
    for i in range(1, len(p)):
        total += d[p[i-1]-1][p[i]-1]
    ans = min(ans, total)
print(ans)