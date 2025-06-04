import sys
sys.setrecursionlimit(1 << 25)
input_read_line = sys.stdin.readline
range_iter = range
enumerate_iter = enumerate

def to_zero_based(val):
    return int(val) - 1

def input_ints(zero_base=None):
    values = map(int, input_read_line().split())
    if zero_base is None:
        return list(values)
    else:
        return list(map(lambda elem: elem - zero_base, values))

def input_single_int():
    return int(input_read_line())

from bisect import bisect_left as bisect_l, bisect_right as bisect_r
from collections import defaultdict as def_dict

node_count = input_single_int()
node_values = input_ints()
adjacency_list = def_dict(list)
for edge_idx in range_iter(node_count - 1):
    node_u, node_v = input_ints(zero_base=1)
    adjacency_list[node_u].append(node_v)
    adjacency_list[node_v].append(node_u)

current_lis = []
result_lis_lengths = [0] * node_count

def depth_first_search(current_node, parent_node):
    node_value = node_values[current_node]
    lis_position = bisect_l(current_lis, node_value)
    did_append = False
    if lis_position == len(current_lis):
        current_lis.append(node_value)
        did_append = True
    else:
        previous_value = current_lis[lis_position]
        current_lis[lis_position] = node_value

    result_lis_lengths[current_node] = len(current_lis)
    for neighbor_node in adjacency_list[current_node]:
        if neighbor_node == parent_node:
            continue
        depth_first_search(neighbor_node, current_node)

    if did_append:
        del current_lis[lis_position]
    else:
        current_lis[lis_position] = previous_value

depth_first_search(0, -1)
print(*result_lis_lengths, sep='\n')