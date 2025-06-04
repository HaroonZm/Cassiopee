import sys
from collections import deque
import heapq

def read_input():
    return map(int, sys.stdin.readline().split())

def read_single_int():
    return int(sys.stdin.readline())

node_count, edge_count, zombie_count, danger_radius = read_input()
normal_cost, danger_cost = read_input()

zombie_city_list = [read_single_int() for _ in range(zombie_count)]

adjacency_list = [[] for _ in range(node_count + 1)]
for _ in range(edge_count):
    city_a, city_b = read_input()
    adjacency_list[city_a].append(city_b)
    adjacency_list[city_b].append(city_a)

danger_city_set = set()
for zombie_city in zombie_city_list:
    visit_queue = deque([zombie_city])
    step_counter = 0
    visited_flags = [False] * (node_count + 1)

    while visit_queue and step_counter <= danger_radius:
        current_level_size = len(visit_queue)
        next_queue = deque()
        for _ in range(current_level_size):
            current_city = visit_queue.popleft()
            visited_flags[current_city] = True
            for neighbor_city in adjacency_list[current_city]:
                if visited_flags[neighbor_city]: continue
                if neighbor_city in visit_queue or neighbor_city in next_queue: continue
                if neighbor_city in zombie_city_list: continue
                next_queue.append(neighbor_city)
        visit_queue = next_queue
        step_counter += 1

    for city_id in range(1, node_count + 1):
        if visited_flags[city_id] and city_id not in zombie_city_list:
            danger_city_set.add(city_id)

reweighted_graph = [[] for _ in range(node_count + 1)]
for city_id in range(1, node_count + 1):
    for adjacent in adjacency_list[city_id]:
        if adjacent in zombie_city_list:
            continue
        if adjacent in danger_city_set:
            reweighted_graph[city_id].append((adjacent, danger_cost))
        else:
            reweighted_graph[city_id].append((adjacent, normal_cost))

priority_queue = [(0, 1)]
distance_array = [float('inf')] * (node_count + 1)
finalized_flags = [False] * (node_count + 1)
distance_array[1] = 0

while priority_queue:
    current_distance, current_city = heapq.heappop(priority_queue)
    if current_city == node_count:
        break
    if finalized_flags[current_city]:
        continue
    finalized_flags[current_city] = True
    for neighbor_city, road_cost in reweighted_graph[current_city]:
        if finalized_flags[neighbor_city]:
            continue
        if current_distance + road_cost < distance_array[neighbor_city]:
            distance_array[neighbor_city] = current_distance + road_cost
            heapq.heappush(priority_queue, (distance_array[neighbor_city], neighbor_city))

end_city_distance = distance_array[node_count]
if node_count in danger_city_set:
    print(end_city_distance - danger_cost)
else:
    print(end_city_distance - normal_cost)