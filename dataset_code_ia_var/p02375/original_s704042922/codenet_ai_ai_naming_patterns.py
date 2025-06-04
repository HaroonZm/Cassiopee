import sys
from collections import deque
from typing import List

sys.setrecursionlimit(200000)

node_count = int(input())
adjacency_list: List[List[int]] = [[0]] * node_count
for node_index in range(node_count):
    input_data = list(map(int, input().split()))
    child_count, *children = input_data
    adjacency_list[node_index] = children

heavy_child: List[int] = [0] * node_count
parent_node: List[int] = [None] * node_count

def compute_heavy_child(current_node: int) -> int:
    subtree_size = 1
    heavy_candidate = None
    max_subtree = 0
    for child in adjacency_list[current_node]:
        parent_node[child] = current_node
        child_subtree_size = compute_heavy_child(child)
        if max_subtree < child_subtree_size:
            heavy_candidate = child
            max_subtree = child_subtree_size
        subtree_size += child_subtree_size
    heavy_child[current_node] = heavy_candidate
    return subtree_size

compute_heavy_child(0)

decomposition_chains: List[List[int]] = []
chain_depths: List[int] = []
chain_index: List[int] = [0] * node_count
node_chain_position: List[int] = [0] * node_count

pending_nodes = deque([(0, 0)])
while pending_nodes:
    chain_root, chain_depth = pending_nodes.popleft()
    current_chain: List[int] = []
    current_chain_index = len(decomposition_chains)
    v = chain_root
    while v is not None:
        node_chain_position[v] = len(current_chain)
        current_chain.append(v)
        chain_index[v] = current_chain_index
        heavy_c = heavy_child[v]
        for child in adjacency_list[v]:
            if child == heavy_c:
                continue
            pending_nodes.append((child, chain_depth + 1))
        v = heavy_c
    decomposition_chains.append(current_chain)
    chain_depths.append(chain_depth)

chain_lengths = list(map(len, decomposition_chains))
fenwick_diff: List[List[int]] = [[0] * (cl + 1) for cl in chain_lengths]
fenwick_sum: List[List[int]] = [[0] * (cl + 1) for cl in chain_lengths]

def fenwick_add(tree_size: int, tree: List[int], index: int, value: int) -> None:
    while index <= tree_size:
        tree[index] += value
        index += index & -index

def fenwick_get(tree_size: int, tree: List[int], index: int) -> int:
    result = 0
    while index:
        result += tree[index]
        index -= index & -index
    return result

def update_path_addition(target_node: int, value: int) -> None:
    while target_node is not None:
        chain_id = chain_index[target_node]
        position = node_chain_position[target_node]
        fenwick_add(chain_lengths[chain_id], fenwick_diff[chain_id], position + 1, -value)
        fenwick_add(chain_lengths[chain_id], fenwick_diff[chain_id], 1, value)
        fenwick_add(chain_lengths[chain_id], fenwick_sum[chain_id], position + 1, value * (position + 1))
        target_node = parent_node[decomposition_chains[chain_id][0]]

def get_path_sum(target_node: int) -> int:
    aggregate = -fenwick_get(chain_lengths[0], fenwick_diff[0], 1) - fenwick_get(chain_lengths[0], fenwick_sum[0], 1)
    while target_node is not None:
        chain_id = chain_index[target_node]
        position = node_chain_position[target_node]
        aggregate += fenwick_get(chain_lengths[chain_id], fenwick_diff[chain_id], position + 1) * (position + 1)
        aggregate += fenwick_get(chain_lengths[chain_id], fenwick_sum[chain_id], position + 1)
        target_node = parent_node[decomposition_chains[chain_id][0]]
    return aggregate

query_count = int(input())
output_results = []
for _ in range(query_count):
    operation, *params = map(int, input().split())
    if operation:
        query_node = params[0]
        output_results.append(str(get_path_sum(query_node)))
    else:
        update_node, increment_value = params
        update_path_addition(update_node, increment_value)
print("\n".join(output_results))