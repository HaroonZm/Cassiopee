#!/usr/bin/env python

import sys

class Node(object):
    def __init__(self):
        # init node as a single leaf node.
        self.parent = -1
        self.type = 'leaf'
        self.depth = 0
        self.children = []
        self.degree = 0
        self.sibling = -1
        self.height = 0

def get_depth(v, depth=0):
    if not v.children:
        # print('rt', v.parent, v.depth, depth)
        v.depth = depth
        return v.depth
    v.depth = depth
    # print('out', v.parent, v.depth, v.children, depth)
    if v.children[0] != -1:
        get_depth(node_list[v.children[0]], depth + 1)

    if v.children[1] != -1:
        get_depth(node_list[v.children[1]], depth + 1)
    return v.depth

def get_height(v):
    h1, h2 = 0, 0

    # leaf's height is 0, children: []
    if not v.children:
        return 0

    if v.children[0] != -1:
        h1 = get_height(node_list[v.children[0]]) + 1

    if v.children[1] != -1:
        h2 = get_height(node_list[v.children[1]]) + 1

    v.height = max(h1, h2)
    return v.height

def generate_tree(_array):
    # add info of each node of a ordered tree
    for each in _array:
        idx, *children = [int(x) for x in each]
        # assert len(children) == 2
        if children != [-1, -1]:
            node_list[idx].type = 'internal node'
            node_list[idx].children = children
            node_list[idx].degree = 1 if (-1 in children) else 2
        else:
            # node is leaf as default, children: []
            continue

        for child_idx in children:
            # non-existent node: no parent or sibling
            if child_idx == -1:
                continue
            node_list[child_idx].parent = idx
            node_list[child_idx].sibling = sum(children) - child_idx

    root_idx = [i for i, x in enumerate(node_list) if x.parent == -1][0]
    node_list[root_idx].type = 'root'

    # add node depth info -- using DFS
    get_depth(node_list[root_idx])
    get_height(node_list[root_idx])

    return node_list

def print_result(_node):
    print('parent = ' + str(_node.parent) + ',', end=' ')
    print('sibling = ' + str(_node.sibling) + ',', end=' ')
    print('degree = ' + str(_node.degree) + ',', end=' ')
    print('depth = ' + str(_node.depth) + ',', end=' ')
    print('height = ' + str(_node.height) + ',', end=' ')
    print(_node.type)
    return None

if __name__ == '__main__':
    _input = sys.stdin.readlines()
    array_length = int(_input[0])
    array = list(map(lambda x: x.split(), _input[1:]))
    # assert len(array) == array_length

    node_list = [Node() for _ in range(array_length)]
    ans = generate_tree(_array=array)
    for key, node in enumerate(ans):
        print('node ' + str(key) + ':', end=' ')
        print_result(_node=node)