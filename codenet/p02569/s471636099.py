import sys
input = sys.stdin.readline

class Lazysegtree:
    def __init__(self, A, fx, ex, fm, em, fa, initialize = True):
        # Aの入力形式は要素が(0の数,1の数,転倒数)のtupleになっている配列
        self.n = len(A)
        self.n0 = 2**(self.n-1).bit_length() 
        self.fm = fm # fm:モノイド関数を指定
        self.ex = ex # 単位元と遅延評価用の数字を突っ込むためのtuple
        self.em = em # 遅延評価後のtreeに仕込む元
        self.lazy = [em]*(2*self.n0) # 遅延評価後のtree配列
        if initialize: # Aをself.dataに仕込む
            self.data = [self.ex]*self.n0 + A + [self.ex]*(self.n0 - self.n)
            for i in range(self.n0-1, -1, -1):
                self.data[i] = self.fx(self.data[i*2], self.data[i*2+1])
                # 偶数index × 奇数indexをしてtreeの上側を更新
        else: # Aを仕込まないときは元で穴埋め
            self.data = [self.ex]*(2*self.n0)
    def fx(self, x, y): # クエリ関数、今回は転倒数
        return (x[0]+y[0], x[1]+y[1], x[2]+y[2]+x[1]*y[0])

    def fa(self, ope, idx):
        if ope == 0:
            return self.data[idx]
        zero, one, t = self.data[idx]
        return (one, zero, (one+zero)*(one+zero-1)//2 - one*(one-1)//2 - zero*(zero-1)//2 - t)

    def _ascend(self, k): # treeを登って更新
        k = k >> 1
        c = k.bit_length()
        for j in range(c):
            idx = k >> j
            self.data[idx] = self.fx(self.data[2*idx], self.data[2*idx+1])
            
    def _descend(self, k):  # treeを降りて更新
        k = k >> 1          # 降りるときに遅延評価後のtreeも更新
        idx = 1
        c = k.bit_length()
        for j in range(1, c+1):
            idx = k >> (c - j)
            if self.lazy[idx] == self.em:
                continue
            self.data[2*idx] = self.fa(self.lazy[idx], 2*idx) 
            self.data[2*idx+1] = self.fa(self.lazy[idx], 2*idx+1)
            self.lazy[2*idx] = self.fm(self.lazy[idx], self.lazy[2*idx])
            self.lazy[2*idx+1] = self.fm(self.lazy[idx], self.lazy[2*idx+1])
            self.lazy[idx] = self.em

    def query(self, l, r): # [l,r)のクエリ関数の出力
        L = l+self.n0
        R = r+self.n0
        self._descend(L//(L & -L))
        self._descend(R//(R & -R)-1)
        
        sl = self.ex
        sr = self.ex                                                                   

        while L < R:
            if R & 1:
                R -= 1
                sr = self.fx(self.data[R], sr)
            if L & 1:
                sl = self.fx(sl, self.data[L])
                L += 1
            L >>= 1
            R >>= 1
        return self.fx(sl, sr)
    
    def operate(self, l, r, x): # [l,r)の各yに対してfm(x,y)をする
        L = l+self.n0
        R = r+self.n0
        Li = L//(L & -L)
        Ri = R//(R & -R)
        self._descend(Li)
        self._descend(Ri-1)
        
        while L < R :
            if R & 1:
                R -= 1
                self.data[R] = self.fa(x, R)
                self.lazy[R] = self.fm(x, self.lazy[R])
            if L & 1:
                self.data[L] = self.fa(x, L)
                self.lazy[L] = self.fm(x, self.lazy[L])
                L += 1
            L >>= 1
            R >>= 1
        
        self._ascend(Li)
        self._ascend(Ri-1)

N, Q = map(int, input().split())
*A, = map(int, input().split())
A = [(0, 1, 0) if a == 1 else (1, 0, 0) for a in A]
segtree = Lazysegtree(A, None, (0, 0, 0), lambda x,y:x^y, 0, None, initialize = True)

ans = []
for i in range(Q):
    t,l,r = map(int, input().split())
    if t == 1:
        segtree.operate(l-1, r, 1)
    else:
        ans.append(segtree.query(l-1, r)[2])

for i in range(len(ans)):
    print(ans[i])