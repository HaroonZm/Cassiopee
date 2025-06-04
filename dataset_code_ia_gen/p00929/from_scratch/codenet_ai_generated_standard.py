import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [0]*n
    def find(self,x):
        while self.parent[x]!=x:
            self.parent[x]=self.parent[self.parent[x]]
            x=self.parent[x]
        return x
    def unite(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if x==y: return False
        if self.rank[x]<self.rank[y]:
            self.parent[x]=y
        else:
            self.parent[y]=x
            if self.rank[x]==self.rank[y]:
                self.rank[x]+=1
        return True
    def same(self,x,y):
        return self.find(x)==self.find(y)

N,M=map(int,input().split())
edges=[]
for i in range(M):
    s,d,c=map(int,input().split())
    edges.append((c,s-1,d-1,i))
edges.sort(key=lambda x:x[0])

uf=UnionFind(N)
res=[False]*M
i=0
while i<M:
    w=edges[i][0]
    group=[]
    while i<M and edges[i][0]==w:
        group.append(edges[i])
        i+=1
    compid={}
    compcount=0
    for e in group:
        a=uf.find(e[1])
        b=uf.find(e[2])
        if a!=b:
            if a not in compid:
                compid[a]=compcount
                compcount+=1
            if b not in compid:
                compid[b]=compcount
                compcount+=1
    if compcount==0:
        continue
    g=[[] for _ in range(compcount)]
    for e in group:
        a=uf.find(e[1])
        b=uf.find(e[2])
        if a!=b:
            u=compid[a]
            v=compid[b]
            g[u].append((v,e[3]))
            g[v].append((u,e[3]))
    # find bridges in this graph
    used=[False]*compcount
    ord=[-1]*compcount
    low=[-1]*compcount
    time=0
    ans_set=set()
    def dfs(v,p):
        nonlocal time
        used[v]=True
        ord[v]=low[v]=time
        time+=1
        for to,eid in g[v]:
            if eid not in ans_set:
                pass
            if not used[to]:
                dfs(to,v)
                low[v]=min(low[v],low[to])
                if low[to]>ord[v]:
                    ans_set.add(eid)
            elif to!=p:
                low[v]=min(low[v],ord[to])
    for v in range(compcount):
        if not used[v]:
            dfs(v,-1)
    # mark edges which are bridges
    for e in group:
        a=uf.find(e[1])
        b=uf.find(e[2])
        if a!=b and e[3] in ans_set:
            res[e[3]]=True
    # unite all edges in group
    for e in group:
        uf.unite(e[1],e[2])

count=0
cost=0
for i,(c,s,d,idx) in enumerate(edges):
    if res[idx]:
        count+=1
        cost+=c
print(count,cost)