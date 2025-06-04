from collections import deque

V, E = map(int, input().split())
num_of_node = V
assert num_of_node > 0

graph = [list() for _ in range(num_of_node)]
level = [None] * num_of_node
ite = [None] * num_of_node

class Edge:
    def __init__(self, to, flow, cap, rev, is_rev):
        self.to = to
        self.flow = flow
        self.cap = cap
        self.rev = rev
        self.is_rev = is_rev

for _ in range(E):
    f, t, cap = map(int, input().split())
    graph[f].append(Edge(t, 0, cap, len(graph[t]), False))
    graph[t].append(Edge(f, cap, cap, len(graph[f]) - 1, True))

s = 0
t = V - 1
flow = 0

while True:
    # BFS
    level = [-1] * num_of_node
    que = deque()
    que.append(s)
    level[s] = 0
    while len(que):
        v = que.popleft()
        for i in range(len(graph[v])):
            e = graph[v][i]
            if e.cap - e.flow > 0 and level[e.to] < 0:
                level[e.to] = level[v] + 1
                que.append(e.to)
    if level[t] < 0:
        print(flow)
        break

    ite = [0] * num_of_node
    while True:
        # DFS
        stack = [(s, t, 10 ** 10, [])]
        result = 0
        visited = [0] * num_of_node
        # Explicit flat DFS loop replacing recursive call
        while stack:
            v, t_, f, path = stack.pop()
            if v == t_:
                result = f
                break
            found = False
            for i in range(ite[v], len(graph[v])):
                e = graph[v][i]
                if e.cap - e.flow > 0 and level[v] < level[e.to]:
                    ite[v] = i
                    stack.append((v, t_, f, path))  # save state to come back after subcall
                    min_f = min(f, e.cap - e.flow)
                    stack.append((e.to, t_, min_f, path + [(v, i, e)]))
                    found = True
                    break
                ite[v] = i
            if not found and path:
                # backtracking, pop the path as recursion unwinds
                continue
        if result == 0:
            break
        # update flows along the path
        v = s
        f = result
        stack = [(s, t, 10 ** 10, [])]
        # repeat once more to capture the path
        path = []
        visited = [0] * num_of_node
        found = False
        while stack and not found:
            v2, t_, f2, path2 = stack.pop()
            if v2 == t_:
                path = path2
                found = True
                break
            for i in range(ite[v2], len(graph[v2])):
                e = graph[v2][i]
                if e.cap - e.flow > 0 and level[v2] < level[e.to]:
                    stack.append((e.to, t_, min(f2, e.cap - e.flow), path2 + [(v2, i, e)]))
        for v2, i, e in path:
            e.flow += result
            graph[e.to][e.rev].flow -= result
        flow += result