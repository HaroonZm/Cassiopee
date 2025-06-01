n = int(input())
graph = [[] for _ in range(200)]
used_nodes = [0]*200

# Marking visited nodes in input
visited = [0]*200

for _ in range(n):
    u, rel, v = input().split()
    u = int(u) - 1
    v = int(v) - 1
    visited[u] = 1
    visited[v + 100] = 1
    if rel == 'lock':
        graph[u].append(v + 100)
    else:
        graph[v + 100].append(u)

visited_stack = [0]*200  # to detect cycles
checked = [0]*200  # nodes we finished processing

def dfs(node):
    if checked[node]:
        return 0
    cycle_found = 0
    visited_stack[node] = 1
    for neigh in graph[node]:
        if visited_stack[neigh]:
            cycle_found = 1
            continue
        cycle_found |= dfs(neigh)
    visited_stack[node] = 0
    checked[node] = 1
    return cycle_found

for i in range(200):
    if not visited[i]:
        continue
    if dfs(i):
        print(1)
        break
else:
    print(0)