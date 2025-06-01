import sys

def parse_tree(s, i=0):
    if i >= len(s) or s[i] != '(':
        return None, i
    i += 1
    # parse left child
    if s[i] == ',':
        left = None
    else:
        left, i = parse_tree(s, i)
    if s[i] != ',':
        raise ValueError("Expected ','")
    i += 1
    # parse right child
    if s[i] == ')':
        right = None
    else:
        right, i = parse_tree(s, i)
    if s[i] != ')':
        raise ValueError("Expected ')'")
    i += 1
    return (left, right), i

def tree_to_str(t):
    if t is None:
        return ''
    left = tree_to_str(t[0]) if t[0] is not None else ''
    right = tree_to_str(t[1]) if t[1] is not None else ''
    return f'({left},{right})'

def intersect(t1, t2):
    if t1 is None or t2 is None:
        return None
    left = intersect(t1[0], t2[0])
    right = intersect(t1[1], t2[1])
    if left is None and right is None:
        return None
    return (left, right)

def union(t1, t2):
    if t1 is None and t2 is None:
        return None
    left = union(t1[0] if t1 else None, t2[0] if t2 else None)
    right = union(t1[1] if t1 else None, t2[1] if t2 else None)
    # if both are None, then None; else return tuple (with children)
    if left is None and right is None:
        # leaf node
        return (None, None)
    return (left, right)

for line in sys.stdin:
    line=line.strip()
    if not line:
        continue
    op, s1, s2 = line.split(' ', 2)
    t1, _ = parse_tree(s1)
    t2, _ = parse_tree(s2)
    if op == 'i':
        res = intersect(t1, t2)
    else:
        res = union(t1, t2)
    print(tree_to_str(res) if res is not None else '')