import heapq
import sys

BIG_NUM = 2000000000

V = int(input())
min_dist = [BIG_NUM]*V
G = [[] for _ in range(V)]

for _ in range(V):
    raw = list(map(int, input().split()))
    node_id = raw[0]
    tmp_num = raw[1]  # nombre d'arêtes sortantes, non utilisé
    edges = raw[2:]
    i = 0
    while i < len(edges):
        to = edges[i]
        cost = edges[i+1]
        G[node_id].append((to, cost))
        i += 2

min_dist[0] = 0
Q = []
heapq.heappush(Q, (0, 0))  # (coût cumulé, id_sommet)

while Q:
    sum_cost, node_id = heapq.heappop(Q)
    if sum_cost > min_dist[node_id]:
        continue
    for edge in G[node_id]:
        to = edge[0]
        cost = edge[1]
        new_cost = sum_cost + cost
        if min_dist[to] > new_cost:
            min_dist[to] = new_cost
            heapq.heappush(Q, (new_cost, to))

i = 0
while i < V:
    print(f"{i} {min_dist[i]}")
    i += 1