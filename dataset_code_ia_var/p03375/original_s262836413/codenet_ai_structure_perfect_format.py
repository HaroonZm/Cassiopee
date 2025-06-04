from collections import defaultdict

class Combinatorics:
    def __init__(self, N, mod):
        '''
        Preprocess for calculating binomial coefficients nCr (0 <= r <= n, 0 <= n <= N)
        over the finite field Z/(mod)Z.
        Input:
            N (int): maximum n
            mod (int): a prime number. The order of the field Z/(mod)Z over which nCr is calculated.
        '''
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

    def binom(self, n, r):
        '''
        Calculate nCr = n! /(r! (n-r)!) % mod
        '''
        if n < r or n < 0 or r < 0:
            return 0
        else:
            return self.fact[n] * (self.fact_inverse[r] * self.fact_inverse[n - r] % self.mod) % self.mod

N, M = map(int, input().split())
com = Combinatorics(N, M)
ans = 0

pow2 = [0] * (N * N // 4 + 1)
pow_pow2 = [0] * (N + 1)
pow2[0] = 1
pow_pow2[0] = 2
for i in range(1, N * N // 4 + 1):
    pow2[i] = (pow2[i - 1] * 2) % M
for i in range(1, N + 1):
    pow_pow2[i] = pow(pow_pow2[i - 1], 2, M)

ways2 = {n: defaultdict(int) for n in range(N + 1)}
for n in range(N + 1):
    ways = 0
    temp = 0
    if n >= 1:
        for i in range(n + 1):
            ways2[n][i] = (ways2[n][i] + ways2[n - 1][i]) % M
            if i >= 1:
                ways2[n][i] = (ways2[n][i] + ways2[n - 1][i - 1]) % M
            ways2[n][i] = (ways2[n][i] + (i * ways2[n - 1][i]) % M) % M
            temp = (temp + (ways2[n][i] * pow2[(N - n) * i]) % M) % M
    else:
        ways2[n][0] = 1
        temp += ways2[n][0]
    ways = (temp * pow_pow2[N - n]) % M
    if n % 2 == 0:
        ans = (ans + (com.binom(N, n) * ways) % M) % M
    else:
        ans = (ans - (com.binom(N, n) * ways) % M) % M

print(ans)