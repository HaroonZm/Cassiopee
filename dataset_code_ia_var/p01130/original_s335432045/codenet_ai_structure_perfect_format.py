while True:
    N, M, s, g1, g2 = map(int, input().split())
    if N == 0 and M == 0 and s == 0 and g1 == 0 and g2 == 0:
        break
    s -= 1
    g1 -= 1
    g2 -= 1
    INF = 10 ** 5
    D = [[INF for _ in range(N)] for _ in range(N)]
    for i in range(N):
        D[i][i] = 0
    for _ in range(M):
        b1, b2, c = map(int, input().split())
        b1 -= 1
        b2 -= 1
        D[b1][b2] = c
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
    result = min(D[s][i] + D[i][g1] + D[i][g2] for i in range(N))
    print(result)