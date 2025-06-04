import sys
from collections import defaultdict

sys.setrecursionlimit(110000)

def compute_depth(node_index):
    if node_index not in adjacency_list:
        return 0
    if memoization[node_index] >= 0:
        return memoization[node_index]
    subtree_values = sorted(-compute_depth(child_index) for child_index in adjacency_list[node_index])
    memoization[node_index] = max(
        node_index + 1 - subtree_values[current_index] for current_index in range(len(subtree_values))
    )
    return memoization[node_index]

node_count = int(sys.stdin.readline())
memoization = [-1] * node_count
adjacency_list = defaultdict(list)
for child_index, _ in enumerate(range(node_count - 1)):
    parent_index = int(sys.stdin.readline()) - 1
    adjacency_list[parent_index].append(child_index + 1)
compute_depth(node_count // 2)
print(compute_depth(0))