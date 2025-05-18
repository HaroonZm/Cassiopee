#!python3

iim = lambda: map(int, input().rstrip().split())

def resolve():
    N, K = iim()
    mod = 10**9 + 7

    if N == 1 or K == 1:
        print(1)
        return

    dp = [[0] * (K+1) for i in range(N+1)]
    dp[0][0] = 1

    def ik(n, k):
        for i in range(1, min(k,n+1)):
            yield (i, i)
        for i in range(i+1, n+1):
            yield (i, k)

    for i, kx in ik(N, K):
        for k in range(1, kx+1):
            dp[i][k] = dp[i-1][k-1] + dp[i-k][k]

    #for row in dp:
    #    print(row)

    print(sum(dp[N]) % mod)

if __name__ == "__main__":
    resolve()