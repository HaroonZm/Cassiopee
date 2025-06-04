t = {}
p = {}
d = {}

n = int(input())
for i in range(n):
    e = input().split()
    t[e[0]] = e[2:]
    for child in e[2:]:
        p[child] = e[0]

# Trouver la racine (le seul nœud sans parent)
root_candidates = set(t.keys()) - set(p.keys())
root = root_candidates.pop()
p[root] = '-1'

def assign_depths(node, depth):
    d[node] = str(depth)
    for child in t[node]:
        assign_depths(child, depth + 1)

assign_depths(root, 0)

s = sorted(map(int, t))
for node in s:
    node_str = str(node)
    parent = p[node_str]
    depth = d[node_str]
    if parent == '-1':
        kind = 'root,'
    elif t[node_str]:
        kind = 'internal node,'
    else:
        kind = 'leaf,'
    children = list(map(int, t[node_str]))
    print('node', node_str + ':', 'parent =', parent + ',', 'depth =', depth + ',', kind, children)