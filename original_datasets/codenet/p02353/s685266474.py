class LazySegmentTree:
    """
    op: 区間取得クエリでreduceする際に使う演算子
    apply: 更新則の(n回)適用
    comp: 更新則の合成
    rep: f(x,m)+f(y,m) != f(x+y,m)となる場合に、m^nを高速に計算する用
    
    range_query: reduce(op, (apply(x,m) for x,m in zip(X,M)))
    
    満たすべき性質:
    
    集合X (要素)
    op[+]: X,X -> X
    (X, op)はモノイド
    
    集合M (更新則)
    comp[*]: M,M -> M
    (M, compose)はモノイド
    
    apply[f(x,m,n)]: X,M,Z+ -> X
    (Z+は区間長)
    
    f(x,e_M,n) = x
    f(x,m*n,p) = f(f(x,m,p),n,p)
    f(x,m,p)+f(y,m,q) = f(x+y,m,p+q)
    
    参考: https://algo-logic.info/segment-tree/#toc_id_3
    """
    @classmethod
    def all_identity(cls, op, op_e, comp, comp_e, apply, size):
        size = 2 << (size-1).bit_length()
        return cls(
            op,
            op_e,
            comp,
            comp_e,
            apply,
            [op_e]*size,
            [comp_e]*size
        )

    @classmethod
    def from_initial_data(cls, op, op_e, comp, comp_e, apply, data):
        size = 1 << (len(data)-1).bit_length()
        temp = [op_e]*(2*size)
        temp[size:size+len(data)] = data

        for i in reversed(range(size)):
            temp[i] = op(temp[2*i],temp[2*i+1])
        return cls(
            op,
            op_e,
            comp,
            comp_e,
            apply,
            temp,
            [comp_e]*size
        )

    # これ使わずファクトリーメソッド使いましょうね
    def __init__(self, op, op_e, comp, comp_e, apply, data, lazy):
        self.op = op
        self.op_e = op_e
        self.comp = comp
        self.comp_e = comp_e
        self.apply = apply
        self.data = data
        self.lazy = lazy
        self.size = len(self.data)//2
        self.depth = self.size.bit_length()-1
        self._l_indices = [0]*self.depth
        self._r_indices = [0]*self.depth
    
    def _update_indices(self, i, l):
        m = i//(i&-i)
        i >>= 1
        for k in reversed(range(self.depth)):
            l[k] = i if i < m else 0
            i >>= 1
    
    
    def _propagate_top_down(self):
        data = self.data
        lazy = self.lazy
        apply = self.apply
        comp = self.comp
        comp_e = self.comp_e
        k = self.size >> 1
        
        for i,j in zip(self._l_indices, self._r_indices):
            if i > 0:
                temp = self.lazy[i]
                if temp != comp_e:
                    lazy[i] = comp_e
                    a = i << 1
                    b = (i << 1) | 1
                    lazy[a] = comp(lazy[a], temp)
                    data[a] = apply(data[a], temp, k)
                    lazy[b] = comp(lazy[b], temp)
                    data[b] = apply(data[b], temp, k)
            if i < j:
                temp = self.lazy[j]
                if temp != comp_e:
                    lazy[j] = comp_e
                    a = j << 1
                    b = (j << 1) | 1
                    lazy[a] = comp(lazy[a], temp)
                    data[a] = apply(data[a], temp, k)
                    lazy[b] = comp(lazy[b], temp)
                    data[b] = apply(data[b], temp, k)
            k >>= 1
            
    def _propagate_bottom_up(self):
        data = self.data
        op = self.op
        for i,j in zip(reversed(self._l_indices), reversed(self._r_indices)):
            if i > 0:
                data[i] = op(data[2*i],data[2*i+1])
            if i < j:
                data[j] = op(data[2*j],data[2*j+1])
    
    def update_interval(self, l, r, m):
        lazy = self.lazy
        data = self.data
        comp = self.comp
        apply = self.apply
        
        l += self.size
        r += self.size
        self._update_indices(l, self._l_indices)
        self._update_indices(r, self._r_indices)
        self._propagate_top_down()
        k = 1
        while l < r:
            if l & 1:
                lazy[l] = comp(lazy[l],m)
                data[l] = apply(data[l],m,k)
                l += 1
            if r & 1:
                r -= 1
                lazy[r] = comp(lazy[r],m)
                data[r] = apply(data[r],m,k)
            l >>= 1
            r >>= 1
            k <<= 1
        self._propagate_bottom_up()
    
    def get_interval(self, l, r):
        data = self.data
        op = self.op
        
        l += self.size
        r += self.size
        self._update_indices(l, self._l_indices)
        self._update_indices(r, self._r_indices)
        self._propagate_top_down()
        
        lx = self.op_e
        rx = self.op_e
        while l < r:
            if l & 1:
                lx = op(lx, data[l])
                l += 1
            if r & 1:
                r -= 1
                rx = op(data[r], rx)
            l >>= 1
            r >>= 1
        return op(lx,rx)

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

from operator import add

if __name__ == '__main__':
    n,q = map(int,readline().split())
    temp = map(int,read().split())

    seg = LazySegmentTree.all_identity(
        add,
        0,
        lambda x,y: x if y is None else y,
        None,
        lambda x,m,l: x if m is None else m*l,
        n)

    try:
        while True:
            mode = next(temp)
            if mode:
                l,r = next(temp), next(temp)+1
                print(seg.get_interval(l,r))
            else:
                l,r,x = next(temp), next(temp)+1, next(temp)
                seg.update_interval(l,r,x)
    except StopIteration:
        pass