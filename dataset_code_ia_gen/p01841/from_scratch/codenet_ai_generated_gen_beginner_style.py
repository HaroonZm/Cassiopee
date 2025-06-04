def parse_tree(s, i=0):
    if i >= len(s) or s[i] == '':
        return None, i
    # parse left child
    assert s[i] == '('
    i += 1
    left, i = parse_tree(s, i)
    assert s[i] == ')'
    i += 1
    # parse value
    assert s[i] == '['
    i += 1
    val_str = ''
    while s[i].isdigit():
        val_str += s[i]
        i += 1
    val = int(val_str)
    assert s[i] == ']'
    i += 1
    # parse right child
    assert s[i] == '('
    i += 1
    right, i = parse_tree(s, i)
    assert s[i] == ')'
    i += 1
    return {'val': val, 'left': left, 'right': right}, i

def combine(t1, t2):
    if t1 is None or t2 is None:
        # If either tree is None, no node created
        # But per problem statement input is never empty for root,
        # still children might be None
        return None
    new_val = t1['val'] + t2['val']
    # combine left children only if both present
    if t1['left'] is not None and t2['left'] is not None:
        new_left = combine(t1['left'], t2['left'])
    else:
        new_left = None
    # combine right children only if both present
    if t1['right'] is not None and t2['right'] is not None:
        new_right = combine(t1['right'], t2['right'])
    else:
        new_right = None
    return {'val': new_val, 'left': new_left, 'right': new_right}

def serialize(t):
    if t is None:
        return ''
    left_str = serialize(t['left'])
    right_str = serialize(t['right'])
    return '(' + left_str + ')[' + str(t['val']) + '](' + right_str + ')'

A = input()
B = input()
tree1, _ = parse_tree(A)
tree2, _ = parse_tree(B)
combined = combine(tree1, tree2)
print(serialize(combined))