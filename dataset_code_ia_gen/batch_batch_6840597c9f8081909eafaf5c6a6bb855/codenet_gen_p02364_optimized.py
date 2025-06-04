import sys
input=sys.stdin.readline

class DSU:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[0]*n
    def find(self,x):
        while self.parent[x]!=x:
            self.parent[x]=self.parent[self.parent[x]]
            x=self.parent[x]
        return x
    def union(self,x,y):
        rx,ry=self.find(x),self.find(y)
        if rx==ry:
            return False
        if self.rank[rx]<self.rank[ry]:
            self.parent[rx]=ry
        else:
            self.parent[ry]=rx
            if self.rank[rx]==self.rank[ry]:
                self.rank[rx]+=1
        return True

V,E=map(int,input().split())
edges=[tuple(map(int,input().split())) for _ in range(E)]
edges.sort(key=lambda x:x[2])

dsu=DSU(V)
mst_sum=0
for s,t,w in edges:
    if dsu.union(s,t):
        mst_sum+=w
print(mst_sum)