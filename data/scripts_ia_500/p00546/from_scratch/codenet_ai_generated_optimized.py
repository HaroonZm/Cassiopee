import sys
import heapq
from collections import deque

input=sys.stdin.readline

N,M,K,S=map(int,input().split())
P,Q=map(int,input().split())

zombies=set()
for _ in range(K):
    c=int(input())
    zombies.add(c)

graph=[[] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# S本以下の道を通って到達できる町を危険な町とするため、
# ゾンビの町を起点にして距離Sまで広げる（多点BFS）

danger=[False]*(N+1)
dist=[-1]*(N+1)
que=deque()

for z in zombies:
    dist[z]=0
    que.append(z)

while que:
    v=que.popleft()
    if dist[v]==S:
        continue
    for nv in graph[v]:
        if dist[nv]==-1:
            dist[nv]=dist[v]+1
            danger[nv]=True
            que.append(nv)

# 町1と町Nはゾンビ支配外なのでdanger[1]とdanger[N]はFalse改めてセットしとく
danger[1]=False
danger[N]=False

# ダイクストラで宿泊費最小ルートを探索
# 状態は町 i でのコスト
# 移動するたびに移動先町で一晩宿泊(町1,町Nは宿泊不要)
# 危険な町ならQ円、危険でない町ならP円
INF=10**18
cost=[INF]*(N+1)
cost[1]=0
hq=[(0,1)]

while hq:
    c,v=heapq.heappop(hq)
    if cost[v]<c:
        continue
    if v==N:
        print(c)
        break
    for nv in graph[v]:
        # 宿泊費は移動先町で発生(町1,町Nはなし)
        nc=c + (Q if danger[nv] else P) if nv!=N else c
        if cost[nv]>nc:
            cost[nv]=nc
            heapq.heappush(hq,(nc,nv))