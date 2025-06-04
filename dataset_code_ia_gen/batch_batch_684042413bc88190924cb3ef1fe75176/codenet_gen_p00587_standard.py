import sys

class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

def parse_tree(s, i=0):
    # Parse tree from s starting at index i, return (node, next_index)
    if s[i] != '(':
        return None, i
    i += 1
    # parse left child
    if s[i] == ',':
        left = None
        i += 1
    else:
        left, i = parse_tree(s, i)
        if s[i] != ',':
            raise ValueError("Expected ',' at %d" % i)
        i += 1
    # parse right child
    if s[i] == ')':
        right = None
    else:
        right, i = parse_tree(s, i)
    if s[i] != ')':
        raise ValueError("Expected ')' at %d" % i)
    i += 1
    return Node(left, right), i

def tree_to_str(node):
    if node is None:
        return ''
    if node.left is None and node.right is None:
        return '()'
    left_str = tree_to_str(node.left) if node.left else ''
    right_str = tree_to_str(node.right) if node.right else ''
    return '(' + left_str + ',' + right_str + ')'

def intersect(n1, n2):
    if n1 is None or n2 is None:
        return None
    left = intersect(n1.left, n2.left)
    right = intersect(n1.right, n2.right)
    if left is None and right is None:
        return None
    return Node(left, right)

def union(n1, n2):
    if n1 is None and n2 is None:
        return None
    left = union(n1.left if n1 else None, n2.left if n2 else None)
    right = union(n1.right if n1 else None, n2.right if n2 else None)
    if left is None and right is None:
        # leaf present if either leaf
        if (n1 is not None) or (n2 is not None):
            return Node()
        return None
    return Node(left, right)

for line in sys.stdin:
    if not line.strip():
        continue
    op, t1, t2 = line.strip().split()
    tree1, _ = parse_tree(t1, 0)
    tree2, _ = parse_tree(t2, 0)
    if op == 'i':
        res = intersect(tree1, tree2)
    else:
        res = union(tree1, tree2)
    if res is None:
        # no node, print empty leaf?
        print('()')
    else:
        print(tree_to_str(res))