input_node_count = int(input())
input_edge_count = int(input())
matrix_distance = [[10**9 for column_index in range(32)] for row_index in range(32)]
for edge_index in range(input_edge_count):
    node_from,node_to,weight_forward,weight_backward = map(int, input().split(","))
    matrix_distance[node_from][node_to] = weight_forward
    matrix_distance[node_to][node_from] = weight_backward

for intermediate_node in range(1, input_node_count + 1):
    for target_node in range(1, input_node_count + 1):
        for source_node in range(1, input_node_count + 1):
            if matrix_distance[source_node][target_node] > matrix_distance[source_node][intermediate_node] + matrix_distance[intermediate_node][target_node]:
                matrix_distance[source_node][target_node] = matrix_distance[source_node][intermediate_node] + matrix_distance[intermediate_node][target_node]

start_node,goal_node,value_total,value_penalty = map(int, input().split(","))
print(value_total - value_penalty - matrix_distance[start_node][goal_node] - matrix_distance[goal_node][start_node])