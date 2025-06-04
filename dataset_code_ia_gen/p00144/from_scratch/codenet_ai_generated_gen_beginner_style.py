n = int(input())
graph = {}

for _ in range(n):
    data = input().split()
    r = int(data[0])
    k = int(data[1])
    neighbors = list(map(int, data[2:2+k]))
    graph[r] = neighbors

p = int(input())

for _ in range(p):
    s, d, v = map(int, input().split())
    from collections import deque
    queue = deque()
    queue.append((s, 1))  # (current router, path length)
    visited = {s: 1}
    found = False
    while queue:
        current, dist = queue.popleft()
        if current == d:
            # les "dist" compte les routeurs traversés, TTL doit au moins être dist
            if v >= dist:
                print(dist)
            else:
                print("NA")
            found = True
            break
        if current in graph:
            for nxt in graph[current]:
                if nxt not in visited:
                    visited[nxt] = dist + 1
                    queue.append((nxt, dist + 1))
    if not found:
        print("NA")