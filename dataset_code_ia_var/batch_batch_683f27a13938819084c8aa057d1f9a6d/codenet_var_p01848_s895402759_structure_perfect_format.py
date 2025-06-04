def fix(c):
    return int(c) - 1

def bfs(x, order, visited):
    if visited[x]:
        return
    visited[x] = True
    for to in edges[x]:
        bfs(to, order, visited)
    order.append(x)

def bfs_rev(x, visited):
    if visited[x]:
        return []
    visited[x] = True
    ret = [x]
    for to in rev_edges[x]:
        ret = ret + bfs_rev(to, visited)
    return ret

def bfs2(x, visited):
    if visited[x]:
        return
    visited[x] = True
    for to in edges[x]:
        bfs2(to, visited)

while True:
    n = int(input())
    if n == 0:
        break
    edges = []
    score = []
    for _ in range(n):
        lst = input().split()
        score.append(float(lst[0]))
        edges.append(list(map(fix, lst[2:])))
    rev_edges = [[] for _ in range(n)]
    for i in range(n):
        for e in edges[i]:
            rev_edges[e].append(i)
    visited = [False] * n
    order = []
    for x in range(n):
        bfs(x, order, visited)
    order.reverse()
    visited = [False] * n
    cycles = []
    for x in order:
        if not visited[x]:
            cycle = bfs_rev(x, visited)
            cycles.append(cycle)
    visited = [False] * n
    ans = 1
    for x in order:
        if not visited[x]:
            for cycle in cycles:
                if x in cycle:
                    acc = 1
                    for node in cycle:
                        bfs2(node, visited)
                        acc *= score[node]
                    ans *= (1 - acc)
    print("{0:.7f}".format(ans))