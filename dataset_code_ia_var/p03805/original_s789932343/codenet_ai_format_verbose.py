import itertools

number_of_nodes, number_of_edges = map(int, input().split())

edge_list = []

for _ in range(number_of_edges):
    node_start, node_end = map(int, input().split())
    edge_list.append([node_start, node_end])
    edge_list.append([node_end, node_start])

number_of_valid_permutations = 0

for node_permutation in itertools.permutations(list(range(1, number_of_nodes + 1))):
    
    is_valid_path = True

    if node_permutation[0] == 1:
        
        for node_index in range(number_of_nodes - 1):
            current_edge = [node_permutation[node_index], node_permutation[node_index + 1]]
            
            if current_edge not in edge_list:
                is_valid_path = False
        
        if is_valid_path:
            number_of_valid_permutations += 1

print(number_of_valid_permutations)