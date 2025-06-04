from heapq import heappush as minheap_push, heappop as minheap_pop

def run_algorithm():
    num_nodes, num_edges = map(int, input().split())
    adjacency_list = [[] for _ in range(num_nodes)]
    for _ in range(num_edges):
        edge_from, edge_to, edge_weight = map(int, input().split())
        source_idx = edge_from - 1
        target_idx = edge_to - 1
        adjacency_list[source_idx].append((target_idx, edge_weight))
        adjacency_list[target_idx].append((source_idx, edge_weight))

    initial_value = int(input())
    multiplier, increment, modulus = map(int, input().split())

    value_transition = dict()
    current_value = initial_value
    while True:
        if current_value not in value_transition:
            next_value = (current_value * multiplier + increment) % modulus
            value_transition[current_value] = next_value
            current_value = next_value
        else:
            break

    min_score_map_forward = dict()
    min_score_map_forward[(initial_value, 0)] = 0
    minheap_forward = []
    minheap_push(minheap_forward, (0, 0, initial_value))
    while minheap_forward:
        acc_score, curr_node, curr_value = minheap_pop(minheap_forward)
        next_value = value_transition[curr_value]
        for neighbor_node, neighbor_weight in adjacency_list[curr_node]:
            tentative_score = acc_score + curr_value * neighbor_weight
            state_key = (next_value, neighbor_node)
            if state_key not in min_score_map_forward or min_score_map_forward[state_key] > tentative_score:
                min_score_map_forward[state_key] = tentative_score
                minheap_push(minheap_forward, (tentative_score, neighbor_node, next_value))

    min_score_map_backward = dict()
    minheap_backward = []
    for candidate_value in range(modulus):
        backward_state = (candidate_value, num_nodes - 1)
        if backward_state in min_score_map_forward:
            min_score_map_backward[backward_state] = min_score_map_forward[backward_state]
            minheap_push(minheap_backward, (min_score_map_forward[backward_state], num_nodes - 1, candidate_value))

    while minheap_backward:
        acc_score, curr_node, curr_value = minheap_pop(minheap_backward)
        if curr_node == 0:
            print(acc_score)
            break
        next_value = value_transition[curr_value]
        for neighbor_node, neighbor_weight in adjacency_list[curr_node]:
            tentative_score = acc_score + curr_value * neighbor_weight
            state_key = (next_value, neighbor_node)
            if state_key not in min_score_map_backward or min_score_map_backward[state_key] > tentative_score:
                min_score_map_backward[state_key] = tentative_score
                minheap_push(minheap_backward, (tentative_score, neighbor_node, next_value))

run_algorithm()