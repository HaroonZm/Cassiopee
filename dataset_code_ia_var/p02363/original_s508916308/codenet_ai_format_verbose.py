from collections import defaultdict

INFINITY = 999999999999999999999

def floyd_warshall_algorithm(graph, number_of_vertices):
    
    shortest_path_distances = {}
    
    for source_vertex in range(number_of_vertices):
        shortest_path_distances[source_vertex] = {}
        
        for target_vertex in range(number_of_vertices):
            if source_vertex in graph and target_vertex in graph[source_vertex]:
                shortest_path_distances[source_vertex][target_vertex] = graph[source_vertex][target_vertex]
            else:
                shortest_path_distances[source_vertex][target_vertex] = INFINITY
                
        shortest_path_distances[source_vertex][source_vertex] = 0
    
    for intermediate_vertex in range(number_of_vertices):
        for start_vertex in range(number_of_vertices):
            for end_vertex in range(number_of_vertices):
                if (shortest_path_distances[start_vertex][intermediate_vertex] == INFINITY or
                    shortest_path_distances[intermediate_vertex][end_vertex] == INFINITY):
                    continue
                if (shortest_path_distances[start_vertex][end_vertex] >
                    shortest_path_distances[start_vertex][intermediate_vertex] + shortest_path_distances[intermediate_vertex][end_vertex]):
                    shortest_path_distances[start_vertex][end_vertex] = (
                        shortest_path_distances[start_vertex][intermediate_vertex] +
                        shortest_path_distances[intermediate_vertex][end_vertex]
                    )
    return shortest_path_distances

graph_representation = {}

number_of_vertices, number_of_edges = [int(value) for value in input().strip().split(' ')]

for vertex_index in range(number_of_vertices):
    graph_representation[vertex_index] = {}

for _ in range(number_of_edges):
    source_vertex, destination_vertex, edge_cost = [int(value) for value in input().strip().split(' ')]
    graph_representation[source_vertex][destination_vertex] = edge_cost

all_pairs_shortest_distances = floyd_warshall_algorithm(graph_representation, number_of_vertices)

for vertex in range(number_of_vertices):
    if all_pairs_shortest_distances[vertex][vertex] < 0:
        print("NEGATIVE CYCLE")
        exit()

for source_vertex in range(number_of_vertices):
    formatted_distances = []
    for target_vertex in range(number_of_vertices):
        distance = all_pairs_shortest_distances[source_vertex][target_vertex]
        formatted_distances.append(str(distance) if distance != INFINITY else "INF")
    print(" ".join(formatted_distances))