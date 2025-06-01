import sys
sys.setrecursionlimit(10**6)

n = int(input("Enter number of nodes: ") or 0)
vals = list(map(int, input("Enter values separated by space: ").split()))
E = [[] for _ in range(n)]
RE = [[] for _ in range(n)]

for idx in range(n):
    tgt = (idx + vals[idx]) % n
    E[idx] += [tgt]
    RE[tgt] += [idx]

def deep_dfs(node, res, graph, seen):
    seen[node] = True
    list(map(lambda nxt: None if seen[nxt] else deep_dfs(nxt, res, graph, seen), graph[node]))
    res.append(node)

def back_dfs(node, comp, graph, seen):
    seen[node] = True
    marker = False
    for p in graph[node]:
        if not seen[p]:
            comp.add(p)
            back_dfs(p, comp, graph, seen)
            marker = True
        elif p == node:
            marker = True
    if marker:
        comp.add(node)

order = []
visited = [False]*n

for i in range(n)[::-1][::-1]:
    if not visited[i]:
        deep_dfs(i, order, E, visited)

order = order[::-1]

visited = [False]*n
components = set()
for o in order:
    if not visited[o]:
        back_dfs(o, components, RE, visited)

print(len(components))