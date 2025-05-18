class LazySegmentTree():
    def __init__(self, op, e, mapping, composition, ie, init_array):
        self.op = op
        self.e = e
        self.mapping = mapping
        self.composition = composition
        self.ie = ie

        l = len(init_array)
        def ceil_pow2(n):
            x = 0
            while (1 << x) < n:
                x += 1
            return x
        self.log = ceil_pow2(l)
        self.size = 1 << self.log
        # self.size = 1 << (l - 1).bit_length()
        # self.h = self.size.bit_length()

        self.d = [self.e() for _ in range(2*self.size)]
        self.lz = [self.ie() for _ in range(self.size)]

        for i, a in enumerate(init_array):
            self.d[i+self.size] = a

        for i in range(self.size-1, 0, -1):
            self.__update(i)

    def set(self, p, x):
        p += self.size

        for i in range(self.log, 0, -1):
            self.__push(p >> i)

        self.d[p] = x

        for i in range(1, self.log+1):
            self.__update(p >> i)

    def __getitem__(self, p):
        p += self.size
        for i in range(self.log, 0, -1):
            self.__push(p >> i)
        return self.d[p]

    def prod(self, l, r):
        if l == r:
            return self.e()

        l += self.size
        r += self.size

        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                self.__push(l >> i)
            if ((r >> i) << i) != r:
                self.__push(r >> i)

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

    # def apply(self, p, f):
    #     p += self.size

    #     for i in range(self.h, 0, -1):
    #         self.__push(p >> i)

    #     self.d[p] = self.mapping(f, self.d[p])

    #     for i in range(1, self.h+1):
    #         self.__update(p >> i)

    def apply(self, l, r, f):
        if l == r:
            return

        l += self.size
        r += self.size

        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                self.__push(l >> i)
            if ((r >> i) << i) != r:
                self.__push((r-1) >> i)

        l2 = l
        r2 = r
        while l < r:
            if l & 1:
                self.__all_apply(l, f)
                l += 1
            if r & 1:
                r -= 1
                self.__all_apply(r, f)
            l >>= 1
            r >>= 1
        l = l2
        r = r2

        for i in range(1, self.log+1):
            if ((l >> i) << i) != l:
                self.__update(l >> i)
            if ((r >> i) << i) != r:
                self.__update((r-1) >> i)

    def __update(self, k):
        self.d[k] = self.op(self.d[2*k], self.d[2*k+1])

    def __all_apply(self, k, f):
        self.d[k] = self.mapping(f, self.d[k])
        if k < self.size:
            self.lz[k] = self.composition(f, self.lz[k])

    def __push(self, k):
        self.__all_apply(2*k, self.lz[k])
        self.__all_apply(2*k+1, self.lz[k])
        self.lz[k] = self.ie()

def atcoder_practice_k():
    import sys
    input = sys.stdin.buffer.readline
    N, Q = map(int, input().split())
    A = list(map(lambda x: (int(x)<<32) +1, input().split()))
    MOD = 998244353
    def e():
        return 0

    def op(s, t):
        sv, sn = s >> 32, s % (1 << 32)
        tv, tn = t >> 32, t % (1 << 32)
        return (((sv + tv) % MOD) << 32) + sn + tn

    def mapping(f, a):
        fb, fc = f >> 32, f % (1 << 32)
        av, an = a >> 32, a % (1 << 32)
        return (((fb * av + fc * an) % MOD) << 32) + an

    def composition(f, g):
        fb, fc = f >> 32, f % (1 << 32)
        gb, gc = g >> 32, g % (1 << 32)
        return ((fb * gb % MOD) << 32) + ((gc * fb + fc) % MOD)

    def ie():
        return 1 << 32
    # op = lambda l, r: ((l[0] + r[0])%M, (l[1] + r[1])%M)
    # e = lambda: (0, 0)
    # mapping = lambda l, r: ((r[0] * l[0] + r[1] * l[1])%M, r[1])
    # composition = lambda l, r: ((r[0] * l[0])%M, (r[1] * l[0] + l[1])%M)
    # ie = lambda: (1, 0)

    st = LazySegmentTree(op, e, mapping, composition, ie, A)
    for _ in range(Q):
        k, *q  = map(int, input().split())
        if k == 0:
            l, r, b, c = q
            st.apply(l, r, (b<<32) + c)
        else:
            l, r = q
            a = st.prod(l, r)
            print(a >> 32)

if __name__ == "__main__":
    atcoder_practice_k()