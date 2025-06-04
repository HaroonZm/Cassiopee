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
        temp_stack = []
        node_stack = [i]
        while node_stack:
            node = node_stack[-1]
            if not visited[node]:
                visited[node] = 1
                for e in edges[node]:
                    if not visited[e]:
                        node_stack.append(e)
                continue
            if node_stack[-1] not in temp_stack:
                temp_stack.append(node_stack[-1])
            node_stack.pop()
        for x in temp_stack:
            if x not in L:
                L.append(x)

L = L[::-1]

flag = 0
for i in range(V):
    print(L[i] + 1)
    if not flag and i < V - 1 and (L[i + 1] not in edges[L[i]]):
        flag = 1
print(flag)