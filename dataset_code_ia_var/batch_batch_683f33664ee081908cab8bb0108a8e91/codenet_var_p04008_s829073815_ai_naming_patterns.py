import sys
stdin_readline = sys.stdin.readline

node_count, max_depth = map(int, stdin_readline().split())
parent_indices_input = list(map(int, stdin_readline().split()))

result_count = 0
adjacency_list = [[] for _ in range(node_count)]
parent_nodes = [-1] * node_count

for current_index, parent_index in enumerate(parent_indices_input):
    if current_index == 0:
        if parent_index != 1:
            result_count += 1
        continue
    parent_nodes[current_index] = parent_index - 1
    adjacency_list[parent_index - 1].append(current_index)

processing_order = []

node_stack = [0]
node_depths = [-1] * node_count
node_depths[0] = 0
while node_stack:
    current_node = node_stack.pop()
    for neighbor_node in adjacency_list[current_node]:
        node_depths[neighbor_node] = node_depths[current_node] + 1
        node_stack.append(neighbor_node)
    processing_order.append((node_depths[current_node], current_node))

processing_order.sort(reverse=True)
visited_nodes = [False] * node_count

for cur_depth, start_node in processing_order:
    if cur_depth <= max_depth:
        break
    if visited_nodes[start_node]:
        continue

    ascend_node = start_node
    for _ in range(max_depth - 1):
        ascend_node = parent_nodes[ascend_node]
    
    bfs_queue = [ascend_node]
    visited_nodes[ascend_node] = True
    while bfs_queue:
        next_queue = []
        for node in bfs_queue:
            for child_node in adjacency_list[node]:
                if not visited_nodes[child_node]:
                    visited_nodes[child_node] = True
                    next_queue.append(child_node)
        bfs_queue = next_queue
    
    result_count += 1

print(result_count)