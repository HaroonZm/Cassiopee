class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 2)  # All indexes are 1-indexed for simplicity

    def get_sum(self, i):  # sum of a[0]..a[i]
        i += 1
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= (i & -i)
        return s

    def range_sum(self, l, r):
        return self.get_sum(r) - self.get_sum(l - 1)

    def add(self, i, x):
        i += 1
        while i < len(self.tree):
            self.tree[i] += x
            i += (i & -i)

import sys
readline = sys.stdin.readline

n, k = map(int, readline().split())
p = list(map(int, readline().split()))

b = BIT(n)
num = BIT(n)
MOD = 998244353
inv2 = (MOD + 1) // 2

for i in range(k):
    b.add(p[i] - 1, 1)
    num.add(p[i] - 1, 1)

ans = (k * (k - 1) // 2) % MOD
ans = ans * inv2 % MOD

tot = k
rate = (k - 1) * pow(k, MOD - 2, MOD) % MOD
rateinv = pow(rate, MOD - 2, MOD)
bunbo = rate
hosei = rateinv

for i in range(k, n):
    pi = p[i] - 1
    v = b.get_sum(pi)
    ans = (ans + v * inv2 % MOD * bunbo % MOD) % MOD

    x = i - num.get_sum(pi)
    w = (x - (tot - v) * inv2 % MOD * bunbo % MOD) % MOD
    ans = (ans + w) % MOD

    b.add(pi, hosei)
    num.add(pi, 1)
    tot = (tot + hosei) % MOD
    hosei = hosei * rateinv % MOD
    bunbo = bunbo * rate % MOD

print(ans % MOD)