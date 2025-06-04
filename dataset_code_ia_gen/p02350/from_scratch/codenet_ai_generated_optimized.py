import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline

INF = 2**31 - 1

class SegmentTree:
    def __init__(self,n):
        self.N=1
        while self.N<n:
            self.N <<=1
        self.minv=[INF]*(2*self.N)
        self.lazy=[None]*(2*self.N)

    def _push(self,i,l,r):
        if self.lazy[i] is not None:
            self.minv[i]=self.lazy[i]
            if l!=r:
                self.lazy[2*i]=self.lazy[i]
                self.lazy[2*i+1]=self.lazy[i]
            self.lazy[i]=None

    def _update(self,i,l,r,ql,qr,x):
        self._push(i,l,r)
        if r<ql or qr<l:
            return
        if ql<=l and r<=qr:
            self.lazy[i]=x
            self._push(i,l,r)
            return
        m=(l+r)//2
        self._update(2*i,l,m,ql,qr,x)
        self._update(2*i+1,m+1,r,ql,qr,x)
        self.minv[i]=min(self.minv[2*i],self.minv[2*i+1])

    def update(self,ql,qr,x):
        self._update(1,0,self.N-1,ql,qr,x)

    def _query(self,i,l,r,ql,qr):
        self._push(i,l,r)
        if r<ql or qr<l:
            return INF
        if ql<=l and r<=qr:
            return self.minv[i]
        m=(l+r)//2
        return min(self._query(2*i,l,m,ql,qr),self._query(2*i+1,m+1,r,ql,qr))

    def query(self,ql,qr):
        return self._query(1,0,self.N-1,ql,qr)

n,q=map(int,input().split())
st=SegmentTree(n)
for _ in range(q):
    line=input().split()
    if line[0]=='0':
        _,s,t,x=line
        s,t,x=int(s),int(t),int(x)
        st.update(s,t,x)
    else:
        _,s,t=line
        s,t=int(s),int(t)
        print(st.query(s,t))