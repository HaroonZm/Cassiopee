def solve(n, a, b):
    MOD = 10 ** 9 + 7
    if a > b:
        a, b = b, a
    if a == 1:
        return pow(2, n, MOD)
    dp1 = [0] * (b + 1)
    dp1_acc = [0] * (b + 1)
    dp1[0] = 1
    dp1_acc[0] = 1
    for i in range(1, b + 1):
        tmp = dp1[i - 1]
        if i - a - 1 >= 0:
            tmp = (tmp + dp1_acc[i - a - 1]) % MOD
        dp1[i] = tmp
        dp1_acc[i] = (dp1_acc[i - 1] + tmp) % MOD
    dp20 = [0] * (n + 1)
    dp21 = [0] * (n + 1)
    dp21_acc = [0] * (n + 1)
    dp20[0] = dp21[0] = dp21_acc[0] = 1
    for i in range(1, n + 1):
        t0 = dp21_acc[i - 1]
        if i >= a:
            t0 -= dp21_acc[i - a]
        dp20[i] = t0 % MOD
        t1 = 0
        for j in range(1, min(i + 1, b)):
            t1 += dp20[i - j] * dp1[j - 1]
        if i < b:
            t1 += dp1[i] - dp1[i - 1]
        t1 %= MOD
        dp21[i] = t1
        dp21_acc[i] = (dp21_acc[i - 1] + t1) % MOD
    disable = dp20[n] + dp21[n]
    for i in range(1, b):
        disable += dp20[n - i] * (dp1[i] - dp1[i - 1])
    return (pow(2, n, MOD) - disable) % MOD

n, a, b = map(int, input().split())
print(solve(n, a, b))