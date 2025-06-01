import sys

class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

def parse_tree(s, i=0):
    if s[i] != '(':
        return None, i
    i += 1
    if s[i] == ',':
        left = None
    else:
        left, i = parse_tree(s, i)
    if s[i] != ',':
        raise ValueError("Expected ','")
    i += 1
    if s[i] == ')':
        right = None
    else:
        right, i = parse_tree(s, i)
    if s[i] != ')':
        raise ValueError("Expected ')'")
    i += 1
    return Node(left, right), i

def tree_to_str(t):
    if t is None:
        return ''
    return '(' + (tree_to_str(t.left) if t.left else '') + ',' + (tree_to_str(t.right) if t.right else '') + ')'

def intersection(t1, t2):
    if t1 is None or t2 is None:
        return None
    return Node(intersection(t1.left, t2.left), intersection(t1.right, t2.right))

def union(t1, t2):
    if t1 is None and t2 is None:
        return None
    left = union(t1.left if t1 else None, t2.left if t2 else None)
    right = union(t1.right if t1 else None, t2.right if t2 else None)
    return Node(left, right)

for line in sys.stdin:
    line=line.strip()
    if not line:
        continue
    op, t1s, t2s = line[0], line[2:].split()
    tree1, _ = parse_tree(t1s)
    tree2, _ = parse_tree(t2s)
    if op == 'i':
        res = intersection(tree1, tree2)
    else:
        res = union(tree1, tree2)
    print(tree_to_str(res))