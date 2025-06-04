from collections import deque

number_of_nodes, number_of_edges = map(int, input().split())

adjacency_list = [[] for _ in range(number_of_nodes + 1)]

for _ in range(number_of_edges):
    node_a, node_b = map(int, input().split())
    adjacency_list[node_a].append(node_b)
    adjacency_list[node_b].append(node_a)

parent_nodes = [-1] * (number_of_nodes + 1)
parent_nodes[0] = 0  # Dummy value for unused index
parent_nodes[1] = 0  # Root node has no parent

bfs_queue = deque()
bfs_queue.append(1)

while bfs_queue:
    current_node = bfs_queue.popleft()
    for neighbor_node in adjacency_list[current_node]:
        if parent_nodes[neighbor_node] != -1:
            continue
        parent_nodes[neighbor_node] = current_node
        bfs_queue.append(neighbor_node)

parent_nodes_excluding_root = parent_nodes[2:]

print("Yes")
for parent in parent_nodes_excluding_root:
    print(parent)