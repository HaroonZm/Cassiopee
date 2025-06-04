N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    s, t = map(int, input().split())
    G[s].append(t)

ans = []
V = set()
stack_trace = []
for i in range(N):
    if i not in V:
        stack = [(i, 0)]
        local_visited = set()
        while stack:
            node, idx = stack[-1]
            if node in V:
                stack.pop()
                continue
            if idx < len(G[node]):
                neighbor = G[node][idx]
                stack[-1] = (node, idx + 1)
                if neighbor not in V and neighbor not in local_visited:
                    stack.append((neighbor, 0))
                    local_visited.add(neighbor)
            else:
                ans.append(node)
                V.add(node)
                stack.pop()
print(*ans[::-1], sep="\n")