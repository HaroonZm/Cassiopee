class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 2)  # Use n+2 to avoid index errors

    def get_sum(self, i):
        # Returns sum from 0 to i
        res = 0
        i += 1
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

    def add(self, i, x):
        # Adds x to position i
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def range_sum(self, l, r):
        # Returns sum from l to r
        return self.get_sum(r) - self.get_sum(l - 1)

import sys

readline = sys.stdin.readline

n, k = map(int, readline().split())
p = list(map(int, readline().split()))

b = BIT(n)
num = BIT(n)
MOD = 998244353
inv2 = (MOD + 1) // 2

for i in range(k):
    b.add(p[i] - 1, inv2)
    num.add(p[i] - 1, 1)

ans = k * (k - 1) // 2 % MOD * inv2 % MOD
prob = (k - 1) * pow(k, MOD - 2, MOD) % MOD
pinv = pow(prob, MOD - 2, MOD)
val = pinv * inv2 % MOD
rate = prob

for j in range(k, n):
    pj = p[j] - 1
    v = b.get_sum(pj)
    ans = (ans + v * rate % MOD) % MOD

    w = b.get_sum(n - 1) - v
    ans = (ans + ((j - num.get_sum(pj)) - w) * rate % MOD) % MOD

    b.add(pj, val)
    num.add(pj, 1)
    val = val * pinv % MOD
    rate = rate * prob % MOD

print(ans % MOD)