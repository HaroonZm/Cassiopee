# 2冪

# 同じインデックスの重複を除くので、関数の呼び出し回数が少し少ないはず。
# ただ、重複を除く分のオーバーヘッドがあるので、
# fmm, fmo, fooが軽い関数だと、スピードはそこまで出ない。

class LazySegmentTree:

    __slots__ = ["n", "original_size", "log", "data", "lazy", "me", "oe", "fmm", "fmo", "foo"]

    def __init__(self, monoid_data, monoid_identity, operator_identity, func_monoid_monoid, func_monoid_operator, func_operator_operator):
        self.me = monoid_identity
        self.oe = operator_identity
        self.fmm = func_monoid_monoid
        self.fmo = func_monoid_operator
        self.foo = func_operator_operator

        self.original_size = len(monoid_data)
        self.log = (self.original_size - 1).bit_length()
        self.n = 1 << self.log
        self.data = [self.me] * self.n + monoid_data + [self.me] * (self.n - self.original_size)
        for i in range(self.n-1, 0, -1):
            self.data[i] = self.fmm(self.data[2*i], self.data[2*i+1])
        self.lazy = [self.oe] * (self.n * 2)
        

    def replace(self, index, value):
        index += self.n

        # propagation
        for shift in range(self.log, 0, -1):
            i = index >> shift
            self.lazy[2*i]   = self.foo(self.lazy[2*i],   self.lazy[i])
            self.lazy[2*i+1] = self.foo(self.lazy[2*i+1], self.lazy[i])
            self.data[i] = self.fmo(self.data[i], self.lazy[i])
            self.lazy[i] = self.oe

        # update
        self.data[index] = value
        self.lazy[index] = self.oe

        # recalculation
        i = index
        while i > 1:
            i //= 2
            self.data[i] = self.fmm( self.fmo(self.data[2*i], self.lazy[2*i]), self.fmo(self.data[2*i+1], self.lazy[2*i+1]) )
            self.lazy[i] = self.oe

    def effect(self, l, r, operator):
        l += self.n
        r += self.n
        
        # preparing indices (参考: http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=3561258#1)
        indices = []
        L = l // 2
        R = r // 2
        lc = 0 if l % 2 else (L & -L).bit_length()
        rc = 0 if r % 2 else (R & -R).bit_length()
        for i in range(self.log):
            if rc <= i:
                indices.append(R)
            if L < R and lc <= i:
                indices.append(L)
            L //= 2
            R //= 2

        # propagation
        for i in reversed(indices):
            self.lazy[2*i]   = self.foo(self.lazy[2*i],   self.lazy[i])
            self.lazy[2*i+1] = self.foo(self.lazy[2*i+1], self.lazy[i])
            self.data[i] = self.fmo(self.data[i], self.lazy[i])
            self.lazy[i] = self.oe

        # effect
        while l < r:
            if l % 2:
                self.lazy[l] = self.foo(self.lazy[l], operator)
                l += 1
            if r % 2:
                r -= 1
                self.lazy[r] = self.foo(self.lazy[r], operator)
            l //= 2
            r //= 2

        # recalculation
        for i in indices:
            self.data[i] = self.fmm( self.fmo(self.data[2*i], self.lazy[2*i]), self.fmo(self.data[2*i+1], self.lazy[2*i+1]) )
            self.lazy[i] = self.oe
            
        
    def folded(self, l, r):
        l += self.n
        r += self.n

        # preparing indices
        indices = []
        L = l // 2
        R = r // 2
        lc = 0 if l % 2 else (L & -L).bit_length()
        rc = 0 if r % 2 else (R & -R).bit_length()
        for i in range(self.log):
            if rc <= i:
                indices.append(R)
            if L < R and lc <= i:
                indices.append(L)
            L //= 2
            R //= 2
        
        # propagation
        for i in reversed(indices):
            self.lazy[2*i]   = self.foo(self.lazy[2*i],   self.lazy[i])
            self.lazy[2*i+1] = self.foo(self.lazy[2*i+1], self.lazy[i])
            self.data[i] = self.fmo(self.data[i], self.lazy[i])
            self.lazy[i] = self.oe

        # fold
        left_folded = self.me
        right_folded = self.me
        while l < r:
            if l % 2:
                left_folded = self.fmm(left_folded, self.fmo(self.data[l], self.lazy[l]))
                l += 1
            if r % 2:
                r -= 1
                right_folded = self.fmm(self.fmo(self.data[r], self.lazy[r]), right_folded)
            l //= 2
            r //= 2
        return self.fmm(left_folded, right_folded)

def atc2():
    # Monoid:   ((0の数), (1の数), (転倒数))
    # Operator: 反転するか? (1 or 0) 

    import sys
    input = sys.stdin.buffer.readline

    N, Q = map(int, input().split())
    monoid_data = [(0, 1, 0) if A == b'1' else (1, 0, 0) for A in input().split()]

    def fmm(m1, m2):
        return (m1[0] + m2[0], m1[1] + m2[1], m1[2] + m2[2] + m1[1] * m2[0])

    def fmo(m1, o1):
        if o1:
            return (m1[1], m1[0], m1[0] * m1[1] - m1[2])
        else:
            return m1 

    def foo(o1, o2):
        return o1 ^ o2

    lst = LazySegmentTree(monoid_data, (0, 0, 0), 0, fmm, fmo, foo)
    ans = []
    for _ in range(Q):
        T, L, R = map(int, input().split())
        if T == 1:
            lst.effect(L-1, R, 1)
        else:
            ans.append(lst.folded(L-1, R)[2])
    print('\n'.join(map(str, ans)))

if __name__ == "__main__":
    atc2()