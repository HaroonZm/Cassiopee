import sys
from collections import deque

def dfs_iterative(graph, start, color):
    stack = [start]
    failed = [False]
    while stack:
        u = stack.pop()
        for w in graph[u]:
            if color[w] == color[u]:
                failed[0] = True
                return
            elif color[w] < 0:
                color[w] = 1 - color[u]
                stack.append(w)
    return

def bfs_mix(adj_, colors_):
    q = deque([0])
    while q:
        u = q.popleft()
        for v in adj_[u]:
            if colors_[v] == colors_[u]:
                return False
            elif colors_[v] < 0:
                colors_[v] = 1 - colors_[u]
                q.append(v)
    return True

sys.setrecursionlimit(10**5)
while True:
    n, m = [int(x) for x in input().split()]
    if not (n or m):
        break
    adj = {i:[] for i in range(n)}
    parity = [-1]*n
    for __ in range(m):
        x, y = map(int, input().split())
        adj[x-1].append(y-1)
        adj[y-1].append(x-1)
    result = []
    ng = [False]

    parity[0] = 0

    if n > 20:
        # Use iterative DFS
        dfs_iterative(adj, 0, parity)
        ng[0] = False  # Can't share flag
    else:
        # Use BFS
        ng[0] = not bfs_mix(adj, parity)

    if -1 in parity and not ng[0]:
        for idx, col in enumerate(parity):
            if col == -1:
                parity[idx] = 0
                dfs_iterative(adj, idx, parity)

    bad = False
    for u in range(n):
        for v in adj[u]:
            if parity[u] == parity[v]:
                bad = True
                break
        if bad:
            break
    if ng[0] or bad:
        print(0)
        continue

    cnt = [0,0]
    for c in parity:
        if c == 0:
            cnt[0] += 1
        elif c == 1:
            cnt[1] += 1
    answer = []
    for grp in [cnt[0], cnt[1]]:
        if grp % 2 == 0 and 0 < grp < n:
            answer.append(grp//2)
    answer.sort()
    print(len(answer))
    if answer:
        for z in answer:
            print(z)