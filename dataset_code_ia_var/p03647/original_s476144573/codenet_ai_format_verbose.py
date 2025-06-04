user_input_line = input().split()

number_of_nodes = int(user_input_line[0])
number_of_edges = int(user_input_line[1])

adjacency_list = [ [] for _ in range(number_of_nodes) ]

for _ in range(number_of_edges):
    edge_input_line = input().split()
    start_node = int(edge_input_line[0]) - 1
    end_node = int(edge_input_line[1]) - 1
    adjacency_list[start_node].append(end_node)

def depth_first_search(current_node_index, depth_so_far):
    if current_node_index == number_of_nodes - 1:
        if depth_so_far == 2:
            return True
        else:
            return False

    for neighbor_index in adjacency_list[current_node_index]:
        if depth_first_search(neighbor_index, depth_so_far + 1):
            return True

    return False

if depth_first_search(0, 0):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")