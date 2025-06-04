import sys

INFINITE_DISTANCE = float('inf')

def floyd_warshall(number_of_vertices, adjacency_matrix):
    
    shortest_distances = [[INFINITE_DISTANCE] * number_of_vertices for _ in range(number_of_vertices)]
    
    for source_vertex in range(number_of_vertices):
        for target_vertex in range(number_of_vertices):
            shortest_distances[source_vertex][target_vertex] = adjacency_matrix[source_vertex][target_vertex]
    
    for intermediate_vertex in range(number_of_vertices):
        for source_vertex in range(number_of_vertices):
            for target_vertex in range(number_of_vertices):
                possible_shorter_distance = shortest_distances[source_vertex][intermediate_vertex] + shortest_distances[intermediate_vertex][target_vertex]
                if possible_shorter_distance < shortest_distances[source_vertex][target_vertex]:
                    shortest_distances[source_vertex][target_vertex] = possible_shorter_distance
    
    for vertex in range(number_of_vertices):
        if shortest_distances[vertex][vertex] < 0:
            return None
    
    return shortest_distances

def print_shortest_distances(shortest_distances_matrix, unreachable_value):
    number_of_vertices = len(shortest_distances_matrix)
    for source_vertex in range(number_of_vertices):
        row_output = []
        for target_vertex in range(number_of_vertices):
            if shortest_distances_matrix[source_vertex][target_vertex] < unreachable_value:
                row_output.append(str(shortest_distances_matrix[source_vertex][target_vertex]))
            else:
                row_output.append('INF')
        print(' '.join(row_output))

def main():
    
    total_vertices, total_edges = map(int, sys.stdin.readline().split())
    
    adjacency_matrix = [
        [INFINITE_DISTANCE] * total_vertices 
        for _ in range(total_vertices)
    ]
    for vertex in range(total_vertices):
        adjacency_matrix[vertex][vertex] = 0
    
    for _ in range(total_edges):
        start_vertex, end_vertex, edge_weight = map(int, sys.stdin.readline().split())
        adjacency_matrix[start_vertex][end_vertex] = edge_weight

    result_matrix = floyd_warshall(total_vertices, adjacency_matrix)
    
    if result_matrix is None:
        print('NEGATIVE CYCLE')
    else:
        print_shortest_distances(result_matrix, INFINITE_DISTANCE)

if __name__ == '__main__':
    main()