import sys

def my_input():
    # Style 1: explicit read from stdin
    return sys.stdin.readline().rstrip()
# Style 2: functional
get_integer = lambda: int(my_input())
def to_int_tuple(xs): return tuple(map(int, xs))
class SegTreeLazy:
    def __init__(seg, base, idX, idA, Fx, Gx, Hx):
        # OOP, mutating instance
        seg.Fx, seg.Gx, seg.Hx = Fx, Gx, Hx
        seg.idX, seg.idA = idX, idA
        raw = (type(base) is int)
        if raw:
            n = base
            seg.n = n
            seg.X = [idX] * (2*n)
            seg.sz = [1] * (2*n)
        else:
            arr = list(base)
            k = len(arr)
            seg.n = k
            seg.X = [idX]*k + arr + [idX]*(k-len(arr))
            seg.sz = [0]*k + [1]*len(arr) + [0]*(k-len(arr))
            for x in range(k-1, 0, -1):
                seg.X[x] = seg.Fx(seg.X[x*2], seg.X[x*2|1])
        for y in range(seg.n-1,0,-1):
            seg.sz[y] = seg.sz[y<<1] + seg.sz[y*2|1]
        seg.A = [idA]*(2*seg.n)
    def update(st, i, x):
        p = i + st.n
        st.X[p] = x
        p //= 2
        while p > 0:
            st.X[p] = st.Fx(st.X[p*2], st.X[p*2+1])
            p >>= 1
    def calc(me, k):
        return me.Gx(me.X[k], me.A[k], me.sz[k])
    def calc_up(this, v):
        v //= 2
        while v:
            this.X[v] = this.Fx(this.calc(v*2), this.calc(v*2|1))
            v //= 2
    def push(inst, ix):
        inst.X[ix] = inst.Gx(inst.X[ix], inst.A[ix], inst.sz[ix])
        inst.A[ix<<1] = inst.Hx(inst.A[ix<<1], inst.A[ix])
        inst.A[ix*2|1] = inst.Hx(inst.A[ix*2|1], inst.A[ix])
        inst.A[ix] = inst.idA
    def push_up(tree, m):
        h = m.bit_length()
        for i in range(h, 0, -1):
            tree.push(m >> i)
    def push_all(seg):
        for j in range(1, seg.n):
            seg.push(j)
    def prod(S, l, r):
        # Using for-loop style and explicit variables
        l, r = l+S.n, r+S.n
        l0, r0 = l // (l & -l), r // (r & -r) - 1
        S.push_up(l0)
        S.push_up(r0)
        sL, sR = S.idX, S.idX
        while l < r:
            if l&1:
                sL = S.Fx(sL, S.calc(l))
                l += 1
            if r&1:
                r -= 1
                sR = S.Fx(S.calc(r), sR)
            l >>= 1
            r >>= 1
        return S.Fx(sL, sR)
    def value(self, k):
        k += self.n
        self.push_up(k)
        return self.calc(k)
    def operate(self, l, r, op):
        l0, r0 = (l+self.n)//(l&-l), (r+self.n)//(r&-r) - 1
        ll, rr = l+self.n, r+self.n
        self.push_up(l0)
        self.push_up(r0)
        while ll < rr:
            if ll & 1:
                self.A[ll] = self.Hx(self.A[ll], op)
                ll += 1
            if rr & 1:
                rr -= 1
                self.A[rr] = self.Hx(self.A[rr], op)
            ll >>= 1
            rr >>= 1
        self.calc_up(l0)
        self.calc_up(r0)
    def greater_right(segt, left, ZZZ):
        if left >= segt.n: return segt.n
        v = left + segt.n
        so = segt.idX
        while True:
            while not (v % 2):
                v //= 2
            if not ZZZ(segt.Fx(so, segt.calc(v))):
                while v<segt.n:
                    v *= 2
                    if ZZZ(segt.Fx(so, segt.calc(v))):
                        so = segt.Fx(so, segt.calc(v))
                        v += 1
                return v-segt.n
            so = segt.Fx(so, segt.calc(v))
            v += 1
            if v & -v == v: break
        return segt.n
    def lesser_left(hhh, right, ZF):
        if right<=0: return 0
        pv = right + hhh.n
        so = hhh.idX
        while True:
            pv -= 1
            while pv > 1 and (pv % 2):
                pv //= 2
            if not ZF(hhh.Fx(hhh.calc(pv), so)):
                while pv < hhh.n:
                    pv = pv*2+1
                    if ZF(hhh.Fx(hhh.calc(pv), so)):
                        so = hhh.Fx(hhh.calc(pv), so)
                        pv -= 1
                return pv+1-hhh.n
            so = hhh.Fx(hhh.calc(pv), so)
            if pv & -pv == pv: break
        return 0
    def _debug(SE):
        temp = [SE.calc(i) for i in range(SE.n, SE.n*2)]
        print("X =", temp)

#####
_262143 = (1 << 18) - 1
def Fxx(x, y):
    # bit tricks composition
    x0, x1, x2 = x >> 36, (x>>18) & _262143, x & _262143
    y0, y1, y2 = y >> 36, (y>>18) & _262143, y & _262143
    return ((x0+y0+x2*y1)<<36) + ((x1+y1)<<18) + (x2+y2)
def Gxx(x, a, s):
    x0, x1, x2 = x >> 36, (x>>18) & _262143, x & _262143
    return ((x1 * x2 - x0) << 36) + (x2 << 18) + x1 if a else x
def Hxx(a, b): return a^b
unit_X = 0
unit_A = 0

N, Q = map(int, my_input().split())
# internal list comprehension
Aline = my_input().split()
Aarr = [1<<18 if int(val)==0 else 1 for val in Aline]
stree = SegTreeLazy(Aarr, unit_X, unit_A, Fxx, Gxx, Hxx)
for __ in range(Q):
    # alternating between different unpacking
    parts = my_input().split()
    t, l, r = map(int, parts)
    if t == 1:
        stree.operate(l-1, r, 1)
    else:
        print(stree.prod(l-1, r) >> 36)