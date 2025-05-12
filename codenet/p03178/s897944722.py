MOD = 10**9 + 7

def main():
    # TDPC E or EDPC S
    S = [s for s in input()]
    N = len(S)
    D = int(input())
    dp = [[[0]*D for _ in range(2)] for _ in range(N+1)]
    dp[0][0][0] = 1
    from itertools import product
    for i, smaller, dsum in product(range(N), [True, False], range(D)):
        lim = 9 if smaller else int(S[i])
        for d in range(lim+1):
            dp[i+1][smaller or d < lim][(dsum+d) % D] += dp[i][smaller][dsum]
            dp[i+1][smaller or d < lim][(dsum+d) % D] %= MOD
    print((dp[N][0][0] + dp[N][1][0] - 1) % MOD)

if __name__ == '__main__':
    main()