import queue

node_count = int(input())
edge_list = [list(map(int, input().split())) for _ in range(node_count - 1)]

adjacency_dict = {}
for node_a, node_b in edge_list:
    if node_a not in adjacency_dict:
        adjacency_dict[node_a] = [node_b]
    else:
        adjacency_dict[node_a].append(node_b)
    if node_b not in adjacency_dict:
        adjacency_dict[node_b] = [node_a]
    else:
        adjacency_dict[node_b].append(node_a)

distance_list = [-1] * (node_count + 1)
bfs_queue = queue.Queue()
bfs_enqueue = bfs_queue.put
bfs_dequeue = bfs_queue.get
bfs_enqueue(1)
distance_list[1] = 1
while not bfs_queue.empty():
    current_node = bfs_dequeue()
    if current_node in adjacency_dict:
        for neighbor in adjacency_dict[current_node]:
            if distance_list[neighbor] == -1:
                distance_list[neighbor] = distance_list[current_node] + 1
                bfs_enqueue(neighbor)

path_nodes = [node_count]
current_path_node = node_count
while current_path_node != 1:
    for neighbor in adjacency_dict[current_path_node]:
        if distance_list[neighbor] < distance_list[current_path_node]:
            path_nodes.append(neighbor)
            current_path_node = neighbor
            break

mid_path_index = len(path_nodes) // 2 - 1
partition_start_node = path_nodes[mid_path_index]

partition_count = 1
bfs_enqueue(partition_start_node)
while not bfs_queue.empty():
    current_partition_node = bfs_dequeue()
    if current_partition_node in adjacency_dict:
        for neighbor in adjacency_dict[current_partition_node]:
            if distance_list[neighbor] > distance_list[current_partition_node]:
                partition_count += 1
                bfs_enqueue(neighbor)

player_names = ["Fennec", "Snuke"]
winning_player = player_names[partition_count >= node_count - partition_count]
print(winning_player)