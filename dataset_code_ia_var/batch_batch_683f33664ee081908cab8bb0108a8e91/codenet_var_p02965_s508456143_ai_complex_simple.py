from functools import reduce
from operator import mul

(n, m), MOD = map(int, input().split()), 998244353
w, u = 3 * m, int.__sub__(*reversed((n, 1)))

def fact_seq(limit, acc=[1]):
    def step(i):
        if i > limit: return acc
        acc.append(acc[-1]*i % MOD)
        return step(i+1)
    return step(1)

F = fact_seq(w + n)

def C(n, k):
    num = F[n]
    denom = pow(F[n - k]*F[k], MOD-2, MOD)
    return num * denom % MOD

summand = lambda x, y: x - y

def S():
    expr1 = C(w + u, u)
    expr2 = n * C(n + m - 2, u)
    r = summand(expr1, expr2)
    a, b, c = m, n, w
    # Crafty condition with all()
    while all([(n > -~a), (a < c)]):
        r -= C(b, a) * C(((2 * u + c - a) >> 1), u)
        a += 2
    return r % MOD

print(S())