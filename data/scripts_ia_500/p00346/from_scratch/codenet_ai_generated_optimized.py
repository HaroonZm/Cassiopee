import sys
import heapq
sys.setrecursionlimit(10**7)
input=sys.stdin.readline

N,R=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(R):
    s,t,d=map(int,input().split())
    graph[s].append((t,d))
    graph[t].append((s,d))

def dijkstra(start):
    dist=[float('inf')]*(N+1)
    dist[start]=0
    h=[]
    heapq.heappush(h,(0,start))
    while h:
        cd,u=heapq.heappop(h)
        if dist[u]<cd:
            continue
        for v,w in graph[u]:
            nd=cd+w
            if nd<dist[v]:
                dist[v]=nd
                heapq.heappush(h,(nd,v))
    return dist

# １．全点間最短距離の中で最大の距離をもつ2点を見つける
# ２．その2点間の最短経路上の町を特定する
# ３．最大距離のペアのうち任意の1組を選び、その最短経路の町が大会コースに使われる可能性がある町
# ４．使われる可能性がない町を出力

# まず、全点間の最短距離は Floyd-Warshall はO(N^3)で無理なので、
# 各頂点からdijkstraで距離を求める O(N*R log N)=1500*3000*log1500はギリギリ可能かも。

# そこで、最大距離を持つ2点を見つける
max_dist=0
max_pair=(1,1)
dist_all=[None]*(N+1)
for i in range(1,N+1):
    disti=dijkstra(i)
    dist_all[i]=disti
    for j in range(i+1,N+1):
        if disti[j]>max_dist:
            max_dist=disti[j]
            max_pair=(i,j)

s,g=max_pair

# sからの最短経路を構築するために、親ノードを記録して復元する
def dijkstra_path(start):
    dist=[float('inf')]*(N+1)
    dist[start]=0
    prev=[-1]*(N+1)
    h=[]
    heapq.heappush(h,(0,start))
    while h:
        cd,u=heapq.heappop(h)
        if dist[u]<cd:
            continue
        for v,w in graph[u]:
            nd=cd+w
            if nd<dist[v]:
                dist[v]=nd
                prev[v]=u
                heapq.heappush(h,(nd,v))
    return dist,prev

dist_s,prev_s=dijkstra_path(s)

# 最短経路復元（s->gの経路）
path=[]
cur=g
while cur!=-1:
    path.append(cur)
    cur=prev_s[cur]
path.reverse()

used=[False]*(N+1)
for node in path:
    used[node]=True

res=[]
for i in range(1,N+1):
    if not used[i]:
        res.append(i)

print(len(res))
print('\n'.join(map(str,res)))