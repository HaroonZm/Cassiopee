import sys
from heapq import heappush, heappop

CONST_MAX_MONEY = 2500
CONST_INF = float('inf')

input_node_count, input_edge_count, input_start_money = map(int, input().split())
input_start_money = min(input_start_money, CONST_MAX_MONEY)

adjacency_list = [[] for _ in range(input_node_count)]
for _ in range(input_edge_count):
    edge_from, edge_to, edge_fare, edge_time = map(int, input().split())
    edge_from -= 1
    edge_to -= 1
    adjacency_list[edge_from].append((edge_to, edge_fare, edge_time))
    adjacency_list[edge_to].append((edge_from, edge_fare, edge_time))

coin_nodes = [tuple(map(int, input().split())) for _ in range(input_node_count)]

dist_matrix = [[CONST_INF] * (CONST_MAX_MONEY + 10) for _ in range(input_node_count)]
dist_matrix[0][input_start_money] = 0

priority_queue = [(0, 0, input_start_money)]
while priority_queue:
    current_dist, current_node, current_money = heappop(priority_queue)
    if dist_matrix[current_node][current_money] < current_dist:
        continue
    for neighbor_node, neighbor_fare, neighbor_time in adjacency_list[current_node]:
        updated_money = current_money - neighbor_fare
        if updated_money < 0:
            continue
        if dist_matrix[neighbor_node][updated_money] > dist_matrix[current_node][current_money] + neighbor_time:
            dist_matrix[neighbor_node][updated_money] = dist_matrix[current_node][current_money] + neighbor_time
            heappush(priority_queue, (dist_matrix[neighbor_node][updated_money], neighbor_node, updated_money))
    increased_money = min(current_money + coin_nodes[current_node][0], CONST_MAX_MONEY)
    if dist_matrix[current_node][increased_money] > dist_matrix[current_node][current_money] + coin_nodes[current_node][1]:
        dist_matrix[current_node][increased_money] = dist_matrix[current_node][current_money] + coin_nodes[current_node][1]
        heappush(priority_queue, (dist_matrix[current_node][increased_money], current_node, increased_money))

for destination_index in range(1, input_node_count):
    print(min(dist_matrix[destination_index]))