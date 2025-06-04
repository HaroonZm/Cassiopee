import sys
import heapq
input=sys.stdin.readline

N,M,K=map(int,input().split())
P=[0]+list(map(int,input().split()))
c=[0]+list(map(int,input().split()))
J=[0]+list(map(int,input().split()))

graph=[[] for _ in range(N+1)]
for _ in range(M):
    u,v,t=map(int,input().split())
    graph[u].append((v,t))
    graph[v].append((u,t))

def dijkstra(start):
    dist=[float('inf')]*(N+1)
    dist[start]=0
    hq=[(0,start)]
    while hq:
        cd,cu=heapq.heappop(hq)
        if dist[cu]<cd:
            continue
        for nv,nc in graph[cu]:
            nd=cd+nc
            if dist[nv]>nd:
                dist[nv]=nd
                heapq.heappush(hq,(nd,nv))
    return dist

dist=dijkstra(1)

# for each city i compute score = P[i] - 2*dist[i]
score = [float('-inf')] * (N+1)
for i in range(1,N+1):
    score[i] = P[i] - 2*dist[i]

# for each jam flavor k find max score of city with c[i]==k
max_score_per_c = [float('-inf')] * (K+1)
for i in range(1,N+1):
    if score[i] > max_score_per_c[c[i]]:
        max_score_per_c[c[i]] = score[i]

# For each jam flavor k find max of (score of city_for_bread + J[j] - 2*dist[j]) 
# over all j with c[j]==k
# That is, max over u of (P[u]-2*dist[u]) plus max over v with c[v]=k of (J[v]-2*dist[v])
max_jam_score = [float('-inf')] * (K+1)
# Precompute max of (J[i] - 2*dist[i]) for each c
max_jam_value = [float('-inf')] * (K+1)
for i in range(1,N+1):
    val = J[i] - 2*dist[i]
    if val > max_jam_value[c[i]]:
        max_jam_value[c[i]] = val

for k in range(1,K+1):
    max_jam_score[k] = max_score_per_c[k] + max_jam_value[k]

for k in range(1,K+1):
    print(max_jam_score[k])