import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7)

class SegmentTree:
    def __init__(self, n):
        self.n=1
        while self.n<n:
            self.n*=2
        self.data=[0]*(2*self.n-1)
        self.lazy=[0]*(2*self.n-1)

    def eval(self, k, l, r):
        if self.lazy[k]!=0:
            self.data[k]+=self.lazy[k]
            if r-l>1:
                self.lazy[2*k+1]+=self.lazy[k]
                self.lazy[2*k+2]+=self.lazy[k]
            self.lazy[k]=0

    def add(self, a, b, x, k=0, l=0, r=None):
        if r is None:
            r=self.n
        self.eval(k,l,r)
        if b<=l or r<=a:
            return
        if a<=l and r<=b:
            self.lazy[k]+=x
            self.eval(k,l,r)
        else:
            m=(l+r)//2
            self.add(a,b,x,2*k+1,l,m)
            self.add(a,b,x,2*k+2,m,r)
            self.data[k]=min(self.data[2*k+1],self.data[2*k+2])

    def find_min(self, a, b, k=0, l=0, r=None):
        if r is None:
            r=self.n
        self.eval(k,l,r)
        if b<=l or r<=a:
            return float('inf')
        if a<=l and r<=b:
            return self.data[k]
        else:
            m=(l+r)//2
            vl=self.find_min(a,b,2*k+1,l,m)
            vr=self.find_min(a,b,2*k+2,m,r)
            return min(vl,vr)

n,q=map(int,input().split())
st=SegmentTree(n)
for _ in range(q):
    query=list(map(int,input().split()))
    if query[0]==0:
        _,s,t,x=query
        st.add(s,t+1,x)
    else:
        _,s,t=query
        print(st.find_min(s,t+1))