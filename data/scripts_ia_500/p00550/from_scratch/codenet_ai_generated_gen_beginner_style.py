import sys
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M, Q = map(int, input().split())
edges = [[] for _ in range(N+1)]
uv = [None]*(M+1)
for i in range(1, M+1):
    u,v = map(int, input().split())
    edges[u].append((v,i))
    edges[v].append((u,i))
    uv[i] = (u,v)

R = [int(input()) for _ in range(Q)]

# すべての路線のコストは1円で初期化
cost = [1]*(M+1)

# 都市1から各都市への初期の最短運賃をdijkstraで求める
def dijkstra():
    dist = [10**15]*(N+1)
    dist[1] = 0
    hq = [(0,1)]
    while hq:
        cd, v = heapq.heappop(hq)
        if dist[v]<cd:
            continue
        for nv, ni in edges[v]:
            c = cost[ni]
            nd = cd+c
            if nd<dist[nv]:
                dist[nv]=nd
                heapq.heappush(hq,(nd,nv))
    return dist

# 計画開始前の最短距離を計算
base_dist = dijkstra()

# 1年目からQ年目まで計画を適用した運賃を順に計算して，そのたびに不満な都市数を求める
# シンプルな方法で毎回dijkstraを計算すると遅いが，初心者向けにはこれでよい
angry_counts = []
for j in range(Q):
    cost[R[j]] = 2
    dist = dijkstra()
    count = 0
    for city in range(2, N+1):
        if dist[city] > base_dist[city]:
            count += 1
    angry_counts.append(count)

for c in angry_counts:
    print(c)