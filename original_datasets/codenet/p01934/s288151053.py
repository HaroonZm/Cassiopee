# AOJ 2834 Dimension travel
# Python3 2018.7.12 bal4u

INF = 0x7fffffff
import heapq
def dijkstra(V, to, start, goal):
	dist = [INF]*V
	Q = []
	dist[start] = 0
	heapq.heappush(Q, (0, start))
	while Q:
		t, s = heapq.heappop(Q)
		if s == goal: break
		if dist[s] < t: continue
		for e in to[s]:
			nt = t
			if e > s: nt += d[e]
			if dist[e] > nt:
				dist[e] = nt
				heapq.heappush(Q, (nt, e))
	return t

import sys
N, M, s, t = map(int, input().split())
s, t = s-1, t-1
if s >= t: print(0); sys.exit(0)
d = list(map(int, input().split()))
to = [[i-1] if i > 0 else [] for i in range(N)]
for i in range(M):
	a, b = map(int, input().split())
	to[a-1].append(b-1)
print(dijkstra(N, to, s, t))