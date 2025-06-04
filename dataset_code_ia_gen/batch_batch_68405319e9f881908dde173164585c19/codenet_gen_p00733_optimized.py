import sys
sys.setrecursionlimit(10**7)

def parse_tree(s):
    idx = 0
    def parse():
        nonlocal idx
        if s[idx] == 'x':
            idx += 1
            return ('leaf',)
        # format: '(' tree ' ' tree ')'
        idx += 1  # '('
        left = parse()
        assert s[idx] == ' '
        idx += 1
        right = parse()
        assert s[idx] == ')'
        idx += 1
        return ('node', left, right)
    return parse()

def canonical(t):
    if t[0] == 'leaf':
        return 'x'
    l = canonical(t[1])
    r = canonical(t[2])
    if l < r:
        l, r = r, l
    return '(' + l + ' ' + r + ')'

def subtree_structures(t):
    # returns set of canonical subtree structures in descendants (including itself)
    if t[0] == 'leaf':
        return set(['x'])
    left_set = subtree_structures(t[1])
    right_set = subtree_structures(t[2])
    cs = canonical(t)
    return left_set | right_set | set([cs])

def similarity(t):
    if t[0] == 'leaf':
        return 0.0
    left_structs = subtree_structures(t[1])
    right_structs = subtree_structures(t[2])
    union = left_structs | right_structs
    intersection = left_structs & right_structs
    if not union:
        return 0.0
    return len(intersection)/len(union)

def make_comparator():
    from functools import lru_cache

    @lru_cache(None)
    def asymmetry_key(t, pos):  # pos: 0=root/left child, 1=right child
        # returns (similarity, left_child_key, right_child_key) with asymmetry ordering for comparison
        sim = similarity(t)
        if t[0] == 'leaf':
            return (sim,)
        # children keys
        # arrange children first in asymmetry order independent of pos for asymmetry_key:
        # but we need to obey problem rule at reorder stage.
        # so just return keys of children as a pair for later compare.
        lkey = asymmetry_key(t[1],0)
        rkey = asymmetry_key(t[2],1)
        # We do not reorder here, only collect keys for comparison.
        return (sim, lkey, rkey)

    def asymmetry_compare(tX,posX,tY,posY):
        # returns True if tX has stronger asymmetricity than tY
        # i.e. tX < tY in asymmetricity strength order
        # lower similarity means stronger asymmetricity
        simX = similarity(tX)
        simY = similarity(tY)
        if simX != simY:
            return simX < simY
        if tX[0] == 'leaf' and tY[0] == 'leaf':
            return False  # equal asymmetricity
        # both have two children
        # find stronger or equal asymmetricity child for X and Y
        lX, rX = tX[1], tX[2]
        lY, rY = tY[1], tY[2]
        def stronger(A,B):
            return asymmetry_compare(A,0,B,0)
        def equal(A,B):
            return not asymmetry_compare(A,0,B,0) and not asymmetry_compare(B,0,A,0)
        # stronger or equal child of X
        if stronger(lX,rX) or equal(lX,rX):
            strongX, weakX = lX, rX
        else:
            strongX, weakX = rX, lX
        # stronger or equal child of Y
        if stronger(lY,rY) or equal(lY,rY):
            strongY, weakY = lY, rY
        else:
            strongY, weakY = rY, lY
        if asymmetry_compare(strongX, posX, strongY, posY):
            return True
        if asymmetry_compare(strongY, posY, strongX, posX):
            return False
        if asymmetry_compare(weakX, posX, weakY, posY):
            return True
        if asymmetry_compare(weakY, posY, weakX, posX):
            return False
        return False  # equal asymmetricity

    return asymmetry_compare

asymmetry_compare = make_comparator()

def reorder(t, pos):
    # pos: 0=root or left child, 1=right child
    if t[0] == 'leaf':
        return t
    l, r = t[1], t[2]
    # reorder children recursively
    nl = reorder(l,0)
    nr = reorder(r,1)
    # at this node reorder based on rules:
    # if pos == 0 (root or left child), left child must be >= right child asymmetricity (left >= right)
    # so if left is weaker asymmetricity than right, swap so left is stronger or equal
    # stronger asymmetricity = smaller in asymmetry_compare ordering
    # so if asymmetry_compare(nr,1,nl,0) == True, means right stronger than left => swap
    # if equal asymmetricity order doesn't matter
    if pos == 0:
        # want left stronger or equal to right
        if asymmetry_compare(nr,1,nl,0):
            nl, nr = nr, nl
    else:
        # pos == 1 means right child
        # want right stronger or equal to left
        if asymmetry_compare(nl,0,nr,1):
            nl, nr = nr, nl
    return ('node', nl, nr)

def tree_to_str(t):
    if t[0] == 'leaf':
        return 'x'
    return '(' + tree_to_str(t[1]) + ' ' + tree_to_str(t[2]) + ')'

def main():
    input_lines = []
    for line in sys.stdin:
        line=line.strip()
        if line == '0':
            break
        input_lines.append(line)
    for line in input_lines:
        t = parse_tree(line)
        t2 = reorder(t,0)
        print(tree_to_str(t2))

if __name__ == '__main__':
    main()