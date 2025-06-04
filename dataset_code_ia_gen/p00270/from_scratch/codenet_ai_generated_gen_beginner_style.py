import sys
import heapq

sys.setrecursionlimit(10**7)
input=sys.stdin.readline

S,R = map(int,input().split())
graph = [[] for _ in range(S+1)]
for _ in range(R):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

a,b,Q = map(int,input().split())

def dijkstra(start):
    dist = [10**15]*(S+1)
    dist[start] = 0
    hq = [(0,start)]
    while hq:
        cd,cv = heapq.heappop(hq)
        if dist[cv]<cd:
            continue
        for nv,nw in graph[cv]:
            nd = cd + nw
            if dist[nv]>nd:
                dist[nv] = nd
                heapq.heappush(hq,(nd,nv))
    return dist

dist_a = dijkstra(a)
dist_b = dijkstra(b)

for _ in range(Q):
    c,d = map(int,input().split())
    if dist_a[c]+dist_a[d]-2*dist_a[a] != dist_a[b]:
        # c, d区間がa〜b最短経路の途中にない可能性あり。簡単に判定できないので正攻法で判定する。
        # 問題の条件でc,d区間も最短経路、pはa→bの最短経路でc,d順通過
        # 以下のチェックでもOK:
        # dist_a[c]+dist_between_c_d+dist_b[d] == dist_a[b] かつ dist_c[d] == dist_between_c_d
        # dist_between_c_dはc→dの最短距離

        dist_c = dijkstra(c)
        if dist_a[c] + dist_c[d] + dist_b[d] == dist_a[b]:
            print("Yes")
        else:
            print("No")
    else:
        # dist_a[b]==dist_a[c]+dist_c[d]+dist_b[d]
        dist_c = dijkstra(c)
        if dist_c[d] + dist_a[c] + dist_b[d] == dist_a[b]:
            print("Yes")
        else:
            print("No")