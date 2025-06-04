from functools import lru_cache

def f(n, k):
    MOD = 10 ** 9 + 7
    if k & 1:
        print(0)
        return

    half_k = k // 2

    @lru_cache(maxsize=None)
    def dp(i, j, s):
        if i == 0:
            return int(j == 0 and s == 0)
        if j > i or s < 0:
            return 0
        res = 0
        # 片側、水平、両方上
        res += (dp(i-1, j, s-j) * (2 * j + 1)) % MOD
        if j:
            res += dp(i-1, j-1, s-j)
        res += (dp(i-1, j+1, s-j) * pow(j+1, 2, MOD)) % MOD
        return res % MOD

    print(dp(n, 0, half_k))

n, k = map(int, input().split())
f(n, k)