import sys
input=sys.stdin.readline

class Fenwick:
    def __init__(self,n):
        self.n=n
        self.BIT=[0]*(n+1)
    def update(self,i,x):
        while i<=self.n:
            self.BIT[i]+=x
            i+=i&(-i)
    def query(self,i):
        s=0
        while i>0:
            s+=self.BIT[i]
            i-=i&(-i)
        return s

n,q=map(int,input().split())
bit1=Fenwick(n)
bit2=Fenwick(n)

def range_add(l,r,x):
    bit1.update(l,x)
    bit1.update(r+1,-x)
    bit2.update(l,x*(l-1))
    bit2.update(r+1,-x*r)

def prefix_sum(i):
    return bit1.query(i)*i - bit2.query(i)

for _ in range(q):
    query=list(map(int,input().split()))
    if query[0]==0:
        _,s,t,x=query
        range_add(s,t,x)
    else:
        _,s,t=query
        print(prefix_sum(t)-prefix_sum(s-1))