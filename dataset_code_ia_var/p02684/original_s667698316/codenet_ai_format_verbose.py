import sys

input_read_line = sys.stdin.readline

number_of_nodes, number_of_steps = map(int, input_read_line().split())

adjacency_list = [0] + list(map(int, input_read_line().split()))

current_position = 1

while number_of_steps:
    if number_of_steps & 1:
        current_position = adjacency_list[current_position]
    next_adjacency_list = [0] * (number_of_nodes + 1)
    for node_index in range(number_of_nodes + 1):
        next_adjacency_list[node_index] = adjacency_list[adjacency_list[node_index]]
    adjacency_list = next_adjacency_list
    number_of_steps >>= 1

print(current_position)