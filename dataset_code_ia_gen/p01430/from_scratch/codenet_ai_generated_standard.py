import sys
from collections import deque
input=sys.stdin.readline

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
            for i,(to,cap,rev) in enumerate(self.g[v]):
                if cap>0 and level[to]<0:
                    level[to]=level[v]+1
                    q.append(to)
        return level[t]>=0
    def dfs(self,v,t,f,level,iter):
        if v==t:
            return f
        while iter[v]<len(self.g[v]):
            to,cap,rev=self.g[v][iter[v]]
            if cap>0 and level[v]<level[to]:
                d=self.dfs(to,t,min(f,cap),level,iter)
                if d>0:
                    self.g[v][iter[v]][1]-=d
                    self.g[to][rev][1]+=d
                    return d
            iter[v]+=1
        return 0
    def max_flow(self,s,t):
        flow=0
        INF=10**9
        level=[-1]*self.n
        while self.bfs(s,t,level):
            iter=[0]*self.n
            while True:
                f=self.dfs(s,t,INF,level,iter)
                if f==0:
                    break
                flow+=f
            level=[-1]*self.n
        return flow

N,E,Q=map(int,input().split())
edges=set()
for _ in range(E):
    f,t_=map(int,input().split())
    a,b=f-1,t_-1
    if a>b:
        a,b=b,a
    edges.add((a,b))
queries=[]
for _ in range(Q):
    M,A,B=map(int,input().split())
    a,b=A-1,B-1
    if a>b:
        a,b=b,a
    queries.append((M,a,b))

for M,a,b in queries:
    if M==1:
        edges.add((a,b))
    else:
        edges.remove((a,b))
    mf=MaxFlow(N)
    for x,y in edges:
        mf.add_edge(x,y,1)
        mf.add_edge(y,x,1)
    print(mf.max_flow(0,N-1))