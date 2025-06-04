from heapq import heappush, heappop

number_of_nodes, colors_available = map(int, input().split())

edges_input_a, edges_input_b = (
    zip(*(map(int, input().split()) for _ in range(number_of_nodes - 1))) if number_of_nodes - 1 else
    ((), ())
)

MODULO_CONST = 10 ** 9 + 7

adjacency_list = [set() for _ in range(number_of_nodes + 1)]
for node_start, node_end in zip(edges_input_a, edges_input_b):
    adjacency_list[node_start].add(node_end)
    adjacency_list[node_end].add(node_start)

priority_queue = []
visited_nodes = [False for _ in range(number_of_nodes + 1)]

# Begin with node 1, color count starts at 1
heappush(priority_queue, (1, 1))
answer_count = colors_available
visited_nodes[1] = True

while priority_queue:
    current_node, used_colors_count = heappop(priority_queue)
    unvisited_neighbors = {neighbor for neighbor in adjacency_list[current_node] if not visited_nodes[neighbor]}
    for sibling_index, neighbor_node in enumerate(unvisited_neighbors):
        heappush(priority_queue, (neighbor_node, 2))   # Children get at least 2 previous colors blocked (root + parent)
        answer_count = (answer_count * (colors_available - used_colors_count - sibling_index)) % MODULO_CONST
        visited_nodes[neighbor_node] = True

print(answer_count)