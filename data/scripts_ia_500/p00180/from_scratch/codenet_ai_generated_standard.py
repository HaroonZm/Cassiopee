import sys
input=sys.stdin.readline

class UnionFind:
    def __init__(self,n):
        self.par=list(range(n))
        self.rank=[0]*n
    def find(self,x):
        while self.par[x]!=x:
            self.par[x]=self.par[self.par[x]]
            x=self.par[x]
        return x
    def unite(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if x==y:
            return False
        if self.rank[x]<self.rank[y]:
            self.par[x]=y
        else:
            self.par[y]=x
            if self.rank[x]==self.rank[y]:
                self.rank[x]+=1
        return True

while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    edges=[]
    for _ in range(m):
        a,b,c=map(int,input().split())
        edges.append((c,a,b))
    edges.sort()
    uf=UnionFind(n)
    ans=0
    for c,a,b in edges:
        if uf.unite(a,b):
            ans+=c
    print(ans)