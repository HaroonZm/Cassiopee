n = int(input())
graph = {}
for _ in range(n):
    data = list(map(int, input().split()))
    r = data[0]
    k = data[1]
    graph[r] = data[2:] if k > 0 else []

p = int(input())
packets = [tuple(map(int, input().split())) for _ in range(p)]

from collections import deque

for s, d, ttl in packets:
    if s == d:
        # Problem states s != d, but just in case
        print(0)
        continue
    # BFS to find shortest path length (number of nodes) from s to d
    queue = deque()
    queue.append((s, 1))  # (current_node, path_length)
    visited = set()
    visited.add(s)
    found = False
    while queue:
        cur, length = queue.popleft()
        if cur == d:
            # length is count of nodes including start and end
            # Number of routers passed is length
            # Number of decrements of TTL is length -1 (excluding the destination)
            needed_ttl = length - 1
            if ttl >= needed_ttl:
                print(length)
            else:
                print("NA")
            found = True
            break
        for nxt in graph[cur]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, length + 1))
    if not found:
        print("NA")