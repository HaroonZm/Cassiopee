import sys
sys.setrecursionlimit(114514)
node_count = int(input())
adjacency_list = [[] for _ in range(node_count + 1)]
for _ in range(node_count - 1):
    node_u, node_v = map(int, input().split())
    adjacency_list[node_u].append(node_v)
    adjacency_list[node_v].append(node_u)
distance_fennec = [-1] * (node_count + 1)
distance_snuke = [-1] * (node_count + 1)
def compute_distances(distance_array, current_node, current_distance):
    if distance_array[current_node] == -1:
        distance_array[current_node] = current_distance
        for adjacent_node in adjacency_list[current_node]:
            compute_distances(distance_array, adjacent_node, current_distance + 1)
compute_distances(distance_fennec, 1, 0)
compute_distances(distance_snuke, node_count, 0)
fennec_count = 0
snuke_count = 0
for index in range(1, node_count + 1):
    if distance_snuke[index] < distance_fennec[index]:
        snuke_count += 1
    else:
        fennec_count += 1
print("Fennec" if fennec_count > snuke_count else "Snuke")