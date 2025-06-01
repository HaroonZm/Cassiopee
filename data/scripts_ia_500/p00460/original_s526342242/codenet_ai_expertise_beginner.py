def main():
    while True:
        line = input()
        N, M, S = map(int, line.split())
        if N == 0 and M == 0 and S == 0:
            break
        result = solve(N, M, S)
        print(result)

def solve(N, M, S):
    MOD = 100000
    p = N * N
    q = M - p
    T = S - (p * (p + 1)) // 2

    dp = []
    for i in range(p + 1):
        row = []
        for j in range(T + 1):
            row.append(0)
        dp.append(row)

    dp[0][0] = 1

    for i in range(1, p + 1):
        for j in range(T + 1):
            dp[i][j] = dp[i-1][j]
            if j - i >= 0:
                dp[i][j] += dp[i][j - i]
            if j - i - q >= 0:
                dp[i][j] -= dp[i-1][j - i - q]
            dp[i][j] = dp[i][j] % MOD

    return dp[p][T]

main()