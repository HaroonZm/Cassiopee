import sys
from bisect import bisect_right as bisect_right_fn

sys.setrecursionlimit(100000)

NODE_COUNT = int(input())
PARENT_MATRIX = [[None] * 20 for _ in range(NODE_COUNT)]

for node_idx in range(NODE_COUNT):
    child_list_input = list(map(int, input().split()))
    child_indices = child_list_input[1:]
    for child_idx in child_indices:
        PARENT_MATRIX[child_idx][0] = node_idx

for lev in range(1, 20):
    for node_idx in range(NODE_COUNT):
        prev_parent = PARENT_MATRIX[node_idx][lev - 1]
        if prev_parent is not None:
            PARENT_MATRIX[node_idx][lev] = PARENT_MATRIX[prev_parent][lev - 1]

NODE_DEPTHS = [None for _ in range(NODE_COUNT)]
NODE_DEPTHS[0] = 0

def compute_node_depth(node_id):
    if NODE_DEPTHS[node_id] is not None:
        return
    parent_id = PARENT_MATRIX[node_id][0]
    if NODE_DEPTHS[parent_id] is None:
        compute_node_depth(parent_id)
    NODE_DEPTHS[node_id] = NODE_DEPTHS[parent_id] + 1

for node_id in range(NODE_COUNT):
    compute_node_depth(node_id)

BINARY_LIFTS = [1 << i for i in range(20)]

def lift_node_to_ancestor(start_node, steps_to_lift):
    if steps_to_lift == 0:
        return start_node
    lift_idx = bisect_right_fn(BINARY_LIFTS, steps_to_lift) - 1
    next_node = PARENT_MATRIX[start_node][lift_idx]
    return lift_node_to_ancestor(next_node, steps_to_lift - BINARY_LIFTS[lift_idx])

def internal_lca_query(node_a, node_b):
    if node_a == node_b:
        return node_a
    for level in range(1, 20):
        if PARENT_MATRIX[node_a][level] == PARENT_MATRIX[node_b][level]:
            return internal_lca_query(PARENT_MATRIX[node_a][level - 1], PARENT_MATRIX[node_b][level - 1])

def find_lowest_common_ancestor(node_a, node_b):
    if NODE_DEPTHS[node_a] < NODE_DEPTHS[node_b]:
        node_b = lift_node_to_ancestor(node_b, NODE_DEPTHS[node_b] - NODE_DEPTHS[node_a])
    elif NODE_DEPTHS[node_a] > NODE_DEPTHS[node_b]:
        node_a = lift_node_to_ancestor(node_a, NODE_DEPTHS[node_a] - NODE_DEPTHS[node_b])
    return internal_lca_query(node_a, node_b)

QUERY_COUNT = int(input())
for _ in range(QUERY_COUNT):
    query_node_a, query_node_b = map(int, input().split())
    print(find_lowest_common_ancestor(query_node_a, query_node_b))