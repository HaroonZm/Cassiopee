import heapq

CONST_INF = 10 ** 20

input_nodes, input_edges, input_zones, input_safe = map(int, input().split())
input_price_normal, input_price_zone = map(int, input().split())

zone_distance = [CONST_INF] * input_nodes
priority_queue_zones = []
for zone_index in range(input_zones):
    node_zone = int(input()) - 1
    zone_distance[node_zone] = 0
    heapq.heappush(priority_queue_zones, (0, node_zone))

adjacency_list = [[] for _ in range(input_nodes)]
for edge_index in range(input_edges):
    edge_start, edge_end = map(int, input().split())
    edge_start -= 1
    edge_end -= 1
    adjacency_list[edge_start].append(edge_end)
    adjacency_list[edge_end].append(edge_start)

while priority_queue_zones:
    current_distance, current_node = heapq.heappop(priority_queue_zones)
    for neighbor_node in adjacency_list[current_node]:
        if zone_distance[neighbor_node] > current_distance + 1:
            zone_distance[neighbor_node] = current_distance + 1
            heapq.heappush(priority_queue_zones, (current_distance + 1, neighbor_node))

path_cost = [CONST_INF] * input_nodes
path_cost[0] = 0
priority_queue_cost = []
heapq.heappush(priority_queue_cost, (0, 0))

while priority_queue_cost:
    current_cost, current_node = heapq.heappop(priority_queue_cost)
    for neighbor_node in adjacency_list[current_node]:
        if neighbor_node == input_nodes - 1:
            if path_cost[neighbor_node] > current_cost:
                path_cost[neighbor_node] = current_cost
            continue
        if zone_distance[neighbor_node] == 0:
            continue
        if zone_distance[neighbor_node] <= input_safe:
            move_cost = input_price_zone
        else:
            move_cost = input_price_normal
        if path_cost[neighbor_node] > current_cost + move_cost:
            path_cost[neighbor_node] = current_cost + move_cost
            heapq.heappush(priority_queue_cost, (current_cost + move_cost, neighbor_node))

print(path_cost[input_nodes - 1])