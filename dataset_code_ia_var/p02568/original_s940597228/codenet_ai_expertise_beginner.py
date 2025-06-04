mod = 998244353

class LazySegtree:
    def __init__(self, arr):
        if type(arr) == int:
            n = arr
            self.n = n
            arr = [self.e()] * n
        else:
            self.n = len(arr)
        self.log = 0
        n = self.n
        while (1 << self.log) < n:
            self.log += 1
        self.size = 1 << self.log
        self.d = [self.e()] * (2 * self.size)
        self.lz = [self.identity()] * self.size
        for i in range(len(arr)):
            self.d[self.size + i] = arr[i]
        for i in range(self.size - 1, 0, -1):
            self.update(i)

    def update(self, k):
        self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])

    def push(self, k):
        self.all_apply(2 * k, self.lz[k])
        self.all_apply(2 * k + 1, self.lz[k])
        self.lz[k] = self.identity()

    def all_apply(self, k, f):
        self.d[k] = self.mapping(f, self.d[k])
        if k < self.size:
            self.lz[k] = self.composition(f, self.lz[k])

    def set_x(self, p, x):
        p += self.size
        for i in range(self.log, 0, -1):
            self.push(p >> i)
        self.d[p] = x
        for i in range(1, self.log + 1):
            self.update(p >> i)

    def get(self, p):
        p += self.size
        for i in range(self.log, 0, -1):
            self.push(p >> i)
        return self.d[p]

    def prod(self, l, r):
        l += self.size
        r += self.size
        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                self.push(l >> i)
            if ((r >> i) << i) != r:
                self.push((r - 1) >> i)
        sml = self.e()
        smr = self.e()
        while l < r:
            if l % 2 == 1:
                sml = self.op(sml, self.d[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                smr = self.op(self.d[r], smr)
            l //= 2
            r //= 2
        return self.op(sml, smr)

    def apply(self, p, f):
        p += self.size
        for i in range(self.log, 0, -1):
            self.push(p >> i)
        self.d[p] = self.mapping(f, self.d[p])
        for i in range(1, self.log + 1):
            self.update(p >> i)

    def range_apply(self, l, r, f):
        if l == r:
            return
        l += self.size
        r += self.size
        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                self.push(l >> i)
            if ((r >> i) << i) != r:
                self.push((r - 1) >> i)
        l2 = l
        r2 = r
        while l < r:
            if l % 2 == 1:
                self.all_apply(l, f)
                l += 1
            if r % 2 == 1:
                r -= 1
                self.all_apply(r, f)
            l //= 2
            r //= 2
        l = l2
        r = r2
        for i in range(1, self.log + 1):
            if ((l >> i) << i) != l:
                self.update(l >> i)
            if ((r >> i) << i) != r:
                self.update((r - 1) >> i)

    def op(self, a, b):
        return ((a[0] + b[0]) % mod, a[1] + b[1])

    def e(self):
        return (0, 0)

    def identity(self):
        return (1, 0)

    def mapping(self, f, x):
        fa, fb = f
        xa, xb = x
        return ((fa * xa + fb * xb) % mod, xb)

    def composition(self, f, g):
        fa, fb = f
        ga, gb = g
        return ((fa * ga) % mod, (gb * fa + fb) % mod)

if __name__ == '__main__':
    import sys
    input = sys.stdin.buffer.readline
    sys.setrecursionlimit(10000000)

    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    init = []
    for a in A:
        init.append((a, 1))
    seg = LazySegtree(init)
    for _ in range(Q):
        tmp = list(map(int, input().split()))
        if tmp[0] == 0:
            _, l, r, c, d = tmp
            seg.range_apply(l, r, (c, d))
        else:
            _, l, r = tmp
            ans = seg.prod(l, r)[0]
            print(ans)