def find_representative(node: int) -> int:
    if parent_list[node] == node:
        return node
    return find_representative(parent_list[node])

def union_sets(node_a: int, node_b: int) -> None:
    representative_a = find_representative(node_a)
    representative_b = find_representative(node_b)
    if depth_list[representative_a] > depth_list[representative_b]:
        parent_list[representative_b] = representative_a
        depth_list[representative_a] = max(depth_list[representative_a], depth_list[representative_b] + 1)
    else:
        parent_list[representative_a] = representative_b
        depth_list[representative_b] = max(depth_list[representative_b], depth_list[representative_a] + 1)

def are_in_same_set(node_a: int, node_b: int) -> bool:
    return find_representative(node_a) == find_representative(node_b)

number_of_nodes, number_of_edges = map(int, input().split())

edge_list = []
for _ in range(number_of_edges):
    endpoint_1, endpoint_2 = map(int, input().split())
    edge_list.append((endpoint_1 - 1, endpoint_2 - 1))

count_disconnecting_edges = 0

for excluded_edge_index in range(number_of_edges):

    is_connected = True

    parent_list = [node_index for node_index in range(number_of_nodes)]
    depth_list = [0 for _ in range(number_of_nodes)]

    for edge_index in range(number_of_edges):
        if edge_index != excluded_edge_index:
            node_u, node_v = edge_list[edge_index]
            union_sets(node_u, node_v)

    for node_index in range(number_of_nodes - 1):
        if find_representative(node_index) != find_representative(node_index + 1):
            is_connected = False

    if not is_connected:
        count_disconnecting_edges += 1

print(count_disconnecting_edges)