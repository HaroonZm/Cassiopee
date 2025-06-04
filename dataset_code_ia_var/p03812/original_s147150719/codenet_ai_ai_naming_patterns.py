node_count = int(input())
node_values = list(map(int, input().split()))
adjacency_list = [[] for _ in range(node_count)]
for edge_start, edge_end in [map(int, input().split()) for _ in range(node_count - 1)]:
    adjacency_list[edge_start - 1].append(edge_end - 1)
    adjacency_list[edge_end - 1].append(edge_start - 1)

def is_special_node(parent_index, current_index):
    return sum(
        (
            parent_index != neighbor_index
            and node_values[current_index] > node_values[neighbor_index]
            and not is_special_node(current_index, neighbor_index)
        )
        for neighbor_index in adjacency_list[current_index]
    )

special_nodes = [index + 1 for index in range(node_count) if is_special_node(node_count, index)]
print(*special_nodes)