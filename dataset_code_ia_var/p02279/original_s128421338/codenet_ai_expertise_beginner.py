import sys
sys.setrecursionlimit(2**20)

class Node:
    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left
        self.right = right

d = {}

def get_all_depth(tree, u, depth):
    d[u] = depth
    if tree[u].right is not None:
        get_all_depth(tree, tree[u].right, depth)
    if tree[u].left is not None:
        get_all_depth(tree, tree[u].left, depth + 1)

def return_children(tree, u):
    children = []
    c = tree[u].left
    while c is not None:
        children.append(c)
        c = tree[c].right
    return children

n = int(input())
t = {}
for k in range(n):
    t[k] = Node(None, None, None)

for _ in range(n):
    parts = list(map(int, input().split()))
    node_id = parts[0]
    num_child = parts[1]
    if num_child == 0:
        continue
    first_child = parts[2]
    t[node_id].left = first_child
    t[first_child].parent = node_id
    prev = first_child
    for child in parts[3:]:
        t[prev].right = child
        t[child].parent = node_id
        prev = child

for i in range(n):
    if t[i].parent is None:
        get_all_depth(t, i, 0)
        break

for i in range(n):
    if t[i].parent is None:
        parent = -1
        node_type = "root"
    elif t[i].left is None:
        parent = t[i].parent
        node_type = "leaf"
    else:
        parent = t[i].parent
        node_type = "internal node"
    children = return_children(t, i)
    print("node {}: parent = {}, depth = {}, {}, {}".format(i, parent, d[i], node_type, children))