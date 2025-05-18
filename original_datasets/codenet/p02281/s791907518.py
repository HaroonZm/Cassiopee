#!/usr/bin/env python

"""
input:
9
0 1 4
1 2 3
2 -1 -1
3 -1 -1
4 5 8
5 6 7
6 -1 -1
7 -1 -1
8 -1 -1

output:
Preorder
 0 1 2 3 4 5 6 7 8
Inorder
 2 1 3 0 6 5 7 4 8
Postorder
 2 3 1 6 7 5 8 4 0
"""

import sys

class Node(object):
    def __init__(self):
        # init node as a single leaf node.
        self.parent = -1
        self.children = []
        self.index = -1

def pre_parse(v):
    print(' ' + str(v.index), end='')

    left_child_idx = v.children[0]
    right_child_idx = v.children[1]

    if left_child_idx != -1:
        pre_parse(node_list[left_child_idx])

    if right_child_idx != -1:
        pre_parse(node_list[right_child_idx])

    return v.index

def in_parse(v):
    left_child_idx = v.children[0]
    right_child_idx = v.children[1]

    if left_child_idx != -1:
        in_parse(node_list[left_child_idx])

    print(' ' + str(v.index), end='')

    if right_child_idx != -1:
        in_parse(node_list[right_child_idx])

    return v.index

def post_parse(v):
    left_child_idx = v.children[0]
    right_child_idx = v.children[1]

    if left_child_idx != -1:
        post_parse(node_list[left_child_idx])

    if right_child_idx != -1:
        post_parse(node_list[right_child_idx])

    print(' ' + str(v.index), end='')

    return v.index

def generate_tree(_array):
    # add info of each node of a ordered tree
    for each in _array:
        idx, *children = [int(x) for x in each]
        # assert len(children) == 2 and idx >= 0
        node_list[idx].index = idx
        node_list[idx].children = children

        for child_idx in children:
            # non-existent node: no parent
            if child_idx == -1:
                continue
            node_list[child_idx].parent = idx

    # find root node
    root_idx = [x.index for x in node_list if x.parent == -1][0]
    root_node = node_list[root_idx]

    # tree walk in 3 ways
    print('Preorder')
    pre_parse(root_node)
    print('\n' + 'Inorder')
    in_parse(root_node)
    print('\n' + 'Postorder')
    post_parse(root_node)
    print('')

    return node_list

if __name__ == '__main__':
    _input = sys.stdin.readlines()
    array_length = int(_input[0])
    array = list(map(lambda x: x.split(), _input[1:]))
    # assert len(array) == array_length

    node_list = [Node() for _ in range(array_length)]
    ans = generate_tree(_array=array)