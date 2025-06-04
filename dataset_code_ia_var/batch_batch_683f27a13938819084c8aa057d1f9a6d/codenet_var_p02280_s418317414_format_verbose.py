#!/usr/bin/env python

import sys

class BinaryTreeNode(object):
    def __init__(self):
        self.parent_index = -1
        self.node_type = 'leaf'
        self.depth_in_tree = 0
        self.children_indices = []
        self.child_count = 0
        self.sibling_index = -1
        self.node_height = 0

def compute_node_depth(current_node, current_depth = 0):
    if not current_node.children_indices:
        current_node.depth_in_tree = current_depth
        return current_node.depth_in_tree

    current_node.depth_in_tree = current_depth

    if current_node.children_indices[0] != -1:
        compute_node_depth(all_tree_nodes[current_node.children_indices[0]], current_depth + 1)

    if current_node.children_indices[1] != -1:
        compute_node_depth(all_tree_nodes[current_node.children_indices[1]], current_depth + 1)

    return current_node.depth_in_tree

def compute_node_height(current_node):
    left_height = 0
    right_height = 0

    if not current_node.children_indices:
        return 0

    if current_node.children_indices[0] != -1:
        left_height = compute_node_height(all_tree_nodes[current_node.children_indices[0]]) + 1

    if current_node.children_indices[1] != -1:
        right_height = compute_node_height(all_tree_nodes[current_node.children_indices[1]]) + 1

    current_node.node_height = max(left_height, right_height)
    return current_node.node_height

def build_binary_tree(node_data_array):
    for node_info in node_data_array:
        node_index, *children_indices = [int(x) for x in node_info]

        if children_indices != [-1, -1]:
            all_tree_nodes[node_index].node_type = 'internal node'
            all_tree_nodes[node_index].children_indices = children_indices
            all_tree_nodes[node_index].child_count = 1 if (-1 in children_indices) else 2
        else:
            continue

        for child_idx in children_indices:
            if child_idx == -1:
                continue
            all_tree_nodes[child_idx].parent_index = node_index
            all_tree_nodes[child_idx].sibling_index = sum(children_indices) - child_idx

    root_node_index = [i for i, node in enumerate(all_tree_nodes) if node.parent_index == -1][0]
    all_tree_nodes[root_node_index].node_type = 'root'

    compute_node_depth(all_tree_nodes[root_node_index])
    compute_node_height(all_tree_nodes[root_node_index])

    return all_tree_nodes

def display_node_information(node_instance):
    print('parent = ' + str(node_instance.parent_index) + ',', end=' ')
    print('sibling = ' + str(node_instance.sibling_index) + ',', end=' ')
    print('degree = ' + str(node_instance.child_count) + ',', end=' ')
    print('depth = ' + str(node_instance.depth_in_tree) + ',', end=' ')
    print('height = ' + str(node_instance.node_height) + ',', end=' ')
    print(node_instance.node_type)
    return None

if __name__ == '__main__':
    raw_input_lines = sys.stdin.readlines()
    number_of_nodes = int(raw_input_lines[0])
    input_node_data = list(map(lambda line: line.split(), raw_input_lines[1:]))

    all_tree_nodes = [BinaryTreeNode() for _ in range(number_of_nodes)]
    constructed_tree_nodes = build_binary_tree(node_data_array = input_node_data)

    for node_index, current_node in enumerate(constructed_tree_nodes):
        print('node ' + str(node_index) + ':', end=' ')
        display_node_information(node_instance = current_node)