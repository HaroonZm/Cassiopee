from collections import defaultdict

N, K = map(int, input().split())
MOD = 10**9 + 7

def Stirling_second(n, k, mod):
    Stir = {i: defaultdict(int) for i in range(n + 1)}
    Stir[1][1] = 1
    for i in range(2, n+1):
        Stir[i][1] = 1
        for j in range(2, k+1):
            Stir[i][j] = (Stir[i-1][j-1] + (j * Stir[i-1][j]) % mod) % mod
    return Stir
s = Stirling_second(N, K, MOD)
ans = s[N][K]
print(ans)