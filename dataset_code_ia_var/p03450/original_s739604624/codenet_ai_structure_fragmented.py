import sys

def read_input():
    n, m = map(int, input().split())
    return n, m

def read_edges(m):
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))
    return edges

def create_empty_connections(n):
    return [[] for _ in range(n)]

def add_edge(connection, u, v, w):
    connection[u].append((v, w))

def populate_connections(connection, edges):
    for edge in edges:
        u, v, w = edge
        add_edge(connection, u-1, v-1, w)
        add_edge(connection, v-1, u-1, -w)

def create_distance_list(n):
    return [-999999999999] * n

def create_visited_list(n):
    return [-1] * n

def need_bfs(distance, i):
    return distance[i] == -999999999999

def enqueue_start(distance, v):
    distance[v] = 0

def process_next_node(next_node, visited, visitct):
    if visited[next_node] == -1:
        visited[next_node] = 1
        visitct += 1
    return visitct

def process_neighbors(current, connection, visited, distance, next2):
    for neighbor, weight in connection[current]:
        if visited[neighbor] == -1:
            distance[neighbor] = distance[current] + weight
            next2.add(neighbor)

def bfs_util(next_nodes, connection, visited, distance, n):
    next2 = set()
    visitct = 0
    while len(next_nodes) != 0 and visitct != n:
        for i in range(len(next_nodes)):
            current = next_nodes[i]
            visitct = process_next_node(current, visited, visitct)
            if visited[current] == 1:  # Only traverse non-visited in this round
                process_neighbors(current, connection, visited, distance, next2)
        next_nodes = list(next2)
        next2 = set()

def bfs(v, connection, visited, distance, n):
    enqueue_start(distance, v)
    next_nodes = [v]
    bfs_util(next_nodes, connection, visited, distance, n)

def perform_bfs_on_unvisited(distance, connection, visited, n):
    for i in range(n):
        if need_bfs(distance, i):
            bfs(i, connection, visited, distance, n)

def check_consistency(edges, distance):
    for edge in edges:
        u, v, w = edge
        if distance[v-1] - distance[u-1] != w:
            return False
    return True

def print_no_and_exit():
    print('No')
    sys.exit()

def print_yes():
    print('Yes')

def main():
    n, m = read_input()
    edges = read_edges(m)
    connection = create_empty_connections(n)
    populate_connections(connection, edges)
    distance = create_distance_list(n)
    visited = create_visited_list(n)
    perform_bfs_on_unvisited(distance, connection, visited, n)
    if not check_consistency(edges, distance):
        print_no_and_exit()
    print_yes()

main()