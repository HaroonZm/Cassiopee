# AOJ 1014: Computation of Minimum Length of Pipeline
# Python3 2018.7.5 bal4u

import sys
from sys import stdin
input = stdin.readline
import heapq

while True:
	s, d = map(int, input().split())
	if s == 0: break
	visited = [0]*100
	Q = []
	to = [[] for i in range(100)]
	for i in range(s):
		visited[i] = 1
		c = list(map(int, input().split()))
		for j in range(d):
			if c[j] > 0: heapq.heappush(Q, (c[j], i, s+j))
	for i in range(d-1):
		c = list(map(int, input().split()))
		for j in range(i+1, d):
			if c[j-i-1] > 0:
				to[s+i].append((s+j, c[j-i-1]))
				to[s+j].append((s+i, c[j-i-1]))

	ans = k = 0
	while k < d:
		while True:
			c, a, b = heapq.heappop(Q)
			if visited[a] == 0 or visited[b] == 0: break
		ans, k = ans+c, k+1
		if visited[a]: a = b
		visited[a] = 1;
		for e, c in to[a]:
			if visited[e] == 0:	heapq.heappush(Q, (c, a, e))
	print(ans)