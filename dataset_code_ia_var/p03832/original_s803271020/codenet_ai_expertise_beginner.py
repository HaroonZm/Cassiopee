import sys

mod = 10**9 + 7

def LI():
    return list(map(int, sys.stdin.readline().split()))

def examC():
    ans = 0
    print(ans)

def examD():
    ans = 0
    print(ans)

def examE():
    # classe pour combinaisons modulo un nombre premier
    class Combination:
        def __init__(self, n, mod):
            self.n = n
            self.mod = mod
            self.fac = [1] * (n + 1)
            self.inv = [1] * (n + 1)
            for i in range(1, n + 1):
                self.fac[i] = (self.fac[i - 1] * i) % mod
            self.inv[n] = pow(self.fac[n], mod - 2, mod)
            for i in range(n - 1, -1, -1):
                self.inv[i] = (self.inv[i + 1] * (i + 1)) % mod

        def comb(self, n, r):
            if r > n or n < 0 or r < 0:
                return 0
            return self.fac[n] * self.inv[n - r] % self.mod * self.inv[r] % self.mod

    N, A, B, C, D = LI()
    comb_class = Combination(N + 1, mod)
    dp = [[0] * (N + 1) for _ in range(B + 2)]
    for i in range(A):
        dp[i][0] = 1
    for i in range(A, B + 1):
        for j in range(N + 1):
            dp[i][j] = dp[i - 1][j]
            for k in range(C, D + 1):
                if j - i * k >= 0:
                    temp = comb_class.comb(N - j + i * k, i * k)
                    temp2 = comb_class.comb(k * i, k)
                    add = dp[i - 1][j - i * k] * temp % mod * pow(temp2, mod - 2, mod) % mod
                    dp[i][j] = (dp[i][j] + add) % mod
    ans = dp[B][N]
    print(ans)

def examF():
    ans = 0
    print(ans)

if __name__ == '__main__':
    examE()