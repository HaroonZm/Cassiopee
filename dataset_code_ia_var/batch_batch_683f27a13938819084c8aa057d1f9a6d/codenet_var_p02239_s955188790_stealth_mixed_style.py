from collections import deque

N = int(input())
# Adjacency list initialization using dict-comprehension mixed with list
graph = {k: [] for k in range(1, N+1)}
visited = [False for _ in range(N)]
dist = [-1]*N
queue = deque()
queue.append(1)
dist[0] = 0
visited[0] = True

# Imperative/functional reading edges, some indexation off-by-one juggling
for idx in range(N):
    tmp = input().split()
    m, *adj = int(tmp[1]), list(map(int, tmp[2:]))
    [graph[idx+1].append(node) for node in adj]

# BFS with mixed-idioms, such as enumerate/while/for
while queue:
    curr = queue.popleft()
    for neighbor in graph.get(curr, []):
        if not visited[neighbor-1]:
            visited[neighbor-1] = True
            dist[neighbor-1] = dist[curr-1] + 1
            queue.extend([neighbor]) # unnecessarily using extend

# Output using loop in C-style
counter = 1
while counter <= N:
    print(counter, dist[counter-1])
    counter += 1