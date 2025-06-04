import sys
sys.setrecursionlimit(2**20)

class Node:
    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left
        self.right = right

d = {}

def get_all_depth(t, u, p):
    d[u] = p
    if t[u].right is not None:
        get_all_depth(t, t[u].right, p)
    if t[u].left is not None:
        get_all_depth(t, t[u].left, p + 1)

def return_children(t, u):
    children = []
    c = t[u].left
    while c is not None:
        children.append(c)
        c = t[c].right
    return children

n = int(input())
t = {k: Node(None, None, None) for k in range(n)}
for _ in range(n):
    tmp = list(map(int, input().split()))
    if tmp[1] == 0:
        continue
    t[tmp[0]].left = tmp[2]
    t[tmp[2]].parent = tmp[0]
    prev_sib = tmp[2]
    for sib in tmp[3:]:
        t[prev_sib].right = sib
        t[sib].parent = tmp[0]
        prev_sib = sib

for node in range(n):
    if t[node].parent is None:
        get_all_depth(t, node, 0)
        break

for node in range(n):
    node_type = "internal node" if t[node].left is not None else "leaf"
    if t[node].parent is None:
        parent = -1
        node_type = "root"
    else:
        parent = t[node].parent
    children = return_children(t, node)
    print(f"node {node}: parent = {parent}, depth = {d[node]}, {node_type}, {children}")