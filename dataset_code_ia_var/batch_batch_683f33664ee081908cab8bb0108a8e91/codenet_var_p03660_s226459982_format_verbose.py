import queue

# Read the number of nodes in the tree
number_of_nodes = int(input())

# Read the edges of the tree
edges_list = [list(map(int, input().split())) for _ in range(number_of_nodes - 1)]

# Build the adjacency list for the tree
adjacency_dict = {}
for node_u, node_v in edges_list:
    if node_u not in adjacency_dict:
        adjacency_dict[node_u] = [node_v]
    else:
        adjacency_dict[node_u].append(node_v)
    if node_v not in adjacency_dict:
        adjacency_dict[node_v] = [node_u]
    else:
        adjacency_dict[node_v].append(node_u)

# Distance array: stores the distance from the root node (node 1)
distance_from_root = [-1] * (number_of_nodes + 1)

# BFS queue initialization
bfs_queue = queue.Queue()
queue_put = bfs_queue.put
queue_get = bfs_queue.get

# Start BFS from root node 1
queue_put(1)
distance_from_root[1] = 1
while not bfs_queue.empty():
    current_node = queue_get()
    if current_node in adjacency_dict:
        for adjacent_node in adjacency_dict[current_node]:
            if distance_from_root[adjacent_node] == -1:
                distance_from_root[adjacent_node] = distance_from_root[current_node] + 1
                queue_put(adjacent_node)

# Find the path from the last node to the root, storing the path taken
path_from_n_to_1 = [number_of_nodes]
current_in_path = number_of_nodes
while current_in_path != 1:
    for adjacent_node in adjacency_dict[current_in_path]:
        if distance_from_root[adjacent_node] < distance_from_root[current_in_path]:
            path_from_n_to_1.append(adjacent_node)
            current_in_path = adjacent_node
            break

# Find the middle node along the shortest path between node 1 and node N
mid_node_on_path = path_from_n_to_1[len(path_from_n_to_1) // 2 - 1]

# Count how many nodes can be reached from mid_node_on_path without going back toward node 1
reachable_node_count = 1
queue_put(mid_node_on_path)
while not bfs_queue.empty():
    current_node = queue_get()
    if current_node in adjacency_dict:
        for adjacent_node in adjacency_dict[current_node]:
            if distance_from_root[adjacent_node] > distance_from_root[current_node]:
                reachable_node_count += 1
                queue_put(adjacent_node)

# Determine which player wins based on the reachable nodes
player_names = ["Fennec", "Snuke"]
print(player_names[reachable_node_count >= number_of_nodes - reachable_node_count])