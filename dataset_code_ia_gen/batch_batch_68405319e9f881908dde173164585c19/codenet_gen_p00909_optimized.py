import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline

class WeightedUnionFind:
    def __init__(self,n):
        self.par = list(range(n))
        self.rank = [0]*n
        self.diff = [0]*n  # diff[x] = w[x] - w[parent[x]]

    def find(self,x):
        if self.par[x] == x:
            return x
        r = self.find(self.par[x])
        self.diff[x] += self.diff[self.par[x]]
        self.par[x] = r
        return r

    def unite(self,x,y,w): # w = w[y]-w[x]
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return
        # make ry child of rx
        if self.rank[rx] < self.rank[ry]:
            rx,ry = ry,rx
            w = -w
        self.par[ry] = rx
        self.diff[ry] = self.diff[x]-self.diff[y]+w
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

    def same(self,x,y):
        return self.find(x) == self.find(y)

    def diff_w(self,x,y):
        if not self.same(x,y):
            return None
        return self.diff[y]-self.diff[x]

while True:
    N,M=map(int,input().split())
    if N==0 and M==0:
        break
    wuf=WeightedUnionFind(N)
    for _ in range(M):
        line=input().split()
        if line[0]=='!':
            a,b,w=int(line[1])-1,int(line[2])-1,int(line[3])
            wuf.unite(a,b,w)
        else:
            a,b=int(line[1])-1,int(line[2])-1
            res=wuf.diff_w(a,b)
            print(res if res is not None else "UNKNOWN")