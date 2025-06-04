from collections import deque

node_count = int(input())
adjacency_list = [[] for idx in range(node_count)]

for edge_idx in range(node_count - 1):
    node_a, node_b = map(int, input().split())
    adjacency_list[node_a - 1].append(node_b - 1)
    adjacency_list[node_b - 1].append(node_a - 1)

parent_main = [-1 for idx in range(node_count)]
distance_main = [-1 for idx in range(node_count)]
visited_main = [False for idx in range(node_count)]

def bfs_main(start_idx):
    visited_main[start_idx] = True
    distance_main[start_idx] = 0
    queue_main = deque([(start_idx, 0)])
    while queue_main:
        current_node, current_dist = queue_main.popleft()
        for neighbor in adjacency_list[current_node]:
            if visited_main[neighbor]:
                continue
            visited_main[neighbor] = True
            parent_main[neighbor] = current_node
            distance_main[neighbor] = current_dist + 1
            queue_main.append((neighbor, current_dist + 1))

parent_fennec = [-1 for idx in range(node_count)]
distance_fennec = [-1 for idx in range(node_count)]
visited_fennec = [False for idx in range(node_count)]

def bfs_fennec(start_idx):
    explored_fennec = 0
    visited_fennec[start_idx] = True
    distance_fennec[start_idx] = 0
    queue_fennec = deque([(start_idx, 0)])
    while queue_fennec:
        current_node, current_dist = queue_fennec.popleft()
        for neighbor in adjacency_list[current_node]:
            if visited_fennec[neighbor]:
                continue
            explored_fennec += 1
            visited_fennec[neighbor] = True
            parent_fennec[neighbor] = (current_node, current_dist)
            distance_fennec[neighbor] = current_dist + 1
            queue_fennec.append((neighbor, current_dist + 1))
    return explored_fennec

parent_snuke = [-1 for idx in range(node_count)]
distance_snuke = [-1 for idx in range(node_count)]
visited_snuke = [False for idx in range(node_count)]

def bfs_snuke(start_idx):
    explored_snuke = 0
    visited_snuke[start_idx] = True
    distance_snuke[start_idx] = 0
    queue_snuke = deque([(start_idx, 0)])
    while queue_snuke:
        current_node, current_dist = queue_snuke.popleft()
        for neighbor in adjacency_list[current_node]:
            if visited_snuke[neighbor]:
                continue
            explored_snuke += 1
            visited_snuke[neighbor] = True
            parent_snuke[neighbor] = current_node
            distance_snuke[neighbor] = current_dist + 1
            queue_snuke.append((neighbor, current_dist + 1))
    return explored_snuke

bfs_main(0)
path_distance = distance_main[node_count - 1]

current = node_count - 1
visited_fennec[node_count - 1] = True
visited_snuke[0] = True
for path_idx in range(path_distance):
    if (path_distance - path_idx) >= (path_distance + 2) // 2:
        visited_fennec[current] = True
        current = parent_main[current]
    else:
        visited_snuke[current] = True
        current = parent_main[current]

fennec_result = bfs_fennec(0)
snuke_result = bfs_snuke(node_count - 1)

if fennec_result > snuke_result:
    print("Fennec")
else:
    print("Snuke")