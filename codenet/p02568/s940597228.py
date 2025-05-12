mod = 998244353

class lazy_segtree(object):

    def __init__(self, n_or_vec):
        if isinstance(n_or_vec, int):
            self.n = n_or_vec
            v = [self.e()] * n_or_vec
        elif isinstance(n_or_vec, list) or isinstance(n_or_vec, tuple):
            self.n = len(n_or_vec)
            v = n_or_vec
        self.log = (self.n - 1).bit_length()
        self.size = 1 << self.log
        self.d = [self.e()] * (2 * self.size)
        self.lz = [self.identity()] * self.size
        for i, vi in enumerate(v):
            self.d[self.size + i] = vi
        for i in reversed(range(1, self.size)):
            self.update(i)

    def update(self, k):
        self.d[k] = self.op(self.d[2*k], self.d[2*k+1])

    def all_apply(self, k, f):
        self.d[k] = self.mapping(f, self.d[k])
        if k < self.size:
            self.lz[k] = self.composition(f, self.lz[k])

    def push(self, k):
        self.all_apply(2*k, self.lz[k])
        self.all_apply(2*k+1, self.lz[k])
        self.lz[k] = self.identity()

    def set_x(self, p, x):
        p += self.size
        for i in reversed(range(1, self.log + 1)):
            self.push(p >> i)
        self.d[p] = x
        for i in range(1, self.log + 1):
            self.update(p >> i)

    def get(self, p):
        p += self.size
        for i in reversed(range(1, self.log + 1)):
            self.push(p >> i)
        return self.d[p]

    def show(self):
        print("show array")
        for i in range(self.n):
            print(self.get(i), end=" ")
        print("\n")

    def prod(self, l, r):
        if l == r:
            return self.e()
        l += self.size
        r += self.size
        for i in reversed(range(1, self.log + 1)):
            if ((l >> i) << i) != l:
                self.push(l >> i)
            if ((r >> i) << i) != r:
                self.push(r >> i)
        sml = self.e()
        smr = self.e()
        while l < r:
            if l & 1:
                sml = self.op(sml, self.d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op(self.d[r], smr)
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def all_prod(self):
        return self.d[1]

    def apply(self, p, f):
        p += self.size
        for i in reversed(range(1, self.log + 1)):
            self.push(p >> i)
        self.d[p] = self.mapping(f, self.d[p])
        for i in range(1, self.log + 1):
            self.update(p >> i)

    def range_apply(self, l, r, f):
        if l == r:
            return
        l += self.size
        r += self.size
        for i in reversed(range(1, self.log + 1)):
            if ((l >> i) << i) != l:
                self.push(l >> i)
            if ((r >> i) << i) != r:
                self.push((r - 1) >> i)

        l2, r2 = l, r
        while l < r:
            if l & 1:
                self.all_apply(l, f)
                l += 1
            if r & 1:
                r -= 1
                self.all_apply(r, f)
            l >>= 1
            r >>= 1
        l, r = l2, r2

        for i in range(1, self.log + 1):
            if ((l >> i) << i) != l:
                self.update(l >> i)
            if ((r >> i) << i) != r:
                self.update((r - 1) >> i)

    def max_right(self, l, g, target):
        if l == self.n:
            return self.n
        l += self.size
        for i in reversed(range(1, self.log + 1)):
            self.push(l >> i)
        sm = self.e()
        while True:
            while l % 2 == 0:
                l >>= 1
            if not g(self.op(sm, self.d[l]), target):
                while l < self.size:
                    self.push(l)
                    l = (2 * l)
                    if g(self.op(sm, self.d[l]), target):
                        sm = self.op(sm, self.d[l])
                        l += 1
                return l - self.size
            sm = self.op(sm, self.d[l])
            l += 1
            if l & -l == l:
                break
        return self.n

    def min_left(self, r, g, target):
        if r == 0:
            return 0
        r += self.size
        for i in reversed(range(1, self.log + 1)):
            self.push((r - 1) >> i)
        sm = self.e()
        while True:
            r -= 1
            while r > 1 and (r % 2):
                r >>= 1
            if not g(self.op(self.d[r], sm), target):
                while r < self.size:
                    self.push(r)
                    r = (2 * r + 1)
                    if g(self.op(self.d[r], sm), target):
                        sm = self.op(self.d[r], sm)
                        r -= 1
                return r + 1 - self.size
            sm = self.op(self.d[r], sm)
            if r & -r == r:
                break
        return 0

    def op(self, L, R):
        La, Lsize = L
        Ra, Rsize = R
        return (La + Ra) % mod, Lsize + Rsize

    def e(self):
        return (0, 0)

    def identity(self):
        return (1, 0)

    def mapping(self, L, R):
        La, Lb = L
        Ra, Rsize = R
        return (La * Ra + Lb * Rsize) % mod, Rsize

    def composition(self, L, R):
        La, Lb = L
        Ra, Rb = R
        return (La * Ra) % mod, (Rb * La + Lb) % mod

if __name__ == "__main__":
    import sys
    input = sys.stdin.buffer.readline
    sys.setrecursionlimit(10 ** 7)

    N, Q = map(int, input().split())
    A = [(a, 1) for a in map(int, input().split())]

    lazyseg = lazy_segtree(A)
    #lazyseg = lazy_segtree(A, op, e, mapping, composition, identity)

    for _ in range(Q):
        t, *arg = map(int, input().split())
        if t == 0:
            l, r, c, d = arg
            lazyseg.range_apply(l, r, (c, d))
        else:
            l, r = arg
            print(lazyseg.prod(l, r)[0])