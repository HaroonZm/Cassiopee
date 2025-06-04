class Twelvefold:
    def __init__(self, n, mod):
        self.mod = mod
        self.fct = [1] * (n + 1)
        self.inv = [1] * (n + 1)
        self.stl = []
        for i in range(n + 1):
            self.stl.append([0] * (n + 1))
        self.bel = []
        for i in range(n + 1):
            self.bel.append([0] * (n + 1))
        self.prt = []
        for i in range(n + 1):
            self.prt.append([0] * (n + 1))

        self.stl[0][0] = 1
        self.bel[0][0] = 1

        for i in range(1, n + 1):
            self.fct[i] = self.fct[i - 1] * i % mod

        self.inv[n] = pow(self.fct[n], mod - 2, mod)
        for i in range(n - 1, -1, -1):
            self.inv[i] = self.inv[i + 1] * (i + 1) % mod

        for i in range(n):
            for j in range(n + 1):
                if j > 0:
                    self.stl[i + 1][j] = (self.stl[i][j - 1] + j * self.stl[i][j]) % mod

        for i in range(n):
            for j in range(n + 1):
                if j == 0:
                    self.bel[i + 1][j] = self.stl[i + 1][j] % mod
                else:
                    self.bel[i + 1][j] = (self.bel[i + 1][j - 1] + self.stl[i + 1][j]) % mod

        for j in range(n + 1):
            self.prt[0][j] = 1
        for i in range(n):
            for j in range(n):
                cur = self.prt[i + 1][j]
                if i - j >= 0:
                    cur = (cur + self.prt[i - j][j + 1]) % mod
                self.prt[i + 1][j + 1] = cur

    def solve(self, n, k, eq_elem=False, eq_sub=False, less1=False, more1=False):
        # We don't use all parameters for now. Only simple orderings.
        a = eq_elem
        b = eq_sub
        c = less1
        d = more1

        id = a * 3 + b * 6 + c + d * 2
        funclist = [self.tw1, self.tw2, self.tw3, self.tw4, self.tw5, self.tw6, self.tw7, self.tw8, self.tw9, self.tw10, self.tw11, self.tw12]
        return funclist[id](n, k)

    def tw1(self, n, k):
        return pow(k, n, self.mod)

    def tw2(self, n, k):
        if k < n:
            return 0
        return self.fct[k] * self.inv[k - n] % self.mod

    def tw3(self, n, k):
        return self.stl[n][k] * self.fct[k] % self.mod

    def tw4(self, n, k):
        if k == 0:
            return 0
        return self.fct[n + k - 1] * self.inv[n] * self.inv[k - 1] % self.mod

    def tw5(self, n, k):
        if k < n:
            return 0
        return self.fct[k] * self.inv[n] * self.inv[k - n] % self.mod

    def tw6(self, n, k):
        if n < k or k == 0:
            return 0
        return self.fct[n - 1] * self.inv[k - 1] * self.inv[n - k] % self.mod

    def tw7(self, n, k):
        return self.bel[n][k]

    def tw8(self, n, k):
        if k < n:
            return 0
        return 1

    def tw9(self, n, k):
        return self.stl[n][k]

    def tw10(self, n, k):
        return self.prt[n][k]

    def tw11(self, n, k):
        if k < n:
            return 0
        return 1

    def tw12(self, n, k):
        if n < k:
            return 0
        return self.prt[n - k][k]

n, k = map(int, input().split())
t = Twelvefold(1000, 10**9 + 7)
print(t.solve(n, k, 0, 0, 0, 0))