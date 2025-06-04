import sys

class SegTree:
    '''区間演算 & 一点変更'''
    def __init__(s, N, O, E):
        s.sz = 1
        while s.sz < N: s.sz <<= 1
        s.el = E
        s._N = N
        s.opr = O
        s.dat = [E]*(s.sz<<1)
    def builder(this, arr):
        for i, val in enumerate(arr):
            this.dat[this.sz + i] = val
        for k in range(this.sz-1,0,-1):
            this.dat[k] = this.opr(this.dat[k<<1], this.dat[(k<<1)|1])
    def set(self, idx, value):
        p = idx + self.sz
        self.dat[p] = value
        while p>1:
            p//=2
            self.dat[p]=self.opr(self.dat[p*2],self.dat[p*2+1])
    def prod(me, left, right):
        l=left+me.sz; r=right+me.sz
        lres=me.el; rres=me.el
        while l<r:
            (lres:=me.opr(lres,me.dat[l])) if l&1 else None
            l += l&1
            r -= r&1; rres = me.opr(me.dat[r],rres) if r&1 else rres
            l>>=1;r>>=1
        return me.opr(lres, rres)

read = sys.stdin.readline
A,B = list(map(int,input().split()))
T = input()
LIMIT = 10**18
st=SegTree(A+1,min,LIMIT)
st.set(A,0)

for idx in reversed(range(A)):
    if T[idx]=='1': continue
    t = st.prod(idx+1, min(A+1, idx+B+1)) + 1
    st.set(idx, t)

if st.prod(0,1) >= LIMIT:
    print(-1)
    quit()

ret,ptr=[],0
for x in range(A+1):
    if st.prod(ptr,ptr+1)-1==st.prod(x,x+1):
        ret+=[x-ptr]
        ptr=x
print(*ret)