import sys

sys.setrecursionlimit(1000000)

def main():

    number_of_nodes, number_of_queries = map(int, input().split())
    
    adjacency_list = [[] for _ in range(number_of_nodes)]
    
    for _ in range(number_of_nodes - 1):
        node_u_input, node_v_input, edge_weight = map(int, input().split())
        node_u = node_u_input - 1
        node_v = node_v_input - 1
        adjacency_list[node_u].append((node_v, edge_weight))
        adjacency_list[node_v].append((node_u, edge_weight))

    node_depth = [None] * number_of_nodes
    node_distance_from_root = [None] * number_of_nodes
    binary_lifting_parent = [[None] * 20 for _ in range(number_of_nodes)]

    stack_for_dfs = [(0, 0, 0)]  # (current_node, depth, distance)
    while stack_for_dfs:
        current_node, current_depth, current_distance = stack_for_dfs.pop()
        node_depth[current_node] = current_depth
        node_distance_from_root[current_node] = current_distance

        for neighbor, neighbor_edge_weight in adjacency_list[current_node]:
            if node_depth[neighbor] is None:
                binary_lifting_parent[neighbor][0] = current_node
                stack_for_dfs.append((neighbor, current_depth + 1, current_distance + neighbor_edge_weight))

    for jump_length_exponent in range(1, 20):
        for node_index in range(1, number_of_nodes):
            if node_depth[node_index] >= 2 ** jump_length_exponent:
                binary_lifting_parent[node_index][jump_length_exponent] = binary_lifting_parent[
                    binary_lifting_parent[node_index][jump_length_exponent - 1]
                ][jump_length_exponent - 1]

    def climb_to_target_depth(start_node, climb_steps):
        if climb_steps == 0:
            return start_node
        accumulated_steps = 1
        for exponent in range(20):
            if accumulated_steps > climb_steps:
                return climb_to_target_depth(binary_lifting_parent[start_node][exponent - 1], climb_steps - accumulated_steps // 2)
            accumulated_steps *= 2

    def recursive_lca(node_x, node_y):
        if node_x == node_y:
            return node_x
        for exponent in range(1, 20):
            if binary_lifting_parent[node_x][exponent] == binary_lifting_parent[node_y][exponent]:
                return recursive_lca(binary_lifting_parent[node_x][exponent - 1], binary_lifting_parent[node_y][exponent - 1])

    def lowest_common_ancestor(node_x, node_y):
        depth_difference = node_depth[node_x] - node_depth[node_y]
        if depth_difference < 0:
            node_y = climb_to_target_depth(node_y, -depth_difference)
        elif depth_difference > 0:
            node_x = climb_to_target_depth(node_x, depth_difference)
        return recursive_lca(node_x, node_y)

    def find_highest_node_under_distance(current_node, target_distance):
        if current_node == 0:
            return 0
        if (node_distance_from_root[current_node] >= target_distance >=
                node_distance_from_root[binary_lifting_parent[current_node][0]]):
            return current_node
        for exponent in range(1, 20):
            if (binary_lifting_parent[current_node][exponent] is None or
                    node_distance_from_root[binary_lifting_parent[current_node][exponent]] <= target_distance):
                return find_highest_node_under_distance(binary_lifting_parent[current_node][exponent - 1], target_distance)

    def compute_max_distance_to_root(node_x, node_y, node_z, root_node):
        lca_x_root = lowest_common_ancestor(node_x, root_node)
        lca_y_root = lowest_common_ancestor(node_y, root_node)
        lca_z_root = lowest_common_ancestor(node_z, root_node)
        return max(
            node_distance_from_root[node_x] + node_distance_from_root[root_node] - 2 * node_distance_from_root[lca_x_root],
            node_distance_from_root[node_y] + node_distance_from_root[root_node] - 2 * node_distance_from_root[lca_y_root],
            node_distance_from_root[node_z] + node_distance_from_root[root_node] - 2 * node_distance_from_root[lca_z_root],
        )

    def compute_score_internal(node_x, node_y, node_z, lca_xy, lca_yz):

        dist_node_x = node_distance_from_root[node_x]
        dist_node_y = node_distance_from_root[node_y]
        dist_node_z = node_distance_from_root[node_z]
        dist_lca_xy = node_distance_from_root[lca_xy]
        dist_lca_yz = node_distance_from_root[lca_yz]

        dx = dist_node_x + dist_lca_yz - 2 * dist_lca_xy
        dy = dist_node_y - dist_lca_yz
        dz = dist_node_z - dist_lca_yz

        if dx >= dy >= dz:
            if dist_node_x >= dist_node_y:
                mid_node = find_highest_node_under_distance(node_x, dist_lca_xy + (dist_node_x - dist_node_y) / 2)
                if mid_node == 0:
                    return dist_node_x
                return min(
                    max(dist_node_x - node_distance_from_root[mid_node], dist_node_y + node_distance_from_root[mid_node] - 2 * dist_lca_xy),
                    max(dist_node_x - node_distance_from_root[binary_lifting_parent[mid_node][0]], dist_node_y + node_distance_from_root[binary_lifting_parent[mid_node][0]] - 2 * dist_lca_xy)
                )
            else:
                mid_node = find_highest_node_under_distance(lca_yz, dist_lca_xy + (dist_node_y - dist_node_x) / 2)
                if mid_node == 0:
                    return dist_node_y
                return min(
                    max(dist_node_y - node_distance_from_root[mid_node], dist_node_x + node_distance_from_root[mid_node] - 2 * dist_lca_xy),
                    max(dist_node_y - node_distance_from_root[binary_lifting_parent[mid_node][0]], dist_node_x + node_distance_from_root[binary_lifting_parent[mid_node][0]] - 2 * dist_lca_xy)
                )

        elif dx >= dz >= dy:
            if dist_node_x >= dist_node_z:
                mid_node = find_highest_node_under_distance(node_x, dist_lca_xy + (dist_node_x - dist_node_z) / 2)
                if mid_node == 0:
                    return dist_node_x
                return min(
                    max(dist_node_x - node_distance_from_root[mid_node], dist_node_z + node_distance_from_root[mid_node] - 2 * dist_lca_xy),
                    max(dist_node_x - node_distance_from_root[binary_lifting_parent[mid_node][0]], dist_node_z + node_distance_from_root[binary_lifting_parent[mid_node][0]] - 2 * dist_lca_xy)
                )
            else:
                mid_node = find_highest_node_under_distance(lca_yz, dist_lca_xy + (dist_node_z - dist_node_x) / 2)
                if mid_node == 0:
                    return dist_node_z
                return min(
                    max(dist_node_z - node_distance_from_root[mid_node], dist_node_x + node_distance_from_root[mid_node] - 2 * dist_lca_xy),
                    max(dist_node_z - node_distance_from_root[binary_lifting_parent[mid_node][0]], dist_node_x + node_distance_from_root[binary_lifting_parent[mid_node][0]] - 2 * dist_lca_xy)
                )

        elif dy >= dx >= dz:
            mid_node = find_highest_node_under_distance(node_y, dist_lca_yz + (dy - dx) / 2)
            if mid_node == 0:
                return dist_node_y
            return min(
                max(dist_node_y - node_distance_from_root[mid_node], dist_node_x + node_distance_from_root[mid_node] - 2 * dist_lca_xy),
                max(dist_node_y - node_distance_from_root[binary_lifting_parent[mid_node][0]], dist_node_x + node_distance_from_root[binary_lifting_parent[mid_node][0]] - 2 * dist_lca_xy)
            )

        elif dy >= dz >= dx:
            mid_node = find_highest_node_under_distance(node_y, dist_lca_yz + (dy - dz) / 2)
            if mid_node == 0:
                return dist_node_y
            return min(
                max(dist_node_y - node_distance_from_root[mid_node], dist_node_z + node_distance_from_root[mid_node] - 2 * dist_lca_yz),
                max(dist_node_y - node_distance_from_root[binary_lifting_parent[mid_node][0]], dist_node_z + node_distance_from_root[binary_lifting_parent[mid_node][0]] - 2 * dist_lca_yz)
            )

        elif dz >= dx >= dy:
            mid_node = find_highest_node_under_distance(node_z, dist_lca_yz + (dz - dx) / 2)
            if mid_node == 0:
                return dist_node_z
            return min(
                max(dist_node_z - node_distance_from_root[mid_node], dist_node_x + node_distance_from_root[mid_node] - 2 * dist_lca_xy),
                max(dist_node_z - node_distance_from_root[binary_lifting_parent[mid_node][0]], dist_node_x + node_distance_from_root[binary_lifting_parent[mid_node][0]] - 2 * dist_lca_xy)
            )

        elif dz >= dy >= dx:
            mid_node = find_highest_node_under_distance(node_z, dist_lca_yz + (dz - dy) / 2)
            if mid_node == 0:
                return dist_node_z
            return min(
                max(dist_node_z - node_distance_from_root[mid_node], dist_node_y + node_distance_from_root[mid_node] - 2 * dist_lca_yz),
                max(dist_node_z - node_distance_from_root[binary_lifting_parent[mid_node][0]], dist_node_y + node_distance_from_root[binary_lifting_parent[mid_node][0]] - 2 * dist_lca_yz)
            )

    def compute_score(node_input_a, node_input_b, node_input_c):

        node_a = node_input_a - 1
        node_b = node_input_b - 1
        node_c = node_input_c - 1

        lca_ab = lowest_common_ancestor(node_a, node_b)
        lca_ac = lowest_common_ancestor(node_a, node_c)
        lca_bc = lowest_common_ancestor(node_b, node_c)

        if lca_ab == lca_ac:
            return compute_score_internal(node_a, node_b, node_c, lca_ab, lca_bc)
        elif lca_ab == lca_bc:
            return compute_score_internal(node_b, node_a, node_c, lca_ab, lca_ac)
        else:
            return compute_score_internal(node_c, node_a, node_b, lca_ac, lca_ab)

    for _ in range(number_of_queries):
        query_node_a, query_node_b, query_node_c = map(int, input().split())
        print(compute_score(query_node_a, query_node_b, query_node_c))

main()