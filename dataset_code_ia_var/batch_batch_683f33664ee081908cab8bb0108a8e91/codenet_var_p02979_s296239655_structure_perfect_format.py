N, K, M = map(int, input().split())
L = (N + 1) // 2 + 1

def even(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(k + 1):
            dp[i + 1][0] = (dp[i + 1][0] + dp[i][j]) % M
            if j != k:
                dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % M
    return sum(dp[n]) % M

def loop(x, y):
    return (2 * x >= K + 1 and 2 * y >= K + 3)

if K % 2 == 0:
    print(even(N // 2, K // 2) * even((N + 1) // 2, K // 2) % M)
else:
    dp0 = [[[0] * (L + 1) for _ in range(L + 1)] for _ in range(L + 1)]
    dp0[0][0][L] = 1
    for i in range(N):
        dp1 = [[[0] * (L + 1) for _ in range(L + 1)] for _ in range(L + 1)]
        for x in range(L + 1):
            for y in range(L + 1):
                if loop(x, y):
                    continue
                for z in range(max(x, y) + 1, L + 1):
                    if dp0[x][y][z] == 0:
                        continue
                    dp1[y][x + 1][z] += dp0[x][y][z]
                    dp1[y][x + 1][z] %= M
                    if y > x:
                        zz = z
                    else:
                        zz = L
                    if 2 * y >= K + 3 and x > 0:
                        zz = min(zz, 1 + y - x + K // 2)
                    dp1[y][0][zz] += dp0[x][y][z]
                    dp1[y][0][zz] %= M
        dp0 = dp1
    ret = 0
    for x in range(L + 1):
        for y in range(L + 1):
            if loop(x, y):
                continue
            for z in range(max(x, y) + 1, L + 1):
                ret += dp0[x][y][z]
                ret %= M
    print(ret)