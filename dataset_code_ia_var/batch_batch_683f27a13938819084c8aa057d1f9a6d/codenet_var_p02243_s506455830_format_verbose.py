from heapq import heappush, heappop

INFINITE_DISTANCE = float('inf')

number_of_nodes = int(input())
adjacency_list = []

for node_index in range(number_of_nodes):
    input_line = list(map(int, input().split()[2:]))
    neighbors = list(zip(input_line[0::2], input_line[1::2]))
    adjacency_list.append(neighbors)

shortest_distances_from_source = [INFINITE_DISTANCE] * number_of_nodes
shortest_distances_from_source[0] = 0

priority_queue = [(0, 0)]  # Each element is a (distance, node_index) tuple

while priority_queue:
    _, current_node = heappop(priority_queue)
    for neighbor_index, edge_cost in adjacency_list[current_node]:
        updated_distance = shortest_distances_from_source[current_node] + edge_cost
        if updated_distance < shortest_distances_from_source[neighbor_index]:
            shortest_distances_from_source[neighbor_index] = updated_distance
            heappush(priority_queue, (updated_distance, neighbor_index))

for node_index in range(number_of_nodes):
    print(node_index, shortest_distances_from_source[node_index])