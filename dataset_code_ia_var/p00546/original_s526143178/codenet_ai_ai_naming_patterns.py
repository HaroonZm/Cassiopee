from collections import deque
from heapq import heappop, heappush

CONST_INF = float("inf")
heap_zone = []
heap_dijkstra = []

num_nodes, num_edges, num_zones, max_distance = map(int, input().split())
cost_regular, cost_zone = map(int, input().split())

zone_nodes = [0] * num_zones
zone_distance = [CONST_INF] * num_nodes

for idx_zone in range(num_zones):
    zone_node = int(input()) - 1
    zone_nodes[idx_zone] = zone_node
    zone_distance[zone_node] = 0
    heappush(heap_zone, (0, zone_node))

edge_list_a = [0] * num_edges
edge_list_b = [0] * num_edges
adj_temp = [[] for _ in range(num_edges)]

for idx_edge in range(num_edges):
    node_a, node_b = map(int, input().split())
    node_a -= 1
    node_b -= 1
    adj_temp[node_a].append(node_b)
    adj_temp[node_b].append(node_a)
    edge_list_a[idx_edge] = node_a
    edge_list_b[idx_edge] = node_b

node_costs = [cost_regular] * num_nodes

while heap_zone:
    dist_current, node_current = heappop(heap_zone)
    for neighbor in adj_temp[node_current]:
        if zone_distance[neighbor] > dist_current + 1:
            zone_distance[neighbor] = dist_current + 1
            heappush(heap_zone, (dist_current + 1, neighbor))

for idx_node in range(num_nodes):
    if zone_distance[idx_node] <= max_distance:
        node_costs[idx_node] = cost_zone

adj_final = [[] for _ in range(num_nodes)]
for idx_edge in range(num_edges):
    node_u = edge_list_a[idx_edge]
    node_v = edge_list_b[idx_edge]
    if (node_u not in zone_nodes) and (node_v not in zone_nodes):
        adj_final[node_u].append((node_v, node_costs[node_v]))
        adj_final[node_v].append((node_u, node_costs[node_u]))

heap_path = []
start_node = 0
heappush(heap_path, (0, start_node))

shortest_distance = [CONST_INF] * num_nodes
shortest_distance[start_node] = 0

while heap_path:
    dist_travelled, node_at = heappop(heap_path)
    for node_next, cost_next in adj_final[node_at]:
        if shortest_distance[node_next] > shortest_distance[node_at] + cost_next:
            shortest_distance[node_next] = shortest_distance[node_at] + cost_next
            heappush(heap_path, (shortest_distance[node_next], node_next))

print(shortest_distance[num_nodes - 1] - node_costs[num_nodes - 1])