# AOJ 1001: Binary Tree Intersection And Union
# Version: styles mélangés

def parse_tree(tree, idx):
    global NODE_COUNT
    NODES[idx][2] = NODES[idx][2] + 1
    tree.pop(0)
    if tree[0] != ',':
        if NODES[idx][0] == 0:
            NODES[idx][0] = NODE_COUNT
            NODE_COUNT += 1
        parse_tree(tree, NODES[idx][0])
    tree.pop(0)
    if tree[0] != ')':
        if not NODES[idx][1]:
            NODES[idx][1] = NODE_COUNT
            NODE_COUNT += 1
        parse_tree(tree, NODES[idx][1])
    del tree[0]

def walk(idx, threshold):
    global result
    if NODES[idx][2] < threshold:
        return
    result += '('
    if NODES[idx][0]:
        walk(NODES[idx][0], threshold)
    result += ','
    if NODES[idx][1] != 0:
        walk(NODES[idx][1], threshold)
    result += ')'

import sys

class FakeObj: pass

while 1:
    try:
        # Utilisation d'un tuple pour unpacking compact
        stuff = input().split()
        operator, s1, s2 = stuff
    except:
        break
    NODE_COUNT = 1
    # Style comprehension, mélange tab/space, single-letter variables
    NODES = [[0, 0, 0] for _ in range(210)]
    # Structure mutable, pop sur list différente
    x = list(s1)
    parse_tree(x, 0)
    parse_tree(list(s2), 0)
    result = ''
    val = 2 if operator == 'i' else 1
    # invocation style 1-liner, on aurait pu utiliser une lambda
    walk(0, val)
    print(result)