class LazySegmentTree:
    def __init__(self, op_X, e_X, mapping, compose, id_M, N, array=None):
        __slots__ = ["op_X","e_X","mapping","compose","id_M","N","log","N0","data","lazy"]
        #  それぞれ Xの演算、単位元、f(x),  f\circ g, Xの恒等変換
        self.e_X = e_X; self.op_X = op_X; self.mapping = mapping; self.compose = compose; self.id_M = id_M
        self.N = N
        self.log = (N-1).bit_length()
        self.N0 = 1<<self.log
        self.data = [e_X]*(2*self.N0)
        self.lazy = [id_M]*self.N0
        if array is not None:
            assert N == len(array)
            self.data[self.N0:self.N0+self.N] = array
            for i in range(self.N0-1,0,-1): self.update(i)

    # 1点更新
    def point_set(self, p, x):
        p += self.N0
        for i in range(self.log, 0,-1):
            self.push(p>>i)
        self.data[p] = x
        for i in range(1, self.log + 1):
            self.update(p>>i)
 
    # 1点取得
    def point_get(self, p):
        p += self.N0
        for i in range(self.log, 0, -1):
            self.push(p>>i)
        return self.data[p]
 
    # 半開区間[L,R)をopでまとめる
    def prod(self, l, r):
        if l == r: return self.e_X
        l += self.N0
        r += self.N0
        for i in range(self.log, 0, -1):
            if (l>>i)<<i != l:
                self.push(l>>i)
            if (r>>i)<<i != r:
                self.push(r>>i)

        sml = smr = self.e_X
        while l < r:
            if l & 1: 
                sml = self.op_X(sml, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op_X(self.data[r], smr)
            l >>= 1
            r >>= 1
        return self.op_X(sml, smr)
 
    # 全体をopでまとめる
    def all_prod(s): return self.data[1]
 
    # 1点作用
    def apply(self, p, f):
        p += self.N0
        for i in range(self.log, 0, -1):
            self.push(p>>i)
        self.data[p] = self.mapping(f, self.data[p])
        for i in range(1, self.log + 1):
            self.update(p>>i)
 
    # 区間作用
    def apply(self, l, r, f):
        if l == r: return
        l += self.N0
        r += self.N0
        for i in range(self.log, 0, -1):
            if (l>>i)<<i != l:
                self.push(l>>i)
            if (r>>i)<<i != r:
                self.push((r-1)>>i)

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
            if (l>>i)<<i != l:
                self.update(l>>i)
            if (r>>i)<<i != r:
                self.update((r-1)>>i)
     
    """
    始点 l を固定
    f(x_l*...*x_{r-1}) が True になる最大の r 
    つまり TTTTFFFF となるとき、F となる最小の添え字
    存在しない場合 n が返る
    f(e_M) = True でないと壊れる
    """
    def max_right(self, l, g):
        if l == self.N: return self.N
        l += self.N0
        for i in range(self.log, 0, -1): self.push(l>>i)
        sm = self.e_X
        while True:
            while l&1 == 0:
                l >>= 1
            if not g(self.op_X(sm, self.data[l])):
                while l < self.N0:
                    self.push(l)
                    l *= 2
                    if g(self.op_X(sm, self.data[l])):
                        sm = self.op_X(sm, self.data[l])
                        l += 1
                return l - self.N0
            sm = self.op_X(sm, self.data[l])
            l += 1
            if l&-l == l: break
        return self.N
 
    """
    終点 r を固定
    f(x_l*...*x_{r-1}) が True になる最小の l
    つまり FFFFTTTT となるとき、T となる最小の添え字
    存在しない場合 r が返る
    f(e_M) = True でないと壊れる
    """
    def min_left(self, r, g):
        if r == 0: return 0
        r += self.N0
        for i in range(self.log, 0, -1): self.push((r-1)>>i)
        sm = self.e_X
        while True:
            r -= 1
            while r>1 and r&1:
                r >>= 1
            if not g(self.op_X(self.data[r], sm)):
                while r < self.N0:
                    self.push(r)
                    r = 2*r + 1
                    if g(self.op_X(self.data[r], sm)):
                        sm = self.op_X(self.data[r], sm)
                        r -= 1
                return r + 1 - self.N0
            sm = self.op_X(self.data[r], sm)
            if r&-r == r: break
        return 0
        
    # 以下内部関数
    def update(self, k):
        self.data[k] = self.op_X(self.data[2*k], self.data[2*k+1])
    
    def all_apply(self, k, f):
        self.data[k] = self.mapping(f, self.data[k])
        if k < self.N0:
            self.lazy[k] = self.compose(f, self.lazy[k])

    def push(self, k): #propagate と同じ
        if self.lazy[k] is self.id_M: return
        self.data[2*k  ] = self.mapping(self.lazy[k], self.data[2*k])
        self.data[2*k+1] = self.mapping(self.lazy[k], self.data[2*k+1])
        if 2*k < self.N0:
            self.lazy[2*k]   = self.compose(self.lazy[k], self.lazy[2*k])
            self.lazy[2*k+1] = self.compose(self.lazy[k], self.lazy[2*k+1])
        self.lazy[k] = self.id_M

###################################################################
#
###################################################################

e_X = 0
id_M = 1<<32
def op_X(X,Y):
    return ((((X+Y)>>32)%MOD)<<32) + ((X+Y)&MASK)
def compose(D,C):
    a = C>>32; b = C&MASK
    c = D>>32; d = D&MASK
    return (a*c%MOD<<32) + (c*b + d)%MOD
def mapping(C,X):
    x = X>>32; v = X&MASK
    a = C>>32; b = C&MASK
    return ((x*a + v*b)%MOD<<32) + v

# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read

n,q = map(int, readline().split())
lr = [list(map(int, readline().split())) for _ in range(q)]

op_X = min
e_X = n-1
mapping = min
compose = min
id_M = n-1

sh = LazySegmentTree(op_X, e_X, mapping, compose, id_M, n, array=[n-1]*(n-1)+[0])
sw = LazySegmentTree(op_X, e_X, mapping, compose, id_M, n, array=[n-1]*(n-1)+[0])

ans = (n-2)**2
for t,x in lr:
    x -= 1
    if t==1:
        #idx = sh.max_right(0, lambda v: v >= x)
        idx = sw.point_get(x)
        sh.apply(1,idx,x)
        ans -= idx-1
        #print(idx,x)
        
    else:
        idx = sh.point_get(x)
        sw.apply(1,idx,x)
        ans -= idx-1
        #print(idx,x)
        #sx.point_set(x,1)

print(ans)