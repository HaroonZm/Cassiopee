import sys
from heapq import heapify, heappop, heappush

def read_input():
    return sys.stdin.readline().rstrip()

def read_int():
    return int(read_input())

def read_int_list():
    return list(map(int, read_input().split()))

def create_graph(node_count):
    return [[] for _ in range(node_count + 1)]

def connect_nodes(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

def initialize_distances(size, value):
    return [value] * size

def set_start_distance(distances, start):
    distances[start] = 0

def create_priority_queue(start):
    return [(0, start)]

def should_continue(distances, current, dist):
    return distances[current] < dist

def calculate_next_distance(dist):
    return dist + 1

def update_distance_if_shorter(distances, queue, neighbor, new_dist):
    if distances[neighbor] > new_dist:
        distances[neighbor] = new_dist
        heappush(queue, (new_dist, neighbor))

def process_neighbors(graph, distances, queue, current, dist):
    for neighbor in graph[current]:
        new_dist = calculate_next_distance(dist)
        update_distance_if_shorter(distances, queue, neighbor, new_dist)

def dijkstra_process(graph, node_count, start):
    INF = 10 ** 15
    distances = initialize_distances(node_count + 1, INF)
    set_start_distance(distances, start)
    queue = create_priority_queue(start)
    while queue:
        dist, current = heappop(queue)
        if should_continue(distances, current, dist):
            continue
        process_neighbors(graph, distances, queue, current, dist)
    return distances

def sort_distances_with_indices(distances):
    return sorted([(x, i) for i, x in enumerate(distances)], reverse=True)

def get_second_far_node(sorted_distances):
    return sorted_distances[1][1]

def find_diameter(distances):
    return max(distances[1:]) + 1

def calculate_bl(diameter):
    return diameter % 3 != 2

def print_result(bl):
    print('First' if bl else 'Second')

def main():
    N = read_int()
    graph = create_graph(N)
    def read_and_connect(_):
        a, b = read_int_list()
        connect_nodes(graph, a, b)
    for _ in range(N-1):
        read_and_connect(_)
    first_dist = dijkstra_process(graph, N, 1)
    sorted_dist = sort_distances_with_indices(first_dist)
    new_root = get_second_far_node(sorted_dist)
    second_dist = dijkstra_process(graph, N, new_root)
    diameter = find_diameter(second_dist)
    bl = calculate_bl(diameter)
    print_result(bl)

main()