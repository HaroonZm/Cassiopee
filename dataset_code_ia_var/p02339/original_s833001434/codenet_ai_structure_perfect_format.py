from collections import defaultdict

N, K = map(int, input().split())
MOD = 10**9 + 7

def Stirling_second(n, k, mod):
    Stir = {i: defaultdict(int) for i in range(n + 1)}
    Stir[1][1] = 1
    for i in range(2, n + 1):
        Stir[i][1] = 1
        for j in range(2, k + 1):
            prev1 = Stir[i - 1][j - 1]
            prev2 = Stir[i - 1][j]
            Stir[i][j] = (prev1 + (j * prev2) % mod) % mod
    return Stir

s = Stirling_second(N, K, MOD)
ans = s[N][K]
print(ans)