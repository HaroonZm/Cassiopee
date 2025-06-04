from sys import stdin
from collections import namedtuple

Node = namedtuple('Node', 'idx left right parent')
def build_tree(data):
    n = int(data[0])
    nodes = [None]*n
    parents = [-1]*n
    for line in data[1:n+1]:
        idx, left, right = map(int, line.split())
        nodes[idx] = [idx, left, right, -1]
        if left != -1: parents[left] = idx
        if right != -1: parents[right] = idx
    for i, p in enumerate(parents):
        nodes[i][3] = p
    # Get root
    root_idx = parents.index(-1)
    return [Node(*x) for x in nodes], root_idx

def preorder(nodes, idx):
    stack = [idx]
    while stack:
        cur = stack.pop()
        yield cur
        right = nodes[cur].right; left = nodes[cur].left
        if right != -1: stack.append(right)
        if left  != -1: stack.append(left)

def inorder(nodes, idx):
    stack = []
    cur = idx
    while stack or cur != -1:
        while cur != -1:
            stack.append(cur)
            cur = nodes[cur].left
        cur = stack.pop()
        yield cur
        cur = nodes[cur].right

def postorder(nodes, idx):
    stack, out = [idx], []
    while stack:
        cur = stack.pop()
        out.append(cur)
        left = nodes[cur].left; right = nodes[cur].right
        if left != -1: stack.append(left)
        if right != -1: stack.append(right)
    yield from reversed(out)

def main():
    data = stdin.readlines()
    nodes, root = build_tree(data)
    print('Preorder')
    print('',' '.join(str(i) for i in preorder(nodes, root)))
    print('Inorder')
    print('',' '.join(str(i) for i in inorder(nodes, root)))
    print('Postorder')
    print('',' '.join(str(i) for i in postorder(nodes, root)))
main()