import sys
from heapq import heappush, heappop

input_line = sys.stdin.readline

def shortest_path(number_of_nodes, adjacency_list, start_node, goal_node):
    
    # Initialize distances with a large number
    distances = [float('inf')] * (number_of_nodes + 1)
    distances[start_node] = 0
    
    # Min-heap priority queue with (distance, node)
    priority_queue = [(0, start_node)]
    
    while priority_queue:
        current_cost, current_node = heappop(priority_queue)
        
        if current_node == goal_node:
            return current_cost
        
        for edge_weight, neighbor_node in adjacency_list[current_node]:
            new_cost = current_cost + edge_weight
            
            if new_cost < distances[neighbor_node]:
                distances[neighbor_node] = new_cost
                heappush(priority_queue, (new_cost, neighbor_node))
                
    return -1


def solve():
    
    for line in iter(input_line, '0 0\n'):
        number_of_nodes, number_of_edges = map(int, line.split())
        
        # Create adjacency list for the graph
        adjacency_list = [[] for _ in range(number_of_nodes + 1)]
        
        for _ in range(number_of_edges):
            edge_input = input_line()
            
            if edge_input[0] == '0':
                # Query shortest path
                start_node, goal_node = map(int, edge_input[2:].split())
                print(shortest_path(number_of_nodes, adjacency_list, start_node, goal_node))
            else:
                # Add edge to graph
                node_1, node_2, edge_weight = map(int, edge_input[2:].split())
                adjacency_list[node_1].append((edge_weight, node_2))
                adjacency_list[node_2].append((edge_weight, node_1))

                
solve()