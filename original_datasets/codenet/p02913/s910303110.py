def main():
    N = int(input())
    S = input()
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    r = 0
    for i in reversed(range(N)):
        s = S[i]
        for j in reversed(range(i, N)):
            if s == S[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
            r = max(r, min(dp[i][j], j - i))
    print(r)

main()