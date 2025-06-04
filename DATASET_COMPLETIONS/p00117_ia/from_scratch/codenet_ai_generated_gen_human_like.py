n = int(input())
m = int(input())

adj = [[] for _ in range(n+1)]
for _ in range(m):
    line = input().strip()
    a,b,c,d = map(int, line.split(','))
    adj[a].append((b,c))
    adj[b].append((a,d))

s, g, V, P = map(int, input().split(','))

import heapq

def dijkstra(start):
    dist = [float('inf')] * (n+1)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        cost, u = heapq.heappop(heap)
        if dist[u] < cost:
            continue
        for v, w in adj[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist

dist_s = dijkstra(s)
dist_g = dijkstra(g)

# coût total = route aller + route retour + prix du poteau
# récompense = V - coût total
total_cost = dist_s[g] + dist_g[s] + P
reward = V - total_cost
print(reward)