from collections import deque

number_of_nodes = int(input())

adjacency_list = [[] for node_index in range(number_of_nodes)]

for edge_index in range(number_of_nodes - 1):
    node_u, node_v = map(int, input().split())
    adjacency_list[node_u - 1].append(node_v - 1)
    adjacency_list[node_v - 1].append(node_u - 1)

first_search_parent = [-1 for node_index in range(number_of_nodes)]
first_search_distance = [-1 for node_index in range(number_of_nodes)]
first_search_visited = [0 for node_index in range(number_of_nodes)]

def breadth_first_search(start_node):
    first_search_visited[start_node] = 1
    first_search_distance[start_node] = 0

    initial_depth = 0

    node_queue = deque([(start_node, initial_depth)])

    while len(node_queue) > 0:
        current_node, current_depth = node_queue.popleft()
        for adjacent_node in adjacency_list[current_node]:
            if first_search_visited[adjacent_node]:
                continue
            first_search_visited[adjacent_node] = 1
            first_search_parent[adjacent_node] = current_node
            first_search_distance[adjacent_node] = current_depth + 1
            node_queue.append((adjacent_node, current_depth + 1))

second_search_parent = [-1 for node_index in range(number_of_nodes)]
second_search_distance = [-1 for node_index in range(number_of_nodes)]
second_search_visited = [0 for node_index in range(number_of_nodes)]

def breadth_first_search_fennec(start_node):
    fennec_count = 0
    second_search_visited[start_node] = 1
    second_search_distance[start_node] = 0

    initial_depth = 0

    node_queue = deque([(start_node, initial_depth)])

    while len(node_queue) > 0:
        current_node, current_depth = node_queue.popleft()
        for adjacent_node in adjacency_list[current_node]:
            if second_search_visited[adjacent_node]:
                continue
            fennec_count += 1
            second_search_visited[adjacent_node] = 1
            second_search_parent[adjacent_node] = (current_node, current_depth)
            second_search_distance[adjacent_node] = current_depth + 1
            node_queue.append((adjacent_node, current_depth + 1))
    return fennec_count

third_search_parent = [-1 for node_index in range(number_of_nodes)]
third_search_distance = [-1 for node_index in range(number_of_nodes)]
third_search_visited = [0 for node_index in range(number_of_nodes)]

def breadth_first_search_snuke(start_node):
    snuke_count = 0
    third_search_visited[start_node] = 1
    third_search_distance[start_node] = 0

    initial_depth = 0

    node_queue = deque([(start_node, initial_depth)])

    while len(node_queue) > 0:
        current_node, current_depth = node_queue.popleft()
        for adjacent_node in adjacency_list[current_node]:
            if third_search_visited[adjacent_node]:
                continue
            snuke_count += 1
            third_search_visited[adjacent_node] = 1
            third_search_parent[adjacent_node] = current_node
            third_search_distance[adjacent_node] = current_depth + 1
            node_queue.append((adjacent_node, current_depth + 1))
    return snuke_count

breadth_first_search(0)

shortest_path_length = first_search_distance[number_of_nodes - 1]

current_node_on_path = number_of_nodes - 1

second_search_visited[number_of_nodes - 1] = 1
third_search_visited[0] = 1

for path_index in range(shortest_path_length):
    if (shortest_path_length - path_index) >= (shortest_path_length + 2) // 2:
        second_search_visited[current_node_on_path] = 1
        current_node_on_path = first_search_parent[current_node_on_path]
    else:
        third_search_visited[current_node_on_path] = 1
        current_node_on_path = first_search_parent[current_node_on_path]

fennec_area_count = breadth_first_search_fennec(0)
snuke_area_count = breadth_first_search_snuke(number_of_nodes - 1)

if fennec_area_count > snuke_area_count:
    print("Fennec")
else:
    print("Snuke")