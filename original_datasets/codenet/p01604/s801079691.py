from heapq import heappush, heappop
from collections import defaultdict

n = int(input())
s = [input() for i in range(n)]
start = tuple("sssssssssss")
goal = tuple("ggggggggggg")
s.append("ggggggggggg;")
v = defaultdict(list)
la = tuple([start[i] for i in range(11)])
k = 0
for i in s:
    if i[:4] == "goto":
        v[la].append((tuple(i[5:-1]),k))
        k += 1
    else:
        v[la].append((tuple(i[:-1]),k))
        la = tuple([i[j] for j in range(len(i)-1)])
        k = 0
q = [(0,start)]
dist = defaultdict(lambda : float("inf"))
dist[start] = 0
while q:
    dx,x = heappop(q)
    for y,d in v[x]:
        if dx + d < dist[y]:
            dist[y] = dx+d
            heappush(q,(dist[y],y))
print(dist[goal])