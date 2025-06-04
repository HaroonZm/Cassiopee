import sys

def readln(): return sys.stdin.readline()

class LAZYSEG: 
    def __init__(S, arr, *_f, initialize=True): 
        S.n = len(arr); S.n0 = 1 << (S.n-1).bit_length()
        S.fx = (lambda x, y: (x[0]+y[0], x[1]+y[1], x[2]+y[2]+x[1]*y[0])) if _f[0] is None else _f[0]
        S.ex = (0, 0, 0) if _f[1] is None else _f[1]
        S.fm = (lambda x, y: x^y) if _f[2] is None else _f[2]
        S.em = 0 if _f[3] is None else _f[3]
        S.fa = lambda op, idx: S.data[idx] if op == 0 else (lambda a,b,c: (b,a,(a+b)*(a+b-1)//2 - b*(b-1)//2 - a*(a-1)//2-c))(*S.data[idx])
        S.lazy = [S.em] * (2*S.n0)
        S.data = [S.ex]*S.n0 + list(arr) + [S.ex]*(S.n0 - S.n) if initialize else [S.ex]*(2*S.n0)
        if initialize:
            for z in range(S.n0-1, 0, -1): S.data[z] = S.fx(S.data[2*z], S.data[2*z+1])
    def _ascend(S, k):
        p = k >> 1
        for _ in range(p.bit_length()):
            S.data[p] = S.fx(S.data[p<<1], S.data[p<<1|1])
            p >>=1
    def _descend(self, ndx):
        k = ndx >> 1
        for j in range(k.bit_length(),0,-1):
            i = k >> (j-1)
            if self.lazy[i] == self.em: continue
            for m in (i<<1, i<<1|1):
                self.data[m] = self.fa(self.lazy[i], m)
                self.lazy[m] = self.fm(self.lazy[i], self.lazy[m])
            self.lazy[i] = self.em
    def query(ss, le, ri):
        l, r = le+ss.n0, ri+ss.n0
        ss._descend(l//(l&-l))
        ss._descend((r//(r&-r))-1)
        sl,sr = ss.ex, ss.ex
        while l < r:
            if r & 1: r -= 1; sr = ss.fx(ss.data[r], sr)
            if l & 1: sl = ss.fx(sl, ss.data[l]); l += 1
            l >>= 1; r >>= 1
        return ss.fx(sl, sr)
    def operate(Ss, s, e, v):
        l, r = s+Ss.n0, e+Ss.n0
        Li, Ri = l//(l & -l), r//(r & -r)
        Ss._descend(Li)
        Ss._descend(Ri-1)
        while l < r:
            if r & 1: r -= 1; Ss.data[r] = Ss.fa(v, r); Ss.lazy[r] = Ss.fm(v, Ss.lazy[r])
            if l & 1: Ss.data[l] = Ss.fa(v, l); Ss.lazy[l] = Ss.fm(v, Ss.lazy[l]); l += 1
            l >>= 1; r >>= 1
        Ss._ascend(Li)
        Ss._ascend(Ri-1)

def many_ints(): return map(int, readln().split())
N,Q = many_ints()
A = [int(s) for s in readln().split()]
tupleize = lambda a: (0,1,0) if a==1 else (1,0,0)
ST = LAZYSEG(list(map(tupleize, A)), None, (0,0,0), None, 0, None, initialize=True)
res, app = [], res.append
for _ in range(Q):
    t,l,r = many_ints()
    if t == 1: ST.operate(l-1, r, 1)
    else: app(ST.query(l-1, r)[2])
for x in res: print(x)