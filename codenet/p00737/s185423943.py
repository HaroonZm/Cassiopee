# AOJ 1156: Twirling Robot
# Python3 2018.7.15 bal4u

mv = [[-1,0,],[0,1],[1,0],[0,-1]]

INF = 0x7fffffff
import heapq
def dijkstra(h, w, cost):
	Q = []
	node = [[[INF for d in range(4)] for c in range(w)] for r in range(h)]
	node[0][0][1] = 0
	heapq.heappush(Q, (0, 0, 0, 1))
	while Q:
		t, r, c, d = heapq.heappop(Q)
		if r == h-1 and c == w-1: break
		for i in range(4):
			nd = (d+i)%4
			nr, nc = r + mv[nd][0], c + mv[nd][1]
			if nr < 0 or nr >= h or nc < 0 or nc >= w: continue
			nt = node[r][c][d]
			if arr[r][c] != i: nt += cost[i]
			if nt < node[nr][nc][nd]:
				node[nr][nc][nd] = nt
				heapq.heappush(Q, (nt, nr, nc, nd))
	return node[h-1][w-1][d]
	
while True:
	w, h = map(int, input().split())
	if w == 0: break
	arr = [[] for r in range(h)]
	for r in range(h): arr[r] = list(map(int, input().split()))
	cost = list(map(int, input().split()))
	print(dijkstra(h, w, cost))