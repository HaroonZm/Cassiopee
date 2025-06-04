import heapq

CONSTANT_INFINITY = 0x7fffffff

def compute_shortest_path(total_vertices, adjacency_list, node_start, node_goal):
    distance_list = [CONSTANT_INFINITY] * total_vertices
    processing_queue = []
    distance_list[node_start] = 0
    heapq.heappush(processing_queue, (0, node_start))
    while processing_queue:
        current_cost, current_node = heapq.heappop(processing_queue)
        if current_node == node_goal:
            break
        if distance_list[current_node] < current_cost:
            continue
        for neighbor, edge_cost in adjacency_list[current_node]:
            new_cost = current_cost + edge_cost
            if distance_list[neighbor] > new_cost:
                distance_list[neighbor] = new_cost
                heapq.heappush(processing_queue, (new_cost, neighbor))
    return distance_list[node_goal]

total_nodes = int(input()) + 1
adjacency_list = [[] for _ in range(total_nodes)]
for _ in range(int(input())):
    node_a, node_b, cost_ab, cost_ba = map(int, input().split(','))
    adjacency_list[node_a].append((node_b, cost_ab))
    adjacency_list[node_b].append((node_a, cost_ba))
start_node, goal_node, available_value, penalty_value = map(int, input().split(','))
if start_node == goal_node:
    print(available_value - penalty_value)
else:
    forward_cost = compute_shortest_path(total_nodes, adjacency_list, start_node, goal_node)
    backward_cost = compute_shortest_path(total_nodes, adjacency_list, goal_node, start_node)
    print(available_value - penalty_value - forward_cost - backward_cost)