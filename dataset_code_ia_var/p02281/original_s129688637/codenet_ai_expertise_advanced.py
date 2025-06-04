from sys import stdin
from typing import NamedTuple

class Node(NamedTuple):
    parent: int = -1
    left: int = -1
    right: int = -1
    sibling: int = -1

N = int(stdin.readline())
tree = [Node() for _ in range(N)]
tree = list(map(lambda _: Node(), range(N)))
parents = set(range(N))

nodes = [list(map(int, stdin.readline().split())) for _ in range(N)]
updated_tree = list(tree)
for nid, l, r in nodes:
    p, s_left, s_right = updated_tree[nid].parent, l, r
    left_node = updated_tree[l]._replace(parent=nid, sibling=r) if l != -1 else None
    right_node = updated_tree[r]._replace(parent=nid, sibling=l) if r != -1 else None
    updated_tree[nid] = updated_tree[nid]._replace(left=l, right=r)
    if l != -1:
        updated_tree[l] = left_node
    if r != -1:
        updated_tree[r] = right_node
    parents -= {l, r}
tree = updated_tree
root, = parents

def preorder(u):
    stack = []
    while True:
        while u != -1:
            print(f' {u}', end='')
            stack.append(u)
            u = tree[u].left
        if not stack:
            break
        u = tree[stack.pop()].right

def inorder(u):
    stack = []
    while True:
        while u != -1:
            stack.append(u)
            u = tree[u].left
        if not stack:
            break
        u = stack.pop()
        print(f' {u}', end='')
        u = tree[u].right

def postorder(u):
    stack, output = [], []
    while u != -1 or stack:
        if u != -1:
            stack.append(u)
            output.append(u)
            u = tree[u].right
        else:
            u = tree[stack.pop()].left
    for node in reversed(output):
        print(f' {node}', end='')

print('Preorder')
preorder(root)
print()
print('Inorder')
inorder(root)
print()
print('Postorder')
postorder(root)
print()