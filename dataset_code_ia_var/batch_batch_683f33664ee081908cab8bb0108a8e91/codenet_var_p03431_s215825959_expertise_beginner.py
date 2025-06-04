def combs_mod(n, k, mod):
    inv = [1] * (k + 1)
    for i in range(1, k + 1):
        inv[i] = pow(i, mod - 2, mod)
    ans = [1] * (k + 1)
    for i in range(1, k + 1):
        ans[i] = ans[i - 1] * (n + 1 - i) % mod
        ans[i] = ans[i] * inv[i] % mod
    return ans

def solve():
    mod = 998244353
    N, K = map(int, input().split())
    ans = 0
    if K < N:
        return ans
    com = combs_mod(K, K, mod)
    com2 = combs_mod(K - 1, K - 1, mod)
    for r in range(K + 1):
        b = K - r
        dif = r - b
        if dif < 0 or r < N:
            continue
        if dif == 0:
            ans = (ans + com2[r]) % mod
            if N >= 2:
                ans = (ans - com2[N - 2]) % mod
        elif dif < N:
            ans = (ans + com[r] - com[N - 1 - dif]) % mod
        else:
            ans = (ans + com[r]) % mod
    return ans

print(solve())