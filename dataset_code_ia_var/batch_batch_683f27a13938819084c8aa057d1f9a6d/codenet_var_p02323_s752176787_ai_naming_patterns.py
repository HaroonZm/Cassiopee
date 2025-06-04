INFINITY = 2 ** 31

from itertools import product

def solve_tsp_dp(vertex_count, adjacency_matrix):
    bitset_max = 1 << vertex_count
    min_cost_dp = [[INFINITY] * vertex_count for _ in range(bitset_max)]
    min_cost_dp[0][0] = 0
    for visited_set in range(bitset_max):
        for from_vertex, to_vertex in product(range(vertex_count), repeat=2):
            if (visited_set >> to_vertex) & 1:
                continue
            next_set = visited_set | (1 << to_vertex)
            min_cost_dp[next_set][to_vertex] = min(
                min_cost_dp[next_set][to_vertex],
                min_cost_dp[visited_set][from_vertex] + adjacency_matrix[from_vertex][to_vertex]
            )
    result = min_cost_dp[bitset_max - 1][0]
    print(result if result != INFINITY else -1)

vertex_total, edge_total = map(int, input().split())
adjacency_matrix = [[INFINITY] * vertex_total for _ in range(vertex_total)]
for _ in range(edge_total):
    source_vertex, target_vertex, edge_cost = map(int, input().split())
    adjacency_matrix[source_vertex][target_vertex] = edge_cost
solve_tsp_dp(vertex_total, adjacency_matrix)