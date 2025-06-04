from heapq import heappush, heappop

def read_input():
    num_nodes, num_edges, num_pairs, start_node = map(int, input().split())
    start_node -= 1
    adjacency_list = [[] for _ in range(num_nodes)]
    for _ in range(num_edges):
        u, v, weight = map(int, input().split())
        u -= 1
        v -= 1
        adjacency_list[u].append((v, weight))
        adjacency_list[v].append((u, weight))
    terminal_nodes = []
    for _ in range(num_pairs):
        pickup, dropoff = map(int, input().split())
        pickup -= 1
        dropoff -= 1
        terminal_nodes.append(pickup)
        terminal_nodes.append(dropoff)
    return num_nodes, num_edges, num_pairs, start_node, adjacency_list, terminal_nodes

INFINITY = 10 ** 20

def dijkstra(source_idx, node_count, edges):
    distances = [INFINITY] * node_count
    distances[source_idx] = 0
    heap = []
    heappush(heap, (0, source_idx))
    while heap:
        current_cost, current_node = heappop(heap)
        for neighbor, edge_weight in edges[current_node]:
            total_cost = current_cost + edge_weight
            if total_cost < distances[neighbor]:
                distances[neighbor] = total_cost
                heappush(heap, (total_cost, neighbor))
    return distances

def main():
    num_nodes, num_edges, num_pairs, start_node, adjacency_list, terminal_nodes = read_input()
    num_terminals = 2 * num_pairs
    pairwise_distances = [[None] * num_terminals for _ in range(num_terminals)]
    for idx_from in range(num_terminals):
        distances_from = dijkstra(terminal_nodes[idx_from], num_nodes, adjacency_list)
        for idx_to in range(num_terminals):
            pairwise_distances[idx_from][idx_to] = distances_from[terminal_nodes[idx_to]]
    start_to_terminal_distances = []
    start_distances = dijkstra(start_node, num_nodes, adjacency_list)
    for idx in range(num_terminals):
        start_to_terminal_distances.append(start_distances[terminal_nodes[idx]])
    dp_cache = {}
    final_state = (1 << num_terminals) - 1

    def find_min_cost(state_mask, current_terminal):
        cache_key = (state_mask, current_terminal)
        if cache_key in dp_cache:
            return dp_cache[cache_key]
        if state_mask == final_state:
            dp_cache[cache_key] = 0
            return 0
        minimal_cost = INFINITY
        for next_terminal in range(num_terminals):
            is_pair_second = (next_terminal % 2 == 1)
            pair_first_index = next_terminal - 1 if is_pair_second else None
            if (state_mask & (1 << next_terminal)) or (is_pair_second and not (state_mask & (1 << (next_terminal - 1)))):
                continue
            cost = pairwise_distances[current_terminal][next_terminal] + find_min_cost(state_mask | (1 << next_terminal), next_terminal)
            if cost < minimal_cost:
                minimal_cost = cost
        dp_cache[cache_key] = minimal_cost
        return minimal_cost

    result = INFINITY
    for pickup_idx in range(0, num_terminals, 2):
        total_cost = start_to_terminal_distances[pickup_idx] + find_min_cost(1 << pickup_idx, pickup_idx)
        if total_cost < result:
            result = total_cost
    if result == INFINITY:
        print("Cannot deliver")
    else:
        print(result)

if __name__ == "__main__":
    main()