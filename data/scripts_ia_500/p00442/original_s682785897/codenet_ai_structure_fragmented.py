import sys
def set_recursion_limit(limit):
    sys.setrecursionlimit(limit)

def read_vertices():
    return int(input())

def read_edges_count():
    return int(input())

def initialize_visited(size):
    visited_list = []
    for i in range(size):
        visited_list.append(0)
    return visited_list

def initialize_edges_list(size):
    edges_list = []
    for i in range(size):
        edges_list.append([])
    return edges_list

def read_edge():
    edge_input = input().split()
    start = int(edge_input[0])
    end = int(edge_input[1])
    return start, end

def add_edge(edges, start, end):
    edges[start - 1].append(end - 1)

def is_visited(visited, node):
    return visited[node] != 0

def mark_visited(visited, node):
    visited[node] = 1

def get_edges(edges, node):
    return edges[node]

def visit(node, visited, edges, result_list):
    if not is_visited(visited, node):
        mark_visited(visited, node)
        node_edges = get_edges(edges, node)
        for e in node_edges:
            visit(e, visited, edges, result_list)
        result_list.append(node)

def process_all_vertices(V, visited, edges, result_list):
    for i in range(V):
        if not is_visited(visited, i):
            visit(i, visited, edges, result_list)

def reverse_list_in_place(lst):
    lst.reverse()

def print_vertex(vertex):
    print(vertex + 1)

def is_last_index(i, V):
    return i < V - 1

def check_edge_exists(edges, source, destination):
    return destination in edges[source]

def print_order_and_flag(L, edges, V):
    flag = 0
    for i in range(V):
        print_vertex(L[i])
        if flag == 0 and is_last_index(i, V):
            if not check_edge_exists(edges, L[i], L[i+1]):
                flag = 1
    print(flag)

def main():
    set_recursion_limit(100000)
    V = read_vertices()
    E = read_edges_count()
    visited = initialize_visited(V)
    edges = initialize_edges_list(V)
    for _ in range(E):
        start, end = read_edge()
        add_edge(edges, start, end)
    L = []
    process_all_vertices(V, visited, edges, L)
    reverse_list_in_place(L)
    print_order_and_flag(L, edges, V)

main()