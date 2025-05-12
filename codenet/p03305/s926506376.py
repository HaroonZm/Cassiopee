import heapq
import sys
input=sys.stdin.readline
n,m,s,t=map(int,input().split())
edge1=[[] for i in range(n)]
edge2=[[] for i in range(n)]
for i in range(m):
    u,v,a,b=map(int,input().split())
    edge1[u-1].append(a*(10**6)+(v-1))
    edge1[v-1].append(a*(10**6)+(u-1))
    edge2[u-1].append(b*(10**6)+(v-1))
    edge2[v-1].append(b*(10**6)+(u-1)) 

def dijkstra_heap(edge,s):
  d=[float("inf")]*n
  used=[True]*n
  d[s]=0
  used[s]=False
  edgelist=[]
  for e in edge[s]:
    heapq.heappush(edgelist,e)
  while edgelist:
    minedge=heapq.heappop(edgelist)
    minedge_cost=minedge//(10**6)
    minedge_v=minedge%(10**6)
    if not used[minedge_v]:
      continue
    d[minedge_v] = minedge_cost
    used[minedge_v] = False
    for e in edge[minedge_v]:
      e_cost=e//(10**6)
      e_v=e%(10**6)
      if used[e_v]:
        heapq.heappush(edgelist,e+minedge_cost*10**6)
  return d

d1=dijkstra_heap(edge1,s-1)
d2=dijkstra_heap(edge2,t-1)
d=[0]*n

for i in range(n):
  d[i]=d1[i]+d2[i]
for i in range(n-1):
  d[-i-2]=min(d[-i-2],d[-i-1])
for dd in d:
  print(10**15-dd)