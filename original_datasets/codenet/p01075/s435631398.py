from collections import deque

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a - 1].append((b - 1, c))

que = deque()
que.append((0, 0))
ans = -1
while que:
    pos, time = que.popleft()
    if pos == n - 1:
        ans = max(ans, time)
    for i in range(len(edges[pos]) - 1, -1, -1):
        to, new_time = edges[pos][i]
        if new_time >= time:
            que.append((to, new_time))
            edges[pos].pop(i)
print(ans)