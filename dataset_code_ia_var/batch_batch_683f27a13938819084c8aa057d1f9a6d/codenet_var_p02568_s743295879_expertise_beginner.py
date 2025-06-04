class LazySegmentTree:
    def __init__(self, op, e, mapping, composition, ie, init_array):
        # On enregistre toutes les fonctions et valeurs neutres nécessaires
        self.op = op
        self.e = e
        self.mapping = mapping
        self.composition = composition
        self.ie = ie

        n = len(init_array)
        pow2 = 1
        log = 0
        while pow2 < n:
            pow2 *= 2
            log += 1
        self.size = pow2
        self.log = log

        self.d = [self.e() for _ in range(2 * self.size)]
        self.lz = [self.ie() for _ in range(self.size)]

        # On place les éléments de l'array de départ
        for i in range(n):
            self.d[self.size + i] = init_array[i]

        # On construit l'arbre
        for i in range(self.size - 1, 0, -1):
            self._update(i)
    
    def set(self, p, x):
        p += self.size
        for i in range(self.log, 0, -1):
            self._push(p >> i)
        self.d[p] = x
        for i in range(1, self.log + 1):
            self._update(p >> i)
    
    def __getitem__(self, p):
        p += self.size
        for i in range(self.log, 0, -1):
            self._push(p >> i)
        return self.d[p]
    
    def prod(self, l, r):
        if l == r:
            return self.e()

        l += self.size
        r += self.size

        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                self._push(l >> i)
            if ((r >> i) << i) != r:
                self._push((r - 1) >> i)

        left = self.e()
        right = self.e()

        while l < r:
            if l % 2:
                left = self.op(left, self.d[l])
                l += 1
            if r % 2:
                r -= 1
                right = self.op(self.d[r], right)
            l //= 2
            r //= 2

        return self.op(left, right)
    
    def apply(self, l, r, f):
        if l == r:
            return

        l += self.size
        r += self.size

        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                self._push(l >> i)
            if ((r >> i) << i) != r:
                self._push((r-1) >> i)

        l_orig = l
        r_orig = r
        while l < r:
            if l % 2:
                self._all_apply(l, f)
                l += 1
            if r % 2:
                r -= 1
                self._all_apply(r, f)
            l //= 2
            r //= 2
        l = l_orig
        r = r_orig

        for i in range(1, self.log + 1):
            if ((l >> i) << i) != l:
                self._update(l >> i)
            if ((r >> i) << i) != r:
                self._update((r-1) >> i)

    def _update(self, k):
        self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])

    def _all_apply(self, k, f):
        self.d[k] = self.mapping(f, self.d[k])
        if k < self.size:
            self.lz[k] = self.composition(f, self.lz[k])

    def _push(self, k):
        self._all_apply(2 * k, self.lz[k])
        self._all_apply(2 * k + 1, self.lz[k])
        self.lz[k] = self.ie()

def atcoder_practice_k():
    import sys
    input = sys.stdin.buffer.readline
    N, Q = map(int, input().split())
    A = list(map(lambda x: (int(x) << 32) + 1, input().split()))
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

    st = LazySegmentTree(op, e, mapping, composition, ie, A)

    for _ in range(Q):
        query = list(map(int, input().split()))
        k = query[0]
        if k == 0:
            l, r, b, c = query[1:]
            st.apply(l, r, (b << 32) + c)
        else:
            l, r = query[1:]
            a = st.prod(l, r)
            print(a >> 32)

if __name__ == "__main__":
    atcoder_practice_k()