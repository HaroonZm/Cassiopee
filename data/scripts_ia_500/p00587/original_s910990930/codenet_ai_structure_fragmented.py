import sys

def is_open_paren(char):
    return char == '('

def is_close_paren(char):
    return char == ')'

def increment_layer_if_open(char, layer):
    if is_open_paren(char):
        return layer + 1
    return layer

def decrement_layer_if_close(char, layer):
    if is_close_paren(char):
        return layer - 1
    return layer

def is_inside_first_layer(layer):
    return layer == 1

def is_comma_position(c, layer):
    return (c != '(' and c != ')') and layer == 1

def searchcenter(string):
    layer = 0
    for index, c in enumerate(string):
        layer = increment_layer_if_open(c, layer)
        if is_close_paren(c):
            layer = decrement_layer_if_close(c, layer)
        if is_inside_first_layer(layer) and (not is_open_paren(c)) and (not is_close_paren(c)):
            return index
    return -1

def either_tree_have(t1len, t2len, center1, center2):
    if center1 == 1 and center2 == 1:
        return "right"
    if center1 == t1len - 2 and center2 == t2len - 2:
        return "left"
    if 4 <= center1 <= t1len - 5 and 4 <= center2 <= t2len - 5:
        return "both"
    if center1 == 1 and center2 == t2len - 2:
        return "t1_rightandt2_left"
    if center1 == t1len - 2 and center2 == 1:
        return "t1_leftandt2_right"
    if center1 == 1 and 4 <= center2 <= t2len - 5:
        return "t1_rightandt2_both"
    if center1 == t1len - 2 and 4 <= center2 <= t2len - 5:
        return "t1_leftandt2_both"
    if 4 <= center1 <= t1len - 5 and center2 == 1:
        return "t1_bothandt2_right"
    if 4 <= center1 <= t1len - 5 and center2 == t2len - 2:
        return "t1_bothandt2_left"
    return "no"

def tree_length_is_three(length1, length2):
    return length1 == 3 or length2 == 3

def swap_tree_if_needed(tree1, tree2):
    if len(tree1) != 3 and len(tree2) == 3:
        return tree1, tree1
    if len(tree2) != 3 and len(tree1) == 3:
        return tree2, tree2
    return tree1, tree2

def get_subtree_left(tree, center):
    return tree[1:center]

def get_subtree_right(tree, center):
    return tree[center + 1:-1]

def get_subtree_left_except_one(tree):
    return tree[1:-2]

def get_subtree_right_except_one(tree):
    return tree[2:-1]

