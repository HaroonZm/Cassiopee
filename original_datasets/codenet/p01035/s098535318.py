class SegmentTree(object):
    def __init__(self, a:list, default: int, op):
        from math import ceil, log
        real_size = len(a)
        self.elem_size = elem_size = 1<<ceil(log(real_size, 2))
        self.tree = tree = [default] * (elem_size * 2)
        tree[elem_size:elem_size + real_size] = a
        self.default = default
        self.op = op
        for i in range(elem_size - 1, 0, -1):
            tree[i] = op(tree[i<<1], tree[(i<<1)+1])
    def get_value(self, x:int, y:int):
        l, r = x+self.elem_size, y+self.elem_size
        tree, result, op = self.tree, self.default, self.op
        while l<r:
            if l & 1:
                result = op(tree[l], result)
                l += 1
            if r&1:
                r -= 1
                result = op(tree[r], result)
            l, r = l>>1, r>>1
        return result
    def set_value(self, i:int, value:int):
        k = self.elem_size + i
        self.tree[k] = value
        self.update(k)
    def update(self, i:int):
        op, tree = self.op, self.tree
        while i > 1:
            i >>= 1
            tree[i] = op(tree[i<<1], tree[(i<<1)+1])

N = int(input())
A = list(map(int, input().split()))
Q_ = int(input())
Q = []
for i in range(Q_):
    l, r, d = map(int, input().split())
    Q.append([l, r, d, i])
seg1 = SegmentTree([-1<<30]*N, -1<<30, max)
seg2 = SegmentTree(A, 1<<30, min)
from operator import itemgetter
Q.sort(key=itemgetter(2))
A = sorted(zip(A, range(N)), key=itemgetter(0))

a_idx = 0
Ans = [0] * Q_
for l, r, d, q_idx in Q:
    while a_idx < N:
        a0, a1 = A[a_idx]
        if a0 > d:
            break
        else:
            seg1.set_value(a1, a0)
            seg2.set_value(a1, 1<<30)
            a_idx += 1
    an1 = abs(seg1.get_value(l, r+1) - d)
    an2 = abs(seg2.get_value(l, r+1) - d)
    Ans[q_idx] = min(an1, an2)

print(*Ans, sep="\n")