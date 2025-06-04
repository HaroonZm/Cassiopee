class Tree:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

def parse_tree(s):
    # Parse tree from string like '((,),(,))'
    # Returns (tree, next_pos)
    # s[pos] should be '(' at start
    def helper(pos):
        if s[pos] != '(':
            return None, pos
        pos += 1  # skip '('
        if s[pos] == ',':
            left = None
        else:
            left, pos = helper(pos)
        if s[pos] != ',':
            return None, pos
        pos += 1  # skip ','
        if s[pos] == ')':
            right = None
        else:
            right, pos = helper(pos)
        if s[pos] != ')':
            return None, pos
        pos += 1  # skip ')'
        return Tree(left, right), pos
    tree, pos = helper(0)
    return tree

def tree_to_str(t):
    if t is None:
        return ''
    left_str = tree_to_str(t.left) if t.left else ''
    right_str = tree_to_str(t.right) if t.right else ''
    return '(' + left_str + ',' + right_str + ')'

def intersection(t1, t2):
    if t1 is None or t2 is None:
        return None
    left = intersection(t1.left, t2.left)
    right = intersection(t1.right, t2.right)
    return Tree(left, right)

def union(t1, t2):
    if t1 is None and t2 is None:
        return None
    left = union(t1.left if t1 else None, t2.left if t2 else None)
    right = union(t1.right if t1 else None, t2.right if t2 else None)
    return Tree(left, right)

import sys

for line in sys.stdin:
    line=line.strip()
    if not line:
        continue
    op, t1s, t2s = line.split(' ', 2)
    t1 = parse_tree(t1s)
    t2 = parse_tree(t2s)
    if op == 'i':
        res = intersection(t1, t2)
    else:
        res = union(t1, t2)
    print(tree_to_str(res))