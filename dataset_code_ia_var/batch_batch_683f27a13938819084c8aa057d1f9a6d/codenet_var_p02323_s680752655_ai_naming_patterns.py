num_vertices, num_edges = map(int, input().split())
value_infinity = float('inf')
adjacency_matrix = [[value_infinity for vertex_col in range(num_vertices)] for vertex_row in range(num_vertices)]

for edge_index in range(num_edges):
    edge_source, edge_target, edge_weight = map(int, input().split())
    adjacency_matrix[edge_source][edge_target] = edge_weight

dp_table = [[value_infinity for dp_vertex in range(num_vertices)] for dp_subset in range(1 << num_vertices)]
dp_table[0][0] = 0

for subset_state in range(1, 1 << num_vertices):
    for current_vertex in range(num_vertices):
        if subset_state & (1 << current_vertex) == 0:
            continue
        prev_subset_state = subset_state - (1 << current_vertex)
        for prev_vertex in range(num_vertices):
            dp_table[subset_state][current_vertex] = min(
                dp_table[subset_state][current_vertex],
                dp_table[prev_subset_state][prev_vertex] + adjacency_matrix[prev_vertex][current_vertex]
            )

final_result = dp_table[(1 << num_vertices) - 1][0]
if final_result == value_infinity:
    print(-1)
else:
    print(final_result)