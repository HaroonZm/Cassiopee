import sys
sys.setrecursionlimit(1000000)
n = int(input())
alst = list(map(int, input().split()))
edges = [[] for _ in range(n)]
rev_edges = [[] for _ in range(n)]
for i in range(n):
    nxt = (i + alst[i]) % n
    edges[i].append(nxt)
    rev_edges[nxt].append(i)
visited = [False] * n
order = []
stack = []
for i in range(n):
    if not visited[i]:
        stack.append((i, 0))
        while stack:
            node, state = stack.pop()
            if state == 0:
                if visited[node]:
                    continue
                visited[node] = True
                stack.append((node, 1))
                for e in edges[node]:
                    if not visited[e]:
                        stack.append((e, 0))
            else:
                order.append(node)
order.reverse()
visited = [False] * n
cycles = set()
for i in order:
    if not visited[i]:
        stack = [i]
        temp_stack = []
        cycles.add(i)
        visited[i] = True
        while stack:
            node = stack.pop()
            for e in rev_edges[node]:
                if not visited[e]:
                    visited[e] = True
                    cycles.add(e)
                    stack.append(e)
                elif e == node:
                    cycles.add(e)
            temp_stack.append(node)
print(len(cycles))