class Fenwick:
    def __init__(self, N):
        self.N = N
        self.A = [0]*(N+2)
    def _prefix(self, j):
        res=0
        idx=j
        while idx>0:
            res += self.A[idx]
            idx -= idx&-idx
        return res
    def updt(self, idx, delta):
        while idx<=self.N+1:
            self.A[idx]+=delta
            idx+=idx&-idx

class RUQ:
    def __init__(self, length):
        def f():return Fenwick(length+2)
        self.bit0, self.bit1 = f(), f()
    def apply(self, l, r, val):
        r+=1
        for BIT, mult in [(self.bit0, -l*val), (self.bit0, r*val)]:
            BIT.updt(l if mult<0 else r, mult)
        for B, d in [(self.bit1, val), (self.bit1, -val)]:
            B.updt(l if d>0 else r, d)
    def get(self, left, right):
        right+=1
        def calc(x):return self.bit0._prefix(x)+self.bit1._prefix(x)*x
        return calc(right)-calc(left)

if __name__=='__main__':
    n,k=[int(e) for e in input().split()]
    T=RUQ(n)
    for __ in range(k):
        parts=list(map(int,input().split()))
        if parts[0]<1:
            T.apply(parts[1],parts[2],parts[3])
        else:
            print(T.get(parts[1],parts[2]))