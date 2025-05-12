# AOJ 0564: Bug Party
# Python3 2018.6.30 bal4u

import heapq
tbl = []
N = int(input())
for i in range(N):
	a, b = map(int, input().split())
	tbl.append((a, b))
tbl.sort()
Q = []
ans = s = sz = 0
for t in tbl:
	s += t[0]
	heapq.heappush(Q, (t[1], t[0]))
	sz += 1
	while sz and sz*Q[0][0] < s:
		s -= Q[0][1]
		heapq.heappop(Q)
		sz -= 1
	if sz > ans: ans = sz
print(ans)