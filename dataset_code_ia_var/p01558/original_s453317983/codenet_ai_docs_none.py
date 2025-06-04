class RollingHash:
    def __init__(self, s, base, MOD):
        self.s = s
        self.l = l = len(s)
        self.base = base
        self.MOD = MOD
        self.h = h = [0]*(l + 1)
        for i in xrange(l):
            h[i+1] = (h[i] * base + ord(s[i])) % MOD
    def get(self, l, r):
        MOD = self.MOD
        return ((self.h[r] - self.h[l]*pow(self.base, r-l, MOD) + MOD)) % MOD
n, m = map(int, raw_input().split())
s = raw_input()
h1 = RollingHash(s, 13, 10**9+7)
h2 = RollingHash(s, 17, 10**9+7)
l = 0; r = 1
vs = set()
ans = 0
for i in xrange(m):
    q = raw_input()
    if q == "R++":
        r += 1
    elif q == "R--":
        r -= 1
    elif q == "L++":
        l += 1
    else:
        l -= 1
    v = (h1.get(l, r), h2.get(l, r))
    if v not in vs:
        ans += 1
        vs.add(v)
print ans