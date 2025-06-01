from heapq import heappop, heappush
import sys

readline = sys.stdin.readline

def shortest_path(number_of_nodes, adjacency_list, start_node, goal_node):
    
    max_distance = int(1e7)
    
    distances = [max_distance] * (number_of_nodes + 1)
    distances[start_node] = 0
    
    priority_queue = [(0, start_node)]
    
    while priority_queue:
        
        current_cost, current_node = heappop(priority_queue)
        
        if current_node == goal_node:
            return current_cost
        
        for edge_cost, neighbor_node in adjacency_list[current_node]:
            
            tentative_cost = current_cost + edge_cost
            
            if tentative_cost < distances[neighbor_node]:
                
                distances[neighbor_node] = tentative_cost
                heappush(priority_queue, (tentative_cost, neighbor_node))
    
    return -1


def process_commands(number_of_nodes, number_of_commands):
    
    adjacency_list = [[] for _ in range(number_of_nodes + 1)]
    
    for _ in range(number_of_commands):
        
        command_line = readline()
        
        if command_line[0] == '0':
            
            _, start_node, goal_node = command_line[2:].split()
            start_node = int(start_node)
            goal_node = int(goal_node)
            
            result = shortest_path(number_of_nodes, adjacency_list, start_node, goal_node)
            print(result)
        
        else:
            
            command_values = list(map(int, command_line[2:].split()))
            node1, node2, weight = command_values
            
            adjacency_list[node1].append((weight, node2))
            adjacency_list[node2].append((weight, node1))


for input_line in iter(readline, '0 0\n'):
    
    node_count, command_count = map(int, input_line.split())
    process_commands(node_count, command_count)