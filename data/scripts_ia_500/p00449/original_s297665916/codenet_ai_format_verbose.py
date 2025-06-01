from heapq import heappop, heappush
import sys

read_input_line = sys.stdin.readline

def find_shortest_path(number_of_nodes, adjacency_list, start_node, goal_node):
    
    max_distance = 10_000_000
    distances = [max_distance] * (number_of_nodes + 1)
    distances[start_node] = 0
    
    priority_queue = [(0, start_node)]
    
    while priority_queue:
        
        current_distance, current_node = heappop(priority_queue)
        
        if current_node == goal_node:
            return current_distance
        
        for edge_weight, neighbor_node in adjacency_list[current_node]:
            new_distance = current_distance + edge_weight
            
            if new_distance < distances[neighbor_node]:
                distances[neighbor_node] = new_distance
                heappush(priority_queue, (new_distance, neighbor_node))
    
    return -1

def process_queries(number_of_nodes, number_of_edges):
    
    adjacency_list = [[] for _ in range(number_of_nodes + 1)]
    
    for _ in range(number_of_edges):
        
        input_line = read_input_line()
        
        if input_line[0] == '0':
            _, start_str, goal_str = input_line.split()
            start = int(start_str)
            goal = int(goal_str)
            shortest_path_distance = find_shortest_path(number_of_nodes, adjacency_list, start, goal)
            print(shortest_path_distance)
        else:
            parts = list(map(int, input_line[2:].split()))
            node_a = parts[0]
            node_b = parts[1]
            edge_weight = parts[2]
            
            adjacency_list[node_a].append([edge_weight, node_b])
            adjacency_list[node_b].append([edge_weight, node_a])

for input_line in iter(read_input_line, '0 0\n'):
    number_of_nodes, number_of_edges = map(int, input_line.split())
    process_queries(number_of_nodes, number_of_edges)