import sys

def my_input():
    return sys.stdin.readline().strip()

def make_2d_list(x, y, val):
    result = []
    for i in range(x):
        row = []
        for j in range(y):
            row.append(val)
        result.append(row)
    return result

def make_3d_list(x, y, z, val):
    result = []
    for i in range(x):
        layer = []
        for j in range(y):
            row = []
            for k in range(z):
                row.append(val)
            layer.append(row)
        result.append(layer)
    return result

def my_ceil(a, b=1):
    return int(-(-a // b))

def to_int():
    return int(my_input())

def to_map():
    return map(int, my_input().split())

def get_list(n=None):
    if n is None:
        return list(to_map())
    else:
        result = []
        for _ in range(n):
            result.append(to_int())
        return result

def print_Yes():
    print('Yes')

def print_No():
    print('No')

def print_YES():
    print('YES')

def print_NO():
    print('NO')

sys.setrecursionlimit(10 ** 9)
INF = 10 ** 18
MOD = 10 ** 9 + 7
EPS = 10 ** -10

class SimpleModTools:
    def __init__(self, size, mod):
        self.size = size + 1
        self.mod = mod
        # set up factorial and inverse tables
        self.fact = [1] * self.size
        for i in range(2, self.size):
            self.fact[i] = self.fact[i-1] * i % mod
        self.inv = [1] * self.size
        self.inv[-1] = pow(self.fact[-1], mod-2, mod)
        for i in range(self.size-2, -1, -1):
            self.inv[i] = self.inv[i+1] * (i+1) % mod

    def nCr(self, n, r):
        if n < r: return 0
        num = self.fact[n]
        denom = self.inv[r] * self.inv[n-r] % self.mod
        return num * denom % self.mod

    def nHr(self, n, r):
        return self.nCr(r+n-1, r)

    def nPr(self, n, r):
        if n < r: return 0
        return self.fact[n] * self.inv[n-r] % self.mod

    def div(self, a, b):
        return a * pow(b, self.mod-2, self.mod) % self.mod

N, K = to_map()
mt = SimpleModTools(max(N, K)+1, MOD)
ans = 0
for i in range(K+1):
    temp = mt.nCr(K, i) * pow(K-i, N, MOD) % MOD
    if i % 2 == 0:
        ans = (ans + temp) % MOD
    else:
        ans = (ans - temp) % MOD
print(ans % MOD)