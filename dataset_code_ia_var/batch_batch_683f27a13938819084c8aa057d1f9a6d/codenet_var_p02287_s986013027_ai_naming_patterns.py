import sys
system_input_reader = sys.stdin.readline

node_count = int(system_input_reader())
binary_tree_keys = list(map(int, system_input_reader().split()))

for node_index in range(1, node_count + 1):
    node_info_str = ""
    node_info_str += "node {idx}: key = {key}, ".format(idx=node_index, key=binary_tree_keys[node_index - 1])
    parent_index = node_index // 2
    left_index = node_index * 2
    right_index = node_index * 2 + 1

    if parent_index > 0:
        node_info_str += "parent key = {key}, ".format(key=binary_tree_keys[parent_index - 1])
    if left_index <= node_count:
        node_info_str += "left key = {key}, ".format(key=binary_tree_keys[left_index - 1])
    if right_index <= node_count:
        node_info_str += "right key = {key}, ".format(key=binary_tree_keys[right_index - 1])

    print(node_info_str)