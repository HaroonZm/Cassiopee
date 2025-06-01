import sys

def set_recursion_limit(limit):
    sys.setrecursionlimit(limit)

def read_graph_sizes():
    V = int(input())
    E = int(input())
    return V, E

def initialize_lists(V):
    L = []
    visited = [0 for _ in range(V)]
    edges = [[] for _ in range(V)]
    return L, visited, edges

def append_to_list(L):
    def app(x):
        L.append(x)
    return app

def read_edges(E, edges):
    for _ in range(E):
        s, t = map(int, input().split())
        edges[s - 1].append(t - 1)

def dfs_visit(x, visited, edges, app):
    if not visited[x]:
        mark_visited(x, visited)
        for e in edges[x]:
            dfs_visit(e, visited, edges, app)
        app(x)

def mark_visited(x, visited):
    visited[x] = 1

def perform_dfs(V, visited, edges, app):
    for i in range(V):
        if not visited[i]:
            dfs_visit(i, visited, edges, app)

def reverse_list(L):
    L.reverse()

def print_order_and_check_flag(L, edges, V):
    flag = 0
    for i in range(V):
        print(L[i] + 1)
        if flag == 0 and i < V - 1:
            flag = check_edge_presence(L, edges, i)
    print(flag)

def check_edge_presence(L, edges, i):
    if L[i + 1] not in edges[L[i]]:
        return 1
    return 0

def main():
    set_recursion_limit(100000)
    V, E = read_graph_sizes()
    L, visited, edges = initialize_lists(V)
    app = append_to_list(L)
    read_edges(E, edges)
    perform_dfs(V, visited, edges, app)
    reverse_list(L)
    print_order_and_check_flag(L, edges, V)

main()