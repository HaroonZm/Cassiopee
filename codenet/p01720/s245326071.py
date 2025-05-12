# AOJ 2608: Minus One
# Python3 2018.6.30 bal4u

import heapq
MAX = 0x7fffffff

def dijkstra(dist, start):
	Q = []
	dist[start] = 0
	heapq.heappush(Q, (0, start))
	while Q:
		t, s = heapq.heappop(Q)
		if dist[s] < t: continue
		for e in to[s]:
			nt = t + 1
			if dist[e] > nt:
				dist[e] = nt
				heapq.heappush(Q, (nt, e))

N, M, s, t = map(int, input().split())
s, t = s-1, t-1
to = [[] for i in range(N)]
for i in range(M):
	x, y = map(int, input().split())
	x, y = x-1, y-1
	to[x].append(y)
	to[y].append(x)
smin = [MAX]*N
dijkstra(smin, s)
tmin = [MAX]*N
dijkstra(tmin, t)
scnt = [0]*N
tcnt = [0]*N
for i in range(N):
	if smin[i] < N: scnt[smin[i]] += 1
	if tmin[i] < N: tcnt[tmin[i]] += 1
ans = 0
s = smin[t]-1
for i in range(s): ans += scnt[i]*tcnt[s-1-i]
print(ans)