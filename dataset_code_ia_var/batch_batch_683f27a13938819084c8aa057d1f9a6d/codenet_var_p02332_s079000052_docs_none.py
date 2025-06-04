from collections import defaultdict

class Combinatorics:
    def __init__(self, N, mod):
        self.mod = mod
        self.fact = {i: None for i in range(N+1)}
        self.inverse = {i: None for i in range(1, N+1)}
        self.fact_inverse = {i: None for i in range(N+1)}
        self.fact[0] = self.fact[1] = 1
        self.fact_inverse[0] = self.fact_inverse[1] = 1
        self.inverse[1] = 1
        for i in range(2, N+1):
            self.fact[i] = i * self.fact[i-1] % self.mod
            q, r = divmod(self.mod, i)
            self.inverse[i] = (- (q % self.mod) * self.inverse[r]) % self.mod
            self.fact_inverse[i] = self.inverse[i] * self.fact_inverse[i-1] % self.mod

    def perm(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        else:
            return (self.fact[n] * self.fact_inverse[n-r]) % self.mod

    def binom(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        else:
            return self.fact[n] * (self.fact_inverse[r] * self.fact_inverse[n-r] % self.mod) % self.mod

    def hom(self, n, r):
        if n == 0 and r > 0:
            return 0
        if n >= 0 and r == 0:
            return 1
        return self.binom(n + r - 1, r)

n, k = map(int, input().split())
MOD = 10**9 + 7
com = Combinatorics(k, MOD)
ans = com.perm(k, n)
print(ans)