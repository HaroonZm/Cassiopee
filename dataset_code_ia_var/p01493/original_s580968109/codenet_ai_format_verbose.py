from collections import deque
import sys

sys.setrecursionlimit(10**6)

read_line_from_stdin = sys.stdin.readline
write_output_to_stdout = sys.stdout.write

def solve():
    number_of_nodes = int(read_line_from_stdin())
    adjacency_list_of_graph = [[] for _ in range(number_of_nodes)]
    
    for current_node_index in range(number_of_nodes):
        line_as_chars = read_line_from_stdin()
        for target_node_index in range(number_of_nodes):
            if line_as_chars[target_node_index] == "Y":
                adjacency_list_of_graph[current_node_index].append(target_node_index)
    
    total_number_of_edges = 0
    component_size_parity_counts = [0, 0]  # [even-sized, odd-sized]
    visited_nodes = [False] * number_of_nodes
    
    for node_index in range(number_of_nodes):
        total_number_of_edges += len(adjacency_list_of_graph[node_index])
        if visited_nodes[node_index]:
            continue
        visited_nodes[node_index] = True
        queue_of_nodes = deque([node_index])
        current_component_size = 0
        while queue_of_nodes:
            current_node = queue_of_nodes.popleft()
            current_component_size += 1
            for neighbor_node in adjacency_list_of_graph[current_node]:
                if visited_nodes[neighbor_node]:
                    continue
                visited_nodes[neighbor_node] = True
                queue_of_nodes.append(neighbor_node)
        component_size_parity_counts[current_component_size % 2] += 1

    total_possible_edges = number_of_nodes * (number_of_nodes - 1) // 2
    number_of_edges_in_graph = total_number_of_edges // 2
    parity_of_missing_edges = (total_possible_edges - number_of_edges_in_graph) & 1
    
    memoization_for_dfs = {}
    
    def compute_game_result_by_dfs(current_move_number, even_sized_components, odd_sized_components):
        current_state_key = (even_sized_components, odd_sized_components)
        if current_state_key in memoization_for_dfs:
            return memoization_for_dfs[current_state_key]
        if even_sized_components + odd_sized_components == 2:
            is_odd_odd = (odd_sized_components == 2)
            outcome_based_on_r0 = is_odd_odd ^ parity_of_missing_edges
            memoization_for_dfs[current_state_key] = final_result = outcome_based_on_r0 ^ (current_move_number & 1)
            return final_result
        game_result = 0
        if even_sized_components > 1 or (even_sized_components and odd_sized_components):
            if compute_game_result_by_dfs(current_move_number + 1, even_sized_components - 1, odd_sized_components) == 0:
                game_result = 1
        if odd_sized_components > 1:
            if compute_game_result_by_dfs(current_move_number + 1, even_sized_components + 1, odd_sized_components - 2) == 0:
                game_result = 1
        memoization_for_dfs[current_state_key] = game_result
        return game_result

    first_player_wins = compute_game_result_by_dfs(0, component_size_parity_counts[0], component_size_parity_counts[1])
    if first_player_wins:
        write_output_to_stdout("Taro\n")
    else:
        write_output_to_stdout("Hanako\n")

solve()