n, m = map(int, input().split())
edges = []
for i in range(n):
    edges.append([])
for i in range(m):
    a, b, c = map(int, input().split())
    edges[a - 1].append((b - 1, c))

queue = []
queue.append((0, 0))
ans = -1

while len(queue) > 0:
    pos, time = queue[0]
    queue = queue[1:]
    if pos == n - 1:
        if time > ans:
            ans = time
    i = len(edges[pos]) - 1
    while i >= 0:
        to, new_time = edges[pos][i]
        if new_time >= time:
            queue.append((to, new_time))
            edges[pos].pop(i)
        i -= 1
print(ans)