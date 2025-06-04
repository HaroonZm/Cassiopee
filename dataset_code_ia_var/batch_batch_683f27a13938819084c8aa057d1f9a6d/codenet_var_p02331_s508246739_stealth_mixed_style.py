def calc():
    class Wrapper:
        def __init__(self, val):
            self.v = val
    [n, k] = list(map(int, input().split()))
    MOD = 10 ** 9 + 7
    def fastpow(a, b, m):
        r = 1
        while b:
            if b & 1:
                r = (r * a) % m
            a = (a * a) % m
            b >>= 1
        return r
    res = fastpow(k, n, MOD)
    w = Wrapper(res)
    print(w.v)
calc()