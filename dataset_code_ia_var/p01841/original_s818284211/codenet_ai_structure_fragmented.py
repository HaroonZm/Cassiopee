class binary_tree():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inc_count_if_fr(current, fr, count):
    if current == fr:
        return count + 1
    return count

def dec_count_if_to(current, to, count):
    if current == to:
        return count - 1
    return count

def is_valid_close(current, to, count):
    return current == to and count == 1

def find_corres_bra_from_index(s, fr, to, i, count, x):
    if i >= len(s):
        return x
    count = inc_count_if_fr(s[i], fr, count)
    if is_valid_close(s[i], to, count):
        return i
    if s[i] == to and count != 1:
        count = dec_count_if_to(s[i], to, count)
    return find_corres_bra_from_index(s, fr, to, i+1, count, x)

def find_corres_bra(s, fr, to):
    return find_corres_bra_from_index(s, fr, to, 0, 0, -1)

def is_empty_string(s):
    return s == ''

def slice_portion(s, start, end):
    return s[start:end]

def get_left_substring(s, x0, x1):
    return slice_portion(s, x0+1, x1-1)

def get_number_substring(s, x1, x2):
    return slice_portion(s, x1+1, x2-1)

def get_right_substring(s, x2):
    return slice_portion(s, x2+1, -1)

def parse_left(s, x0, x1):
    return make_tree(get_left_substring(s, x0, x1))

def parse_right(s, x2):
    return make_tree(get_right_substring(s, x2))

def extract_value(s, x1, x2):
    return int(get_number_substring(s, x1, x2))

def build_tree(value, left, right):
    return binary_tree(value, left, right)

def inner_make_tree(s, x0, x1, x2):
    left = parse_left(s, x0, x1)
    value = extract_value(s, x1, x2)
    right = parse_right(s, x2)
    return build_tree(value, left, right)

def make_tree(s):
    if is_empty_string(s):
        return None
    x0 = 0
    x1 = find_corres_bra(s, '(', ')') + 1
    x2 = x1 + find_corres_bra(s[x1:], '[', ']') + 1
    return inner_make_tree(s, x0, x1, x2)

def is_not_none(x):
    return x is not None

def sum_values(val1, val2):
    return val1 + val2

def synthe_left(t1, t2):
    if is_not_none(t1.left) and is_not_none(t2.left):
        return synthe_trees(t1.left, t2.left)
    return None

def synthe_right(t1, t2):
    if is_not_none(t1.right) and is_not_none(t2.right):
        return synthe_trees(t1.right, t2.right)
    return None

def create_synthe_node(t1, t2):
    value = sum_values(t1.value, t2.value)
    left = synthe_left(t1, t2)
    right = synthe_right(t1, t2)
    return binary_tree(value, left, right)

def synthe_trees(t1, t2):
    return create_synthe_node(t1, t2)

def is_tree_none(tree):
    return tree is None

def tree_to_str_left(tree):
    return tree_to_str(tree.left)

def tree_to_str_right(tree):
    return tree_to_str(tree.right)

def tree_value_to_str(tree):
    return str(tree.value)

def build_tree_str(left_str, value_str, right_str):
    return '(' + left_str + ')' + '[' + value_str + ']' + '(' + right_str + ')'

def tree_to_str(tree):
    if is_tree_none(tree):
        return ''
    left_str = tree_to_str_left(tree)
    value_str = tree_value_to_str(tree)
    right_str = tree_to_str_right(tree)
    return build_tree_str(left_str, value_str, right_str)

def input_tree():
    return make_tree(input())

def main():
    t1 = input_tree()
    t2 = input_tree()
    tree = synthe_trees(t1, t2)
    print(tree_to_str(tree))

main()