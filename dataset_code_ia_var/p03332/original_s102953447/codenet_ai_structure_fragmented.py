MOD = 998244353

def create_list(size, default):
    return [default] * (size + 1)

def initialize_factorial_list(n, mod):
    f = create_list(n, 0)
    f[0] = 1
    return f

def fill_factorial_list(f, n, mod):
    b = 1
    for i in range(1, n + 1):
        b = (b * i) % mod
        f[i] = b
    return f

def initialize_inv_list(n):
    return create_list(n, 0)

def compute_inverse(a, mod):
    return pow(a, -1, mod)

def fill_inv_list(inv, f, n, mod):
    b = compute_inverse(f[n], mod)
    inv[n] = b
    for i in range(n, 0, -1):
        b = (b * i) % mod
        inv[i - 1] = b
    return inv

def factorial(f, i):
    return f[i]

def ifactorial(inv, i):
    return inv[i]

def combination(f, inv, mod, n, k):
    if not 0 <= k <= n:
        return 0
    return f[n] * inv[n - k] % mod * inv[k] % mod

def permutation(f, inv, mod, n, k):
    if not 0 <= k <= n:
        return 0
    return f[n] * inv[n - k] % mod

def homogeneous(f, inv, mod, n, k):
    if (n == 0 and k > 0) or k < 0:
        return 0
    return f[n + k - 1] * inv[k] % mod * inv[n - 1] % mod

def input_parser():
    return map(int, input().split())

class Factorial:
    def __init__(self, n, mod):
        self.mod = mod
        self.f = self._build_factorial(n, mod)
        self.inv = self._build_inv(self.f, n, mod)
    def _build_factorial(self, n, mod):
        f = initialize_factorial_list(n, mod)
        return fill_factorial_list(f, n, mod)
    def _build_inv(self, f, n, mod):
        inv = initialize_inv_list(n)
        return fill_inv_list(inv, f, n, mod)
    def factorial(self, i):
        return factorial(self.f, i)
    def ifactorial(self, i):
        return ifactorial(self.inv, i)
    def C(self, n, k):
        return combination(self.f, self.inv, self.mod, n, k)
    def P(self, n, k):
        return permutation(self.f, self.inv, self.mod, n, k)
    def H(self, n, k):
        return homogeneous(self.f, self.inv, self.mod, n, k)

def compute_term(F, n, p, b, k):
    q, r = divmod(k - p * b, b)
    if r != 0:
        return 0
    return F.C(n, p) * F.C(n, q) % MOD

def compute_summation(F, n, a, b, k):
    result = 0
    max_p = k // a
    for p in range(max_p + 1):
        current = compute_term(F, n, p, b, k)
        result = (result + current) % MOD
    return result

def main():
    n, a, b, k = input_parser()
    F = Factorial(n, MOD)
    result = compute_summation(F, n, a, b, k)
    print(result)

main()