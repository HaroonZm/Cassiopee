import sys
from collections import deque

sys.setrecursionlimit(10**8)

def find_path():
    parent = [-1] * n
    stack = [0]
    visited = [False] * n
    visited[0] = True
    while stack:
        u = stack.pop()
        if u == n - 1:
            break
        for v in g[u]:
            if not visited[v]:
                parent[v] = u
                visited[v] = True
                stack.append(v)
    path = deque()
    curr = n - 1
    while curr != -1:
        path.appendleft(curr)
        curr = parent[curr]
    return list(path)

def multi_color_dfs(root, assign_color, restrict):
    stack = [root]
    while stack:
        node = stack.pop()
        for neighbor in g[node]:
            if color[neighbor] == restrict:
                color[neighbor] = assign_color
                stack.append(neighbor)

n = int(raw_input())
g = [[] for _ in xrange(n)]
for _ in xrange(n - 1):
    a, b = map(int, raw_input().split())
    a -= 1; b -= 1
    g[a].append(b)
    g[b].append(a)

path = find_path()
color = ['bl'] * n
color[0] = 'b'
color[-1] = 'w'
i, j = 1, len(path) - 2
for idx in range(1, len(path) - 1):
    if idx & 1:
        v = path[i]
        color[v] = 'b'
        i += 1
    else:
        v = path[j]
        color[v] = 'w'
        j -= 1

multi_color_dfs(0, 'b', 'bl')
multi_color_dfs(n - 1, 'w', 'bl')

cntf = sum(c == 'b' for c in color)
cnts = n - cntf
print "Fennec" if cntf > cnts else "Snuke"