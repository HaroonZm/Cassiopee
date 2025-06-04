import sys
input = sys.stdin.readline
INF = 10**15

while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    dist = [[INF]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    queries = []
    for _ in range(k):
        tmp = list(map(int, input().split()))
        if tmp[0] == 1:
            _, c, d, e = tmp
            c -= 1
            d -= 1
            if e < dist[c][d]:
                dist[c][d] = e
                dist[d][c] = e
            # Floyd-Warshall update for new edge
            for i in range(n):
                for j in range(n):
                    nd = min(dist[i][c]+e+dist[d][j], dist[i][d]+e+dist[c][j])
                    if nd < dist[i][j]:
                        dist[i][j] = nd
        else:
            _, a, b = tmp
            a -= 1
            b -= 1
            queries.append((a,b))
    for a,b in queries:
        print(dist[a][b] if dist[a][b]!=INF else -1)