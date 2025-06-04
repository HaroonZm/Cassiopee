import sys
sys.setrecursionlimit(10**7)

class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

def parse_tree(s, i=0):
    # parse tree starting at s[i]
    if s[i] == 'x':
        return Node(), i+1
    # s[i] == '('
    i += 1  # skip '('
    left, i = parse_tree(s, i)
    i += 1  # skip space
    right, i = parse_tree(s, i)
    i += 1  # skip ')'
    return Node(left, right), i

def collect_structures(node, structs):
    # return a frozenset of structure fingerprints in descendants including node itself
    if node.left is None:
        # leaf
        return {('x',)}
    left_structs = collect_structures(node.left, structs)
    right_structs = collect_structures(node.right, structs)
    # structure of current node
    # Because we consider interchangeable children, sort their structures to get canonical form
    lset = frozenset(left_structs)
    rset = frozenset(right_structs)
    if lset <= rset or rset <= lset:
        # They might overlap, but to get one unique representation:
        # So we get canonical representation by sorting the tuple of their structure strings
        left_repr = min_struct_repr(node.left)
        right_repr = min_struct_repr(node.right)
        if left_repr < right_repr:
            struct = ('(', left_repr, right_repr, ')')
        else:
            struct = ('(', right_repr, left_repr, ')')
    else:
        left_repr = min_struct_repr(node.left)
        right_repr = min_struct_repr(node.right)
        if left_repr < right_repr:
            struct = ('(', left_repr, right_repr, ')')
        else:
            struct = ('(', right_repr, left_repr, ')')

    new_structs = left_structs | right_structs | {struct}
    return new_structs

_struct_cache = {}
def min_struct_repr(node):
    # compute canonical minimal representation of subtree rooted at node
    # because children can be swapped arbitrarily, the representation should be canonical
    if node.left is None:
        return 'x'
    l = min_struct_repr(node.left)
    r = min_struct_repr(node.right)
    if l < r:
        return '(' + l + ' ' + r + ')'
    else:
        return '(' + r + ' ' + l + ')'

def left_right_similarity(node, memo):
    # left-right similarity: ratio of number of common structures in left and right descendants
    # including all descendants starting at child
    if node.left is None:
        return 0.0
    if node in memo:
        return memo[node]
    left_structs = collect_structures(node.left, set())
    right_structs = collect_structures(node.right, set())
    union = left_structs | right_structs
    if len(union) == 0:
        sim = 0.0
    else:
        common = left_structs & right_structs
        sim = len(common)/len(union)
    memo[node] = sim
    return sim

def asymmetricity_cmp(x, y, memo):
    # compare asymmetricity of nodes x and y
    # return -1 if x has stronger asymmetricity (smaller left-right similarity),
    # 1 if y has stronger asymmetricity,
    # 0 if equal
    if x.left is None and y.left is None:
        # no children, equal asymmetricity
        return 0
    sim_x = left_right_similarity(x, memo)
    sim_y = left_right_similarity(y, memo)
    if sim_x < sim_y:
        return -1
    if sim_x > sim_y:
        return 1
    # equal similarities
    if x.left is None and y.left is None:
        return 0
    # both have two children
    # compare child with stronger (or equal) asymmetricity
    cx0, cx1 = x.left, x.right
    cmpc = asymmetricity_cmp(cx0, cx1, memo)
    if cmpc <= 0:
        # cx1 has stronger or equal asymmetricity
        cxs = (cx1, cx0)
    else:
        cxs = (cx0, cx1)
    cy0, cy1 = y.left, y.right
    cmpc = asymmetricity_cmp(cy0, cy1, memo)
    if cmpc <= 0:
        cys = (cy1, cy0)
    else:
        cys = (cy0, cy1)
    res = asymmetricity_cmp(cxs[0], cys[0], memo)
    if res != 0:
        return res
    # compare weaker (or equal)
    res = asymmetricity_cmp(cxs[1], cys[1], memo)
    if res != 0:
        return res
    return 0

def reorder(node, is_left_child, memo):
    if node.left is None:
        return
    # reorder children recursively
    reorder(node.left, True, memo)
    reorder(node.right, False, memo)
    cmpres = asymmetricity_cmp(node.left, node.right, memo)
    if is_left_child:
        # left child cell of parent or root: left must have stronger or equal asymmetricity (smaller or equal left-right similarity)
        # stronger asymmetricity means cmpres == -1
        # if cmpres==1 means right stronger, swap
        if cmpres == 1:
            node.left, node.right = node.right, node.left
    else:
        # right child cell of parent: right must have stronger or equal asymmetricity
        # right stronger means cmpres==1
        # if cmpres==-1 means left stronger, swap
        if cmpres == -1:
            node.left, node.right = node.right, node.left

def serialize(node):
    if node.left is None:
        return "x"
    else:
        return "(" + serialize(node.left) + " " + serialize(node.right) + ")"

def main():
    for line in sys.stdin:
        line = line.strip()
        if line == "0":
            break
        root, _ = parse_tree(line)
        memo = {}
        reorder(root, True, memo)
        print(serialize(root))

if __name__ == "__main__":
    main()