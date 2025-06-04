import sys
input = sys.stdin.readline

node_count = int(input())
log_node_count = (node_count - 1).bit_length()

parent = [[-1] * (log_node_count + 1) for _ in range(node_count)]
adjacency_list = [[] for _ in range(node_count)]
for node_index in range(node_count):
    input_list = list(map(int, input().split()))
    child_count = input_list[0]
    children = input_list[1:]
    adjacency_list[node_index] = children
    for child in children:
        parent[child][0] = node_index

query_count = int(input())
queries = [list(map(int, input().split())) for _ in range(query_count)]

node_depth = [-1] * node_count
bfs_queue = [0]
node_depth[0] = 0
current_depth = 0
while bfs_queue:
    next_bfs_queue = []
    current_depth += 1
    for current_node in bfs_queue:
        for adjacent_node in adjacency_list[current_node]:
            if node_depth[adjacent_node] == -1:
                node_depth[adjacent_node] = current_depth
                next_bfs_queue.append(adjacent_node)
    bfs_queue = next_bfs_queue

for level in range(log_node_count):
    for node_index in range(node_count):
        if parent[node_index][level] == -1:
            parent[node_index][level + 1] = -1
        else:
            parent[node_index][level + 1] = parent[parent[node_index][level]][level]

def lowest_common_ancestor(node_u, node_v):
    depth_diff = node_depth[node_v] - node_depth[node_u]
    if depth_diff < 0:
        node_u, node_v = node_v, node_u
        depth_diff = -depth_diff
    for level in range(log_node_count + 1):
        if depth_diff & 1:
            node_v = parent[node_v][level]
        depth_diff >>= 1
    if node_u == node_v:
        return node_u
    for level in reversed(range(log_node_count)):
        parent_u = parent[node_u][level]
        parent_v = parent[node_v][level]
        if parent_u != parent_v:
            node_u, node_v = parent_u, parent_v
    return parent[node_u][0]

for query_node_u, query_node_v in queries:
    print(lowest_common_ancestor(query_node_u, query_node_v))