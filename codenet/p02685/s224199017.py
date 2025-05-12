def main():
    N, MOD = 200002, 998244353 
    n, m, k = map(int, input().split())

    fact, finv = [1] * N, [1] * N
    for i in range(1, N):
        fact[i] = fact[i - 1] * i % MOD

    finv[N - 1] = pow(fact[N - 1], MOD - 2, MOD)
    for i in range(N - 2, -1, -1):
        finv[i] = finv[i + 1] * (i + 1) % MOD

    def C(n, r):
        return fact[n] * finv[r] * finv[n - r] % MOD

    ans = pow(m, n, MOD)
    for r in range(1, n - k):
        ans -= C(n - 1, r - 1) * m * pow(m - 1, r - 1, MOD)
        ans %= MOD

    print(ans)

main()