import sys
sys.setrecursionlimit(10**7)

def main():
    node_count, edge_count = map(int, input().split())
    if node_count == 1:
        exit()

    adjacency_dict = {}
    for edge_index in range(edge_count):
        node_u, node_v = map(int, input().split())
        adjacency_dict.setdefault(node_u, []).append(node_v)
        adjacency_dict.setdefault(node_v, []).append(node_u)

    node_order = [0] * node_count
    order_counter = 0
    articulation_points = []

    def depth_first_search(current_node, parent_node):
        nonlocal order_counter
        child_count = 0
        is_articulation = False
        order_counter += 1
        lowest_order = node_order[current_node - 1] = order_counter
        for neighbor_node in adjacency_dict[current_node]:
            if neighbor_node == parent_node:
                continue
            if node_order[neighbor_node - 1] == 0:
                subtree_lowest_order = depth_first_search(neighbor_node, current_node)
                if subtree_lowest_order >= node_order[current_node - 1]:
                    is_articulation = True
                lowest_order = min(lowest_order, subtree_lowest_order)
                child_count += 1
            else:
                lowest_order = min(lowest_order, node_order[neighbor_node - 1])
        if (parent_node == -1 and child_count > 1) or (parent_node != -1 and is_articulation):
            articulation_points.append(current_node)
        return lowest_order

    depth_first_search(1, -1)
    for articulation_node in sorted(articulation_points):
        print(articulation_node)

if __name__ == '__main__':
    main()