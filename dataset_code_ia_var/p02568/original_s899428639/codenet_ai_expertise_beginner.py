class LazySegmentTree:
    def __init__(self, a, e, op, id_, mapping, composition):
        self.e = e
        self.op = op
        self.id = id_
        self.mapping = mapping
        self.composition = composition
        self.n = len(a)
        size = 1
        while size < self.n:
            size <<= 1
        self.size = size
        self.tree = [e] * (2 * size)
        self.lazy = [id_] * size
        # set leaves
        for i in range(self.n):
            self.tree[size + i] = a[i]
        # build tree
        for i in range(size - 1, 0, -1):
            self.tree[i] = op(self.tree[i << 1], self.tree[(i << 1) | 1])

    def _push(self, k):
        if self.lazy[k] == self.id:
            return
        self._apply(k << 1, self.lazy[k])
        self._apply((k << 1) | 1, self.lazy[k])
        self.lazy[k] = self.id

    def _apply(self, k, f):
        self.tree[k] = self.mapping(f, self.tree[k])
        if k < self.size:
            if self.lazy[k] == self.id:
                self.lazy[k] = f
            else:
                self.lazy[k] = self.composition(f, self.lazy[k])

    def _pull(self, k):
        while k > 1:
            k >>= 1
            self.tree[k] = self.op(self.tree[k << 1], self.tree[(k << 1) | 1])
            if self.lazy[k] != self.id:
                self.tree[k] = self.mapping(self.lazy[k], self.tree[k])

    def apply_range(self, l, r, f):
        l0, r0 = l + self.size, r + self.size
        l1, r1 = l0, r0
        h = self.size.bit_length()
        # push down
        for i in range(h, 0, -1):
            if ((l1 >> i) << i) != l1:
                self._push(l1 >> i)
            if ((r1 >> i) << i) != r1:
                self._push((r1 - 1) >> i)
        l2, r2 = l0, r0
        while l2 < r2:
            if l2 & 1:
                self._apply(l2, f)
                l2 += 1
            if r2 & 1:
                r2 -= 1
                self._apply(r2, f)
            l2 >>= 1
            r2 >>= 1
        # pull up
        for i in range(1, h + 1):
            if ((l0 >> i) << i) != l0:
                self._pull(l0 >> i)
            if ((r0 >> i) << i) != r0:
                self._pull((r0 - 1) >> i)

    def prod(self, l, r):
        l += self.size
        r += self.size
        h = self.size.bit_length()
        for i in range(h, 0, -1):
            if ((l >> i) << i) != l:
                self._push(l >> i)
            if ((r >> i) << i) != r:
                self._push((r - 1) >> i)
        sml = self.e
        smr = self.e
        while l < r:
            if l & 1:
                sml = self.op(sml, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op(self.tree[r], smr)
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

MOD = 998244353

def range_affine_range_sum():
    import sys
    input = sys.stdin.buffer.readline
    N, Q = map(int, input().split())
    lst = list(map(int, input().split()))
    A = [(x << 32) + 1 for x in lst]
    e = 1
    id_ = 1 << 32

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

    seg = LazySegmentTree(A, e, op, id_, mapping, composition)
    ans = []
    for _ in range(Q):
        arr = list(map(int, input().split()))
        if arr[0] == 1:
            l, r = arr[1], arr[2]
            val = seg.prod(l, r) >> 32
            ans.append(str(val))
        else:
            l, r, b, c = arr[1], arr[2], arr[3], arr[4]
            seg.apply_range(l, r, (b << 32) + c)
    print('\n'.join(ans))

if __name__ == '__main__':
    range_affine_range_sum()