def operate_u(tree1, tree2):
    length_tree1 = len(tree1)
    length_tree2 = len(tree2)

    if tree_length_is_three(length_tree1, length_tree2):
        tree1, tree2 = swap_tree_if_needed(tree1, tree2)
        if len(tree1) == 3 and len(tree2) == 3:
            return "(,)"
    center1 = searchcenter(tree1)
    center2 = searchcenter(tree2)

    either_result = either_tree_have(length_tree1, length_tree2, center1, center2)

    if either_result == "both":
        left = operate_u(get_subtree_left(tree1, center1), get_subtree_left(tree2, center2))
        right = operate_u(get_subtree_right(tree1, center1), get_subtree_right(tree2, center2))
        return "(" + left + "," + right + ")"

    if either_result == "left":
        left = operate_u(get_subtree_left_except_one(tree1), get_subtree_left_except_one(tree2))
        return "(" + left + ",)"

    if either_result == "right":
        right = operate_u(get_subtree_right_except_one(tree1), get_subtree_right_except_one(tree2))
        return "(," + right + ")"

    if either_result == "t1_leftandt2_right":
        left = operate_u(get_subtree_left(tree1, center1), get_subtree_left(tree1, center1))
        right = operate_u(get_subtree_right(tree2, center2), get_subtree_right(tree2, center2))
        return "(" + left + "," + right + ")"

    if either_result == "t1_rightandt2_left":
        left = operate_u(get_subtree_left(tree2, center2), get_subtree_left(tree2, center2))
        right = operate_u(get_subtree_right(tree1, center1), get_subtree_right(tree1, center1))
        return "(" + left + "," + right + ")"

    if either_result == "t1_leftandt2_both":
        left = operate_u(get_subtree_left_except_one(tree1), get_subtree_left(tree2, center2))
        right = operate_u(get_subtree_right(tree2, center2), get_subtree_right(tree2, center2))
        return "(" + left + "," + right + ")"

    if either_result == "t1_rightandt2_both":
        left = operate_u(get_subtree_left(tree2, center2), get_subtree_left(tree2, center2))
        right = operate_u(get_subtree_right_except_one(tree1), get_subtree_right(tree2, center2))
        return "(" + left + "," + right + ")"

    if either_result == "t1_bothandt2_left":
        left = operate_u(get_subtree_left(tree1, center1), get_subtree_left_except_one(tree2))
        right = operate_u(get_subtree_right(tree1, center1), get_subtree_right(tree1, center1))
        return "(" + left + "," + right + ")"

    if either_result == "t1_bothandt2_right":
        left = operate_u(get_subtree_left(tree1, center1), get_subtree_left(tree1, center1))
        right = operate_u(get_subtree_right(tree1, center1), get_subtree_right_except_one(tree2))
        return "(" + left + "," + right + ")"

    return "(,)"

def both_tree_have(t1len, t2len, center1, center2):
    if 4 <= center1 <= t1len - 5 and 4 <= center2 <= t2len - 5:
        return "both"
    if (center1 == 1 and center2 == t2len - 2) or (center1 == t1len - 2 and center2 == 1):
        return "no"
    if center1 == t1len - 2 or center2 == t2len - 2:
        return "left"
    if center1 == 1 or center2 == 1:
        return "right"
    return "no"

def operate_i(tree1, tree2):
    length_tree1 = len(tree1)
    length_tree2 = len(tree2)

    if tree_length_is_three(length_tree1, length_tree2):
        return "(,)"

    center1 = searchcenter(tree1)
    center2 = searchcenter(tree2)

    both_result = both_tree_have(length_tree1, length_tree2, center1, center2)

    if both_result == "both":
        left = operate_i(tree1[1:center1], tree2[1:center2])
        right = operate_i(tree1[center1 + 1:-1], tree2[center2 + 1:-1])
        return "(" + left + "," + right + ")"

    if both_result == "left":
        left = operate_i(tree1[1:center1], tree2[1:center2])
        return "(" + left + ",)"

    if both_result == "right":
        right = operate_i(tree1[center1 + 1:-1], tree2[center2 + 1:-1])
        return "(," + right + ")"

    return "(,)"

class Process:
    def process(self):
        pass

class Intersection(Process):
    def __init__(self, tree1, tree2):
        self.tree1 = tree1
        self.tree2 = tree2
    def process(self):
        return operate_i(self.tree1, self.tree2)

class Unit(Process):
    def __init__(self, tree1, tree2):
        self.tree1 = tree1
        self.tree2 = tree2
    def process(self):
        return operate_u(self.tree1, self.tree2)

class BuilderProcess:
    def __init__(self, line):
        factor = line.split(" ")
        self.tree1 = factor[1]
        self.tree2 = factor[2][:-1]
        self.task = self.assign_task(factor[0])

    def assign_task(self, operator):
        if operator == 'i':
            return Intersection(self.tree1, self.tree2)
        else:
            return Unit(self.tree1, self.tree2)

def read_input_lines():
    lines = []
    for line in sys.stdin:
        lines.append(line)
    return lines

def process_input_lines(lines):
    for line in lines:
        builder = BuilderProcess(line)
        print(builder.task.process())

if __name__ == '__main__':
    lines = read_input_lines()
    process_input_lines(lines)