import sys
input=sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.par=list(range(n))
        self.rank=[0]*n
    def find(self, x):
        while self.par[x]!=x:
            self.par[x]=self.par[self.par[x]]
            x=self.par[x]
        return x
    def unite(self, x, y):
        x=self.find(x)
        y=self.find(y)
        if x==y: return
        if self.rank[x]<self.rank[y]:
            self.par[x]=y
        else:
            self.par[y]=x
            if self.rank[x]==self.rank[y]:
                self.rank[x]+=1
    def same(self, x, y):
        return self.find(x)==self.find(y)

n,m=map(int,input().split())
uf=UnionFind(n)
for _ in range(m):
    s,t=map(int,input().split())
    uf.unite(s,t)
q=int(input())
for _ in range(q):
    s,t=map(int,input().split())
    print("yes" if uf.same(s,t) else "no")