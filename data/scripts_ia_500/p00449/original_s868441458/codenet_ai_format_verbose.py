from heapq import heappush, heappop, heapify

def dijkstra_shortest_path(start_node, target_node, adjacency_list):
    
    priority_queue = list(adjacency_list[start_node])
    heapify(priority_queue)
    
    visited_nodes = set()
    
    while priority_queue:
        
        current_fare, current_node = heappop(priority_queue)
        
        if current_node == target_node:
            return current_fare
        
        if current_node in visited_nodes:
            continue
        
        visited_nodes.add(current_node)
        
        for edge_fare, adjacent_node in adjacency_list[current_node]:
            if adjacent_node not in visited_nodes:
                heappush(priority_queue, (current_fare + edge_fare, adjacent_node))
    
    return -1


while True:
    
    number_of_nodes, number_of_edges = map(int, input().split())
    
    if number_of_nodes == 0:
        break
    
    adjacency_list = [set() for _ in range(number_of_nodes)]
    
    for _ in range(number_of_edges):
        
        input_values = map(int, input().split())
        command_type = next(input_values)
        
        if command_type == 1:
            node_start, node_end, fare_cost = input_values
            node_start -= 1
            node_end -= 1
            
            adjacency_list[node_start].add((fare_cost, node_end))
            adjacency_list[node_end].add((fare_cost, node_start))
        
        else:
            query_start_node, query_end_node = input_values
            query_start_node -= 1
            query_end_node -= 1
            
            shortest_path_fare = dijkstra_shortest_path(query_start_node, query_end_node, adjacency_list)
            print(shortest_path_fare)