def tsp(matrix):
    INF = float("inf")
    n = len(matrix)

    # dp[bit_state][i] := すでにbit_stateの状態を訪れていて、
    #                     最後に訪問したのがi番目のときの最小値
    dp = [[INF]*n for i in range(1 << n)]
    dp[1 << 0][0] = 0
 
    for bit_state in range(1 << n):
        for i in range(n):
            # bit_stateにiを含んでいる
            if (bit_state >> i) & 1:
                for j in range(n):
                    # bit_stateにjを含んでいない
                    if not ((bit_state >> j) & 1):
                        dp[bit_state|(1 << j)][j] = min(dp[bit_state|(1 << j)][j], dp[bit_state][i] + matrix[i][j])
    ans = INF
    for i in range(n):
        ans = min(dp[(1 << n) - 1][i] + matrix[i][0], ans)
    return ans

n, m = map(int, input().split())
info = [list(map(int, input().split())) for i in range(m)]
INF = float("inf")

matrix = [[INF]*n for i in range(n)]
for i in range(m):
    a, b, cost = info[i]
    matrix[a][b] = cost
for i in range(n):
    matrix[i][i] = 0

ans = tsp(matrix)
if ans == INF:
    print(-1)
else:
    print(ans)