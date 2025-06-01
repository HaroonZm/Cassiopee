m = int(input())
n = int(input())
edges = [[] for _ in range(m + 1)]
indegree = [0] * (m + 1)
for _ in range(n):
    x, y = map(int, input().split())
    edges[x].append(y)
    indegree[y] += 1
from collections import deque
q = deque()
for i in range(1, m + 1):
    if indegree[i] == 0:
        q.append(i)
order = []
while q:
    curr = q.popleft()
    order.append(curr)
    for nxt in edges[curr]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)
for o in order:
    print(o)