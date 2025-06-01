import sys
import collections
import heapq
sys.setrecursionlimit(10**7)
input=sys.stdin.readline

N,M,K,S=map(int,input().split())
P,Q=map(int,input().split())
zombies=set(int(input()) for _ in range(K))
graph=[[] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dist=[-1]*(N+1)
q=collections.deque()
for z in zombies:
    dist[z]=0
    q.append(z)
while q:
    u=q.popleft()
    if dist[u]==S:
        continue
    for v in graph[u]:
        if dist[v]==-1:
            dist[v]=dist[u]+1
            q.append(v)

INF=10**15
cost=[INF]*(N+1)
cost[1]=0
h=[]
heapq.heappush(h,(0,1))
while h:
    c,u=heapq.heappop(h)
    if cost[u]<c:
        continue
    if u==N:
        print(c)
        break
    for v in graph[u]:
        if v==N:
            nc=c
        else:
            nc=c+(Q if 0<=dist[v]<=S else P)
        if cost[v]>nc:
            cost[v]=nc
            heapq.heappush(h,(nc,v))