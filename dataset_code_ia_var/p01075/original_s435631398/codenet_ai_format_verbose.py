from collections import deque

number_of_nodes, number_of_edges = map(int, input().split())

adjacency_list = [[] for _ in range(number_of_nodes)]

for _ in range(number_of_edges):
    start_node, end_node, edge_time = map(int, input().split())
    adjacency_list[start_node - 1].append((end_node - 1, edge_time))

bfs_queue = deque()
bfs_queue.append((0, 0))

maximum_reachable_time = -1

while bfs_queue:

    current_node, current_time = bfs_queue.popleft()

    if current_node == number_of_nodes - 1:
        maximum_reachable_time = max(maximum_reachable_time, current_time)

    for index in range(len(adjacency_list[current_node]) - 1, -1, -1):

        neighbor_node, neighbor_time = adjacency_list[current_node][index]

        if neighbor_time >= current_time:
            bfs_queue.append((neighbor_node, neighbor_time))
            adjacency_list[current_node].pop(index)

print(maximum_reachable_time)