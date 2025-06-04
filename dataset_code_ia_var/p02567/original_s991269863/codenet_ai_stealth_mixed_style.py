import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)
def output(x): print(x)

# base SegmentTree functions in OOP (procedural + OOP mix)
class SegTree(object):
    # Use __slots__ to obscure code a bit :-)
    __slots__ = ['N','size','data']
    def __init__(self, n, arr=None):
        N2=1
        while N2<n: N2*=2
        self.N = N2
        self.data = [0]*(2*N2)
        if arr:
            for i, v in enumerate(arr): self.data[N2+i]=v
            for i in range(N2-1,0,-1): self.data[i]=max(self.data[i*2],self.data[i*2+1])
    def update(self, i, x):
        k = self.N + i
        self.data[k] = x
        while k > 1:
            k //= 2
            self.data[k] = max(self.data[k*2], self.data[k*2+1])
    # Query interval [l, r)
    def query(self, l, r):
        L, R = l+self.N, r+self.N
        res = -float('inf')
        while L < R:
            if L&1: res = max(res, self.data[L]); L +=1
            if R&1: R -=1; res = max(res, self.data[R])
            L //=2; R//=2
        return res
    def find_left(self, l, r, x):
        # recursive + functional approach inside OOP
        def go(k, a, b):
            if b <= l or a >= r or self.data[k] < x: return self.N
            if k >= self.N: return k - self.N
            t = go(2*k, a, (a+b)//2)
            if t < self.N: return t
            return go(2*k+1, (a+b)//2, b)
        return go(1, 0, self.N)
    # index of max value in [a,b)
    def query_idx(self, a, b, k=1, l=0, r=None):
        if r is None: r = self.N
        if b<=l or r<=a: return (-float('inf'), -1)
        if a<=l and r<=b: return (self.data[k], self._idx(k))
        x = self.query_idx(a,b,2*k,l,(l+r)//2)
        y = self.query_idx(a,b,2*k+1,(l+r)//2,r)
        return x if x[0]>=y[0] else y
    def _idx(self, k):
        while k<self.N:
            k = k*2 if self.data[k*2]>=self.data[k*2+1] else k*2+1
        return k-self.N

n, q = map(int, input().split())
a = list(map(int, input().split()))
tree = SegTree(n, a)

for _ in range(q):
    tmp = input()
    if not tmp: continue
    # parse line in a functional way on the fly
    t, x, y = list(map(int, tmp.strip().split()))
    # pattern matching by elif
    if t==1:
        tree.update(x-1, y)
    elif t==2:
        output(tree.query(x-1, y))
    else:
        v = tree.find_left(x-1, n, y)+1
        output(v if v<=n else n+1)