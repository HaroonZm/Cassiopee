import heapq
from collections import deque
from functools import reduce
N,M,X=map(int,(lambda s:s.replace('\n',' ').split())(input()))
H=[0]+list(map(lambda _:int(input()),range(N)))
graph=[[] for _ in range(N+1)]
add_edge=lambda u,v,c:(graph[u].append((v,c)) if H[u]>=c else None,graph[v].append((u,c)) if H[v]>=c else None)
[*map(lambda _:add_edge(*map(int,input().split())),range(M))]
INF=10**10
visited=[False]*(N+1)
costs=[INF]*(N+1)
class HeapNode:
    __slots__=['cost','node','h']
    def __init__(self,cost,node,h):self.cost,self.node,self.h=cost,node,h
    def __lt__(self,other):return self.cost < other.cost
q=[HeapNode(0,1,X)]
costs[1]=0
last_pos=0
def complicated_calc(p,nt,nh,Hn,cn,cost):
    conditions = (
        (lambda:((lambda climbUp: (cost+climbUp+cn,0) if climbUp <= Hn else (INF,0))(nt-p)) if nt-p>0 else INF),
        (lambda:((lambda climbDown: (cost+climbDown+cn,Hn) if climbDown>=0 else (INF,nh))(p-(Hn+nt))) if p-nt>Hn else INF),
        (lambda:(cost+cn, p-nt))
    )
    r = (conditions[0]() if nt-p>0 else conditions[1]() if p-nt>Hn else conditions[2]())
    if isinstance(r,int): return (INF, nh)
    return r
while q:
    curr=heapq.heappop(q)
    if visited[curr.node]:continue
    visited[curr.node]=True
    if(curr.node==N):last_pos=curr.h;break
    for to,cost_edge in graph[curr.node]:
        if visited[to]:continue
        nextCost,nextH=complicated_calc(curr.h,cost_edge,H[to],H[curr.node],cost_edge,curr.cost)
        if nextCost<costs[to]:costs[to]=nextCost;heapq.heappush(q,HeapNode(nextCost,to,nextH))
print(-1 if costs[N]==INF else costs[N]+H[N]-last_pos)