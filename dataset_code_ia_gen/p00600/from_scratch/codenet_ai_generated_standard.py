import sys
sys.setrecursionlimit(10**7)

class UnionFind:
    def __init__(self,n):
        self.par=list(range(n))
        self.rank=[0]*n
    def find(self,x):
        while self.par[x]!=x:
            self.par[x]=self.par[self.par[x]]
            x=self.par[x]
        return x
    def union(self,x,y):
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

def main():
    input=sys.stdin.readline
    while True:
        s,d=map(int,input().split())
        if s==0 and d==0:
            break
        edges=[]
        # hot springs idx: 0 to s-1
        # districts idx: s to s+d-1
        for i in range(s):
            dist=list(map(int,input().split()))
            for j,x in enumerate(dist):
                if x!=0:
                    edges.append((x,i,s+j))
        for i in range(d-1):
            line=list(map(int,input().split()))
            for j,x in enumerate(line):
                if x!=0:
                    u=s+i
                    v=s+i+1+j
                    edges.append((x,u,v))
        edges.sort()
        uf=UnionFind(s+d)
        ans=0
        for w,u,v in edges:
            if uf.union(u,v):
                ans+=w
        print(ans)
if __name__=="__main__":
    main()