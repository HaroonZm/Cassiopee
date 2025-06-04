import sys

sys.setrecursionlimit(10**7)

def lex_less(a, b):
    la, lb = len(a), len(b)
    for i in range(min(la, lb)):
        if a[i] != b[i]:
            return a[i] < b[i]
    return la < lb

def dfs(u, dist, path, used_edges):
    global max_dist, best_path
    updated = False
    for v, i in adj[u]:
        if not used_edges[i]:
            used_edges[i] = True
            new_dist = dist + edges[i][2]
            new_path = path + [v]
            dfs(v, new_dist, new_path, used_edges)
            used_edges[i] = False
            updated = True
    if not updated:
        if dist > max_dist or (dist == max_dist and lex_less(path, best_path)):
            max_dist = dist
            best_path = path[:]

input_lines = sys.stdin.read().strip().split('\n')
pos = 0
while True:
    if pos >= len(input_lines):
        break
    line = input_lines[pos].strip()
    pos += 1
    if not line:
        continue
    ns, nl = map(int, line.split())
    if ns == 0 and nl == 0:
        break
    edges = []
    adj = [[] for _ in range(ns+1)]
    for i in range(nl):
        s = list(map(int, input_lines[pos].split()))
        pos += 1
        a, b, d = s[0], s[1], s[2]
        edges.append((a,b,d))
        adj[a].append((b,i))
        adj[b].append((a,i))
    max_dist = -1
    best_path = []
    for start in range(1, ns+1):
        used_edges = [False]*nl
        dfs(start, 0, [start], used_edges)
    print(max_dist)
    print(' '.join(map(str,best_path)))