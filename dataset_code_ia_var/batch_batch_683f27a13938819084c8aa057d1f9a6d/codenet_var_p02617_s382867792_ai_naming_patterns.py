import sys
def read_input():
    return sys.stdin.readline()

node_count = int(read_input())
total_sum = 0
for node_idx in range(1, node_count + 1):
    total_sum += node_idx * (node_idx + 1) // 2

for edge_idx in range(node_count - 1):
    node_u, node_v = map(int, read_input().split())
    min_node = min(node_u, node_v)
    max_node = max(node_u, node_v)
    total_sum -= (node_count - max_node + 1) * min_node

print(total_sum)