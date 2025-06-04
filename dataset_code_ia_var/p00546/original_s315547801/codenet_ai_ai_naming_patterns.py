from heapq import heappush as hp_push, heappop as hp_pop

CONST_INF = 10 ** 20

node_count, edge_count, zombie_count, safe_radius = map(int, input().split())
regular_cost, danger_cost = map(int, input().split())
distance_to_zombie = [CONST_INF] * node_count
zombie_queue = []
for _ in range(zombie_count):
    zombie_node_index = int(input()) - 1
    distance_to_zombie[zombie_node_index] = 0
    hp_push(zombie_queue, (0, zombie_node_index))

adjacency_list = [[] for _ in range(node_count)]
for _ in range(edge_count):
    edge_start, edge_end = map(int, input().split())
    edge_start -= 1
    edge_end -= 1
    adjacency_list[edge_start].append(edge_end)
    adjacency_list[edge_end].append(edge_start)

while zombie_queue:
    current_distance, current_node = hp_pop(zombie_queue)
    for neighbor in adjacency_list[current_node]:
        if distance_to_zombie[neighbor] > current_distance + 1:
            distance_to_zombie[neighbor] = current_distance + 1
            hp_push(zombie_queue, (current_distance + 1, neighbor))

node_cost = [CONST_INF] * node_count
node_cost[0] = 0
cost_queue = []
hp_push(cost_queue, (0, 0))

while cost_queue:
    accumulated_cost, visited_node = hp_pop(cost_queue)
    for adjacent_node in adjacency_list[visited_node]:
        if adjacent_node == node_count - 1:
            print(accumulated_cost)
            cost_queue = []
            break
        if distance_to_zombie[adjacent_node] == 0:
            continue
        if distance_to_zombie[adjacent_node] <= safe_radius:
            move_cost = danger_cost
        else:
            move_cost = regular_cost
        if node_cost[adjacent_node] > accumulated_cost + move_cost:
            node_cost[adjacent_node] = accumulated_cost + move_cost
            hp_push(cost_queue, (accumulated_cost + move_cost, adjacent_node))