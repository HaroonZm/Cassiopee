import sys

def build_adjacency_list(edge_list_input):
    for u_idx, v_idx in edge_list_input:
        adjacency_list_init[u_idx].append(v_idx)
    return adjacency_list_init

def perform_cycle_detection_dfs(node_idx, node_visited_flags, active_recursion_flags):
    if not node_visited_flags[node_idx]:
        node_visited_flags[node_idx] = True
        active_recursion_flags[node_idx] = True

        for neighbor_idx in adjacency_list[node_idx]:
            if not node_visited_flags[neighbor_idx] and perform_cycle_detection_dfs(neighbor_idx, node_visited_flags, active_recursion_flags):
                return True
            elif active_recursion_flags[neighbor_idx]:
                return True

    active_recursion_flags[node_idx] = False
    return False

def detect_directed_cycle_top_level():
    node_visited_flags, active_recursion_flags = ([False] * vertex_count for _ in range(2))
    for vertex_idx in range(vertex_count):
        if perform_cycle_detection_dfs(vertex_idx, node_visited_flags, active_recursion_flags):
            return True
    return False

if __name__ == '__main__':
    stdin_input_lines = sys.stdin.readlines()
    vertex_count, edge_count = map(int, stdin_input_lines[0].split())
    input_edge_list = map(lambda edge_line: list(map(int, edge_line.split())), stdin_input_lines[1:])

    adjacency_list_init = tuple([] for _ in range(vertex_count))
    adjacency_list = build_adjacency_list(input_edge_list)

    print(int(detect_directed_cycle_top_level()))