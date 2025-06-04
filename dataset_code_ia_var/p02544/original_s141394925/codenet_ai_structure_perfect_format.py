class SegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()
        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size
        res_left = res_right = self._default
        while start < stop:
            if start & 1:
                res_left = self._func(res_left, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self._func(self.data[stop], res_right)
            start >>= 1
            stop >>= 1
        return self._func(res_left, res_right)

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)

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
    else:
        return x % m

n, k = map(int, input().split())
p = list(map(lambda x: int(x) - 1, input().split()))

out = 0
mod = 998244353

mult_r = (k - 1) * modinv(k, mod)
mult_inv = modinv(mult_r, mod)
mult = 1
inv = 1

seg = SegmentTree([0] * n, func=lambda x, y: x + y)
seg2 = SegmentTree([0] * n, func=lambda x, y: x + y)

for i in range(n):
    if i >= k:
        mult *= mult_r
        mult %= mod
        inv *= mult_inv
        inv %= mod

    expected_above = (seg.query(p[i], n) * mult) % mod
    expected_below = (seg.query(0, p[i]) * mult) % mod
    tot_above = seg2.query(p[i], n)

    out += tot_above - modinv(2, mod) * (expected_above)
    out += modinv(2, mod) * (expected_below)
    out %= mod

    seg[p[i]] = inv
    seg2[p[i]] = 1

print(out)