from collections import deque
from heapq import heappush, heappop

node_count, edge_count, zombie_count, danger_distance = map(int, input().split())
cost_safe, cost_danger = map(int, input().split())
zombie_nodes = [int(input()) - 1 for _ in range(zombie_count)]
adjacency_list = [[] for _ in range(node_count)]

for _ in range(edge_count):
    node_u, node_v = map(int, input().split())
    node_u -= 1
    node_v -= 1
    adjacency_list[node_u].append(node_v)
    adjacency_list[node_v].append(node_u)

danger_levels = [node_count] * node_count
queue_bfs = deque()
for zombie in zombie_nodes:
    danger_levels[zombie] = 0
    queue_bfs.append(zombie)

while queue_bfs:
    current_node = queue_bfs.popleft()
    current_danger = danger_levels[current_node]
    for neighbor in adjacency_list[current_node]:
        if danger_levels[neighbor] != node_count:
            continue
        danger_levels[neighbor] = current_danger + 1
        queue_bfs.append(neighbor)

distance_inf = 10 ** 18
min_costs = [distance_inf] * node_count
min_costs[0] = 0
priority_queue = [(0, 0)]

while priority_queue:
    curr_cost, curr_node = heappop(priority_queue)
    if min_costs[curr_node] < curr_cost:
        continue
    for neighbor in adjacency_list[curr_node]:
        if danger_levels[neighbor] == 0:
            continue
        transit_cost = cost_danger if danger_levels[neighbor] <= danger_distance else cost_safe
        next_cost = curr_cost + transit_cost
        if next_cost < min_costs[neighbor]:
            min_costs[neighbor] = next_cost
            heappush(priority_queue, (next_cost, neighbor))

final_dest = node_count - 1
final_transit_cost = cost_danger if danger_levels[final_dest] <= danger_distance else cost_safe
print(min_costs[final_dest] - final_transit_cost)