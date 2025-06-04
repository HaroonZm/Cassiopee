n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append([])
for i in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

from collections import deque
queue = deque()
queue.append(0)
colors = []
for i in range(n):
    colors.append(-1)
colors[0] = 0
is_bipartite = True

while len(queue) > 0:
    node = queue.popleft()
    current_color = colors[node]
    for neighbor in graph[node]:
        if colors[neighbor] == -1:
            colors[neighbor] = 1 - current_color
            queue.append(neighbor)
        elif colors[neighbor] == current_color:
            is_bipartite = False

if not is_bipartite:
    print((n * (n - 1) // 2) - m)
else:
    w = 0
    b = 0
    for color in colors:
        if color == 0:
            w += 1
        elif color == 1:
            b += 1
    print(w * b - m)