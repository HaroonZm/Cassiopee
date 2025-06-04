number_of_nodes, number_of_colors = map(int, input().split())

adjacency_list = [[] for _ in range(number_of_nodes)]

for _ in range(number_of_nodes - 1):
    
    node_a, node_b = map(int, input().split())
    node_a -= 1
    node_b -= 1
    
    adjacency_list[node_a].append(node_b)
    adjacency_list[node_b].append(node_a)

MODULO = 10 ** 9 + 7

from collections import deque

color_possibilities_for_nodes = [-1] * number_of_nodes
color_possibilities_for_nodes[0] = number_of_colors

nodes_to_visit = deque([0])

while nodes_to_visit:
    
    current_node = nodes_to_visit.popleft()
    
    available_colors = max(number_of_colors - 2, color_possibilities_for_nodes[current_node] - 1)
    
    for neighbor_node in adjacency_list[current_node]:
        
        if color_possibilities_for_nodes[neighbor_node] == -1:
            
            if available_colors <= 0:
                print(0)
                exit()
            
            color_possibilities_for_nodes[neighbor_node] = available_colors
            available_colors -= 1
            nodes_to_visit.append(neighbor_node)

total_number_of_colorings = 1

for color_count in color_possibilities_for_nodes:
    total_number_of_colorings *= color_count
    total_number_of_colorings %= MODULO

print(total_number_of_colorings)