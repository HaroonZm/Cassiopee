import sys
sys.setrecursionlimit(100000)
V = int(input())
E = int(input())
L = []
visited = [0 for i in range(V)]
edges = [[] for i in range(V)]

for i in range(E):
    s, t = map(int, input().split())
    edges[s - 1].append(t - 1)

stack = []
for i in range(V):
    if not visited[i]:
        stack.append((i, 0))
        while stack:
            node, state = stack.pop()
            if state == 0:
                if not visited[node]:
                    visited[node] = 1
                    stack.append((node, 1))
                    for e in reversed(edges[node]):
                        if not visited[e]:
                            stack.append((e, 0))
            else:
                L.append(node)

L.reverse()

flag = 0
for i in range(V):
    print(L[i] + 1)
    if not flag and i < V - 1 and (L[i + 1] not in edges[L[i]]):
        flag = 1
print(flag)