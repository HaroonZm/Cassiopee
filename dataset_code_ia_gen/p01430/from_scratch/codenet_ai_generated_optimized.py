import sys
input=sys.stdin.readline

from collections import deque

class MaxFlow:
    def __init__(self,n):
        self.n=n
        self.g=[[] for _ in range(n)]
    def add_edge(self,a,b,c):
        self.g[a].append([b,c,len(self.g[b])])
        self.g[b].append([a,0,len(self.g[a])-1])
    def bfs(self,s,t,level):
        q=deque([s])
        level[s]=0
        while q:
            v=q.popleft()
            lv=level[v]+1
            for i,(to,cap,rev) in enumerate(self.g[v]):
                if cap and level[to]<0:
                    level[to]=lv
                    q.append(to)
        return level[t]>=0
    def dfs(self,v,t,f,level,it):
        if v==t:
            return f
        while it[v]<len(self.g[v]):
            to,cap,rev=self.g[v][it[v]]
            if cap>0 and level[v]<level[to]:
                d=self.dfs(to,t,min(f,cap),level,it)
                if d>0:
                    self.g[v][it[v]][1]-=d
                    self.g[to][rev][1]+=d
                    return d
            it[v]+=1
        return 0

def max_flow(mf,s,t):
    flow=0
    INF=10**9
    level=[-1]*mf.n
    while True:
        for i in range(mf.n):
            level[i]=-1
        if not mf.bfs(s,t,level):
            return flow
        it=[0]*mf.n
        while True:
            f=mf.dfs(s,t,INF,level,it)
            if f==0:
                break
            flow+=f

N,E,Q=map(int,input().split())
edges=set()
adj=[set() for _ in range(N)]
for _ in range(E):
    f,t_=map(int,input().split())
    f-=1
    t_-=1
    edges.add((f,t_))
    edges.add((t_,f_:=t_))
    adj[f].add(t_)
    adj[t_].add(f)
queries=[]
for _ in range(Q):
    M,A,B=map(int,input().split())
    A-=1
    B-=1
    queries.append((M,A,B))

for M,A,B in queries:
    if M==1:
        adj[A].add(B)
        adj[B].add(A)
    else:
        adj[A].discard(B)
        adj[B].discard(A)

    mf=MaxFlow(N)
    for u in range(N):
        for v in adj[u]:
            # capacity 1 for each edge
            mf.add_edge(u,v,1)
    print(max_flow(mf,0,N-1))