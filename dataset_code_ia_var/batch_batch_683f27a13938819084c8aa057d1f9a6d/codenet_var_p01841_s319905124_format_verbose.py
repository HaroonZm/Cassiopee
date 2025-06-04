from sys import setrecursionlimit

setrecursionlimit(10 ** 8)

first_tree_input = input()
second_tree_input = input()

first_tree_structure = [[-1] * 3 for _ in range(1000)]
second_tree_structure = [[-1] * 3 for _ in range(1000)]

class TreeInputParser:
    def __init__(self, input_string):
        self.input_string = input_string
        self.current_position = 0

def peek_next_character(parser):
    if parser.current_position < len(parser.input_string):
        return parser.input_string[parser.current_position]
    else:
        return -1

def advance_position(parser):
    parser.current_position += 1

def build_tree_structure(parser, tree_structure, node_index_reference):
    advance_position(parser)
    
    if peek_next_character(parser) == ')':
        advance_position(parser)
        return -1
    
    current_node_index = node_index_reference[0]
    node_index_reference[0] += 1
    
    left_child_index_value = node_index_reference[0]
    left_child_index = build_tree_structure(parser, tree_structure, node_index_reference)
    
    node_value = extract_node_value(parser, tree_structure)
    
    node_index_reference[0] += 1
    right_child_index_value = node_index_reference[0]
    right_child_index = build_tree_structure(parser, tree_structure, node_index_reference)
    
    tree_structure[current_node_index] = [node_value, left_child_index_value, right_child_index_value]
    
    advance_position(parser)

def extract_node_value(parser, tree_structure):
    node_value = 0
    advance_position(parser)
    while peek_next_character(parser) != ']':
        node_value = node_value * 10 + int(peek_next_character(parser))
        advance_position(parser)
    advance_position(parser)
    return node_value

build_tree_structure(TreeInputParser('(' + first_tree_input + ')'), first_tree_structure, [0])
build_tree_structure(TreeInputParser('(' + second_tree_input + ')'), second_tree_structure, [0])

def merge_tree_sum(node_index_in_first_tree, node_index_in_second_tree):
    if first_tree_structure[node_index_in_first_tree][0] == -1 or second_tree_structure[node_index_in_second_tree][0] == -1:
        return '()'
    
    merged_node_value = '[' + str(first_tree_structure[node_index_in_first_tree][0] + second_tree_structure[node_index_in_second_tree][0]) + ']'
    
    left_merged_subtree = merge_tree_sum(first_tree_structure[node_index_in_first_tree][1], second_tree_structure[node_index_in_second_tree][1])
    right_merged_subtree = merge_tree_sum(first_tree_structure[node_index_in_first_tree][2], second_tree_structure[node_index_in_second_tree][2])
    
    return '(' + left_merged_subtree + merged_node_value + right_merged_subtree + ')'

print(merge_tree_sum(0, 0)[1:-1])