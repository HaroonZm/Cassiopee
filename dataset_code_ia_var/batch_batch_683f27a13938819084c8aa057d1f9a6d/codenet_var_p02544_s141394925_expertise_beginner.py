class SegmentTree:
    def __init__(self, arr, default=0, func=max):
        self.default = default
        self.func = func
        self.n = len(arr)
        # next power of two for size
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        # fill array with defaults
        self.data = [default] * (2 * self.size)
        for i in range(self.n):
            self.data[self.size + i] = arr[i]
        # build the tree
        for i in range(self.size - 1, 0, -1):
            self.data[i] = func(self.data[i * 2], self.data[i * 2 + 1])

    def __getitem__(self, idx):
        return self.data[self.size + idx]

    def __setitem__(self, idx, value):
        i = self.size + idx
        self.data[i] = value
        while i > 1:
            i //= 2
            self.data[i] = self.func(self.data[2 * i], self.data[2 * i + 1])

    def query(self, l, r):
        l += self.size
        r += self.size
        res_left = self.default
        res_right = self.default
        while l < r:
            if l % 2 == 1:
                res_left = self.func(res_left, self.data[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                res_right = self.func(self.data[r], res_right)
            l //= 2
            r //= 2
        return self.func(res_left, res_right)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    return x % m

n, k = map(int, input().split())
p = list(map(lambda x: int(x) - 1, input().split()))

out = 0
mod = 998244353

mult_r = (k - 1) * modinv(k, mod) % mod
mult_inv = modinv(mult_r, mod)
mult = 1
inv = 1

seg = SegmentTree([0] * n, func=lambda x, y: x + y)
seg2 = SegmentTree([0] * n, func=lambda x, y: x + y)

for i in range(n):
    if i >= k:
        mult = (mult * mult_r) % mod
        inv = (inv * mult_inv) % mod

    expected_above = (seg.query(p[i], n) * mult) % mod
    expected_below = (seg.query(0, p[i]) * mult) % mod

    tot_above = seg2.query(p[i], n)

    temp = (tot_above - modinv(2, mod) * expected_above) % mod
    temp2 = (modinv(2, mod) * expected_below) % mod
    out = (out + temp + temp2) % mod

    seg[p[i]] = inv
    seg2[p[i]] = 1

print(out)