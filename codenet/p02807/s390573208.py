class Combination:
    '''MOD上の
    計算量：階乗・逆元テーブルの作成O(N)
    nCkを求めるO(1)'''

    def __init__(self, n, MOD):
        self.fact = [1]
        for i in range(1, n + 1):
            self.fact.append(self.fact[-1] * i % MOD)
        self.inv_fact = [pow(self.fact[i], MOD - 2, MOD) for i in range(n + 1)]
        self.MOD = MOD

    def factorial(self, k):
        """k!を求める O(1)"""
        return self.fact[k]

    def inverse_factorial(self, k):
        """k!の逆元を求める O(1)"""
        return self.inv_fact[k]

    def permutation(self, k, r):
        """kPrを求める O(1)"""
        if k < r:
            return 0
        return (self.fact[k] * self.inv_fact[r]) % self.MOD

    def combination(self, k, r):
        """kCrを求める O(1)"""
        if k < r:
            return 0
        return (self.fact[k] * self.inv_fact[k - r] * self.inv_fact[r]) % self.MOD

n = int(input())
a = list(map(int, input().split()))
MOD = 10**9 + 7
comb = Combination(n, MOD)

effi = [0] * n
effi[0] = 1
for i in range(n - 1):
    effi[i + 1] = effi[i] + pow(i + 2, MOD - 2, MOD)
    effi[i + 1] %= MOD

ans = 0
for i in range(n - 1):
    ans += effi[i] * (a[i+1] - a[i])
    ans %= MOD

print(ans * comb.factorial(n - 1) % MOD)