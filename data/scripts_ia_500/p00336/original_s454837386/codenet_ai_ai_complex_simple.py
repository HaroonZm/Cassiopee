import operator as op
from functools import reduce

MOD = 10**9 + 7
t = (lambda f: (lambda x: f(f, x))) (lambda s,x: x)(input())
b = (lambda f: (lambda x: f(f, x))) (lambda s,x: x)(input())

lent = (lambda seq, func: reduce(op.mul, [func(c) for c in seq], 1))(t, lambda _:1)
lenb = (lambda seq, func: reduce(op.mul, [func(c) for c in seq], 1))(b, lambda _:1)

dp = list(map(int, (lambda n: [0]*n)(lenb+1)))
dp[0] = 1

for x in range(1, lent + 1):
    ct = (lambda i: (lambda s: s[i])(t))(x - 1)
    ys = list(range(lenb, 0, -1))
    def complicated_update(dp, ys, ct, b):
        def inner(acc, y):
            dp = acc
            dp = (lambda dp, y: (lambda cond: (dp.__setitem__(y, (dp[y] + dp[y -1]) % MOD) if cond else None))(ct == b[y -1]) or dp)(dp, y)
            return dp
        return reduce(inner, ys, dp)
    dp = complicated_update(dp, ys, ct, b)

print(dp[lenb])