import sys
sys.setrecursionlimit(10**7)

def parse_tree(s):
    # parse string s and return (tree, next_index)
    # tree = (left_subtree, value, right_subtree)
    # if empty string, return (None, start_index)
    if not s:
        return None, 0

    def parse_node(i):
        if i >= len(s):
            return None, i
        # parse left subtree
        if s[i] == '(':
            left, i = parse_node(i + 1)
            if s[i] != ')':
                raise ValueError("Expected ')'")
            i += 1
        else:
            left = None

        # parse [value]
        if s[i] != '[':
            raise ValueError("Expected '['")
        j = i + 1
        while s[j] != ']':
            j += 1
        val = int(s[i + 1:j])
        i = j + 1

        # parse right subtree
        if i < len(s) and s[i] == '(':
            right, i = parse_node(i + 1)
            if s[i] != ')':
                raise ValueError("Expected ')'")
            i += 1
        else:
            right = None

        return (left, val, right), i

    tree, idx = parse_node(0)
    if idx != len(s):
        raise ValueError("Extra characters after parse")
    return tree

def compose(t1, t2):
    # t = (left, val, right) or None
    if t1 is None or t2 is None:
        return None
    left1, val1, right1 = t1
    left2, val2, right2 = t2
    new_val = val1 + val2

    if left1 is not None and left2 is not None:
        new_left = compose(left1, left2)
    else:
        new_left = None

    if right1 is not None and right2 is not None:
        new_right = compose(right1, right2)
    else:
        new_right = None

    return (new_left, new_val, new_right)

def serialize_tree(t):
    if t is None:
        return ''
    left, val, right = t
    return '(' + serialize_tree(left) + ')[' + str(val) + '](' + serialize_tree(right) + ')'

def main():
    A = input().strip()
    B = input().strip()
    t1 = parse_tree(A)
    t2 = parse_tree(B)
    t = compose(t1, t2)
    print(serialize_tree(t))

if __name__ == '__main__':
    main()