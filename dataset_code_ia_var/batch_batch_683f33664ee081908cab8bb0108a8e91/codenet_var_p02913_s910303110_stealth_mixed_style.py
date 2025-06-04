def main():
    N = int(input())
    S = input()
    dp = []
    for _ in range(N+1):
        dp.append([0]*(N+1))
    res = 0
    i = N-1
    while i >= 0:
        ch = S[i]
        # style fonctionnel pour la boucle intérieure
        def process_j(j):
            nonlocal res
            if ch == S[j]:
                dp[i][j] = dp[i+1][j+1] + 1
            else:
                pass
            res = max(res, min(dp[i][j], j-i))
        for j in range(N-1, i-1, -1):
            process_j(j)
        i -= 1
    print(res)
main()