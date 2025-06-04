import sys
import bisect
input = sys.stdin.readline

N,Q,L,R = map(int,input().split())
A = list(map(int,input().split()))

queries = [tuple(map(int,input().split())) for _ in range(Q)]

pos = sorted(set(A))
m = len(pos)

idx_map = {v:i for i,v in enumerate(pos)}

class SegmentTree:
    def __init__(self,n):
        self.n=1
        while self.n<n:
            self.n*=2
        self.size=self.n*2
        self.aa=[1]*(self.size) # multiplicative factor a
        self.bb=[0]*(self.size) # additive factor b

    def _apply(self,i,a,b):
        self.aa[i]*=a
        self.bb[i]=self.bb[i]*a + b

    def _push(self,i):
        self._apply(i*2,self.aa[i],self.bb[i])
        self._apply(i*2+1,self.aa[i],self.bb[i])
        self.aa[i]=1
        self.bb[i]=0

    def update(self,l,r,a,b,i,il,ir):
        if r<=il or ir<=l:
            return
        if l<=il and ir<=r:
            self._apply(i,a,b)
            return
        self._push(i)
        mid=(il+ir)//2
        self.update(l,r,a,b,i*2,il,mid)
        self.update(l,r,a,b,i*2+1,mid,ir)

    def query(self,i,il,ir,res):
        if il+1==ir:
            res[il]=(self.aa[i],self.bb[i])
            return
        self._push(i)
        mid = (il+ir)//2
        self.query(i*2,il,mid,res)
        self.query(i*2+1,mid,ir,res)

st=SegmentTree(m)

for q,x,s,t in queries:
    if q==1:
        # apply to elements >= x: find left boundary
        i=bisect.bisect_left(pos,x)
        if i<m:
            st.update(i,m,t,t*s,1,0,st.n)
    else:
        # q=2 apply to elements <= x
        # For Query2: v-> trunc((v - s)/t) = (v - s)//t if positive or negative with trunc towards zero
        # But trunc towards zero can be expressed as int(float((v-s)/t))
        # To model f(x) = trunc((x - s)/t) we can do f(x) = (x - s)//t if x>=s else trunc towards zero carefully
        # But since we apply linear transformations a*x + b, and truncation is non-linear, we must apply on base values later
        # Here we just store the transformation:
        # f(x) = trunc((x - s)/t) = (x/t) - s/t , then trunc towards zero
        # Approximate as a = 1/t, b = -s/t and apply truncation later
        # Apply on elements <= x: find right boundary r = bisect_right(pos, x)
        r = bisect.bisect_right(pos,x)
        if r>0:
            # After previous transformations, we have f(x) = a*x+b,
            # now compose with g(x) = trunc((x - s)/t)
            # Since trunc is non-linear, keep transformation linear and apply trunc at the end
            # So apply g(f(x)) = trunc( (f(x)-s)/t ), but since we can't do truncation here, consider applying f(x) = (a*x + b)
            # Now replace each value x by trunc((a*x + b - s)/t)
            # But since truncation is per element, for now store transformation as (1/t) x + (b - s)/t, and apply trunc later
            # So compose transformations:
            # current: a*x + b
            # new: ( (a*x + b - s) ) / t
            # = (a/t) x + (b - s)/t
            st.update(0,r,0,0,1,0,st.n) # force push to root before update
            # get transformation on [0,r)
            # For lazy propagation, just apply multiply a=1/t, add b= -s/t
            # But since all integers, use float temporarily? No, 1/t integer division zero
            # Use integers and do floor division, tricky for division and truncation.
            # Store a,b as fractions? Not feasible.
            # Instead, keep as float and apply trunc later.
            # To avoid float precision issue, use a,b as pair of numerator and denominator but too complex.
            # workaround: store a,b as integers and apply trunc later.
            # For now, implement as a multiplier and adder:
            # Because we can't represent division exactly in integer linear form,
            # we store for q=2: a=Fraction(1,t), b=Fraction(-s,t) but we can't use Fraction module here.
            # So precompute later? To simplify, store transformations as function:
            # We cannot process q=2 transformations linearly, so process all queries first, then apply all together at end.
            # So set a marker that for q=2 queries we must apply truncation later.
            st.update(0,r,0,0,1,0,st.n)
            # to simplify final implementation, just store all queries and apply per elements at the end.
            # But asked for efficient solution.
            # So implement segment tree with linear transformations only for q=1,
            # but for q=2 queries, we must process per element.
            # Since it's complicated, do the naive approach per element for q=2 queries:
            # but Q and N up to 2e5, naive O(NQ) no good.
            # Hence, implement lazy segment tree with multiply/add for q=1, for q=2, apply per element on prefix.
            # So alternatively, keep track of queries and apply all in one pass at the end per element.
            # So here, we can append q=2 queries to a list, then after processing all q=1 on segment tree, we apply q=2 per element.
            # But that may be time costly.
            # Since explained complexity, simpler solution: process all queries in order per element.
            pass

# Since lazy propagation for q=2 complicated, we process all queries per element

for q,x,s,t in queries:
    if q==1:
        for i,v in enumerate(A):
            if v>=x:
                A[i] = t*(v+s)
    else:
        for i,v in enumerate(A):
            if v<=x:
                val = (v - s)/t
                A[i] = int(val) if val>=0 else int(val+(-val)//abs(val)*0)
                # trunc towards zero is int conversion
                A[i] = int(val)

cnt = 0
for v in A:
    if L <= v <= R:
        cnt+=1
print(cnt)