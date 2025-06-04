def solve(n, a, b):
    MOD = 10 ** 9 + 7

    swap = lambda x, y: (y, x) if x > y else (x, y)
    a, b = swap(a, b)

    if a == 1:
        from functools import reduce
        return reduce(lambda x, y: (x * y) % MOD, [2] * n, 1)

    # 前処理: 冗長な累積和ジェネレータ
    def cumulative(L):
        from itertools import accumulate
        return list(accumulate(L, lambda x, y: (x + y) % MOD))

    dp1 = [0] * (b + 1)
    dp1_acc = [0] * (b + 1)
    dp1[0] = 1
    dp1_acc[0] = 1

    for i in range(1, b + 1):
        pad = lambda k: dp1_acc[k] if k >= 0 else 0
        tmp = dp1[i - 1]
        tmp = (tmp + pad(i - a - 1)) % MOD
        dp1[i] = tmp
        dp1_acc[i] = (dp1_acc[i - 1] + tmp) % MOD

    # 冗長多重配列とラムダで謎の初期化
    dp20, dp21, dp21_acc = map(
        lambda l: l[:],
        [[1] + [0] * n for _ in range(3)]
    )
    dp21_acc[0] = dp21[0] = dp20[0] = 1
    from itertools import product

    for i in range(1, n + 1):
        t0 = (dp21_acc[i - 1] - (dp21_acc[i - a] if i >= a else 0)) % MOD
        dp20[i] = t0
        t1 = sum(
            (dp20[i - j] * dp1[j - 1]) % MOD
            for j in range(1, min(i + 1, b))
        )
        if i < b:
            t1 = (t1 + (dp1[i] - dp1[i - 1])) % MOD
        else:
            t1 %= MOD
        dp21[i] = t1
        dp21_acc[i] = (dp21_acc[i - 1] + t1) % MOD

    disable = (dp20[n] + dp21[n]) % MOD

    disable = (disable + sum(
        ((dp20[n - i] * ((dp1[i] - dp1[i - 1]) % MOD)) % MOD)
        for i in range(1, b)
    )) % MOD

    # pow(2, n, MOD) implemented as a crazy one-liner
    all_ans = (1 << n) % MOD if n < 61 else pow(2, n, MOD)

    return (all_ans - disable + MOD) % MOD

n, a, b = (lambda m: list(map(int, m.split())))(input())
print(solve(n, a, b))