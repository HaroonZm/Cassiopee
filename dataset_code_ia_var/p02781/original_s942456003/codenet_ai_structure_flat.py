N = list(map(int, list(input())))
K = int(input())
Nlen = len(N)
dp = [[[0]*(K+2) for _ in range(2)] for n in range(Nlen+1)]
dp[0][0][0] = 1
nlen = 0
while nlen < Nlen:
    dN = N[nlen]
    d = 0
    while d < 10:
        j = 0
        while j < 2:
            k = 0
            while k < K+2:
                flagj = j or d < dN
                if (flagj == 0) and (d > dN):
                    k += 1
                    continue
                flagk = min(K+1, k+(d != 0))
                dp[nlen+1][flagj][flagk] += dp[nlen][j][k]
                k += 1
            j += 1
        d += 1
    nlen += 1
print(dp[-1][0][K]+dp[-1][1][K])