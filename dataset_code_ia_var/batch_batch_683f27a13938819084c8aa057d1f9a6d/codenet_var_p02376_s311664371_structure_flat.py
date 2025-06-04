from collections import deque

n, m = map(int, input().split())
inf = 10**9 + 7

edges = []
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c, len(graph[b])])
    graph[b].append([a, 0, len(graph[a]) - 1])
    edges.append(((a, len(graph[a]) - 1), (b, len(graph[b]) - 1)))

level = [-1] * n
iter_ = [0] * n

flow = 0
source = 0
sink = n - 1

while True:
    level = [-1] * n
    dq = deque()
    level[source] = 0
    dq.append(source)
    while dq:
        v = dq.popleft()
        for e in graph[v]:
            to, cap, rev = e
            if cap > 0 and level[to] < 0:
                level[to] = level[v] + 1
                dq.append(to)
    if level[sink] < 0:
        break
    iter_ = [0] * n
    while True:
        stack = []
        visited = [0] * n
        ptr = [0] * n
        stack.append((source, inf))
        path = []
        pushed = 0
        while stack:
            v, f = stack[-1]
            if v == sink:
                path = stack.copy()
                pushed = f
                break
            while ptr[v] < len(graph[v]):
                to, cap, rev = graph[v][ptr[v]]
                if cap > 0 and level[v] < level[to]:
                    stack.append((to, min(f, cap)))
                    break
                ptr[v] += 1
            else:
                stack.pop()
        if not path:
            break
        delta = pushed
        for i in range(len(path)-1):
            u = path[i][0]
            v = path[i+1][0]
            for j, e in enumerate(graph[u]):
                if e[0] == v and e[1] > 0 and level[u] < level[v]:
                    e[1] -= delta
                    graph[v][e[2]][1] += delta
                    break
        flow += delta
print(flow)