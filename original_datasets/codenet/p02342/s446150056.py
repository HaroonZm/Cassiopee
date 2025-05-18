#!python3

iim = lambda: map(int, input().rstrip().split())
from itertools import chain, repeat

def resolve():
    N, K = iim()

    if N < K:
        print(0)
        return
    if N == 1 or K == 1:
        print(1)
        return

    mod = 10**9 + 7

    dp = [[0]*(K+1) for i in range(N+1)]
    dp[0][0] = 1

    for i, kx, i0 in zip( range(1, N+1), chain(range(1, K), repeat(K)), chain(repeat(1, N+1-K), range(2, K+1))):
        #print(i, kx, i0)
        for k in range(i0, kx + 1):
            dp[i][k] = dp[i-1][k-1] + dp[i-k][k]

    #for row in  dp:
    #    print(row)

    print(dp[N][K] % mod)

if __name__ == "__main__":
    resolve()