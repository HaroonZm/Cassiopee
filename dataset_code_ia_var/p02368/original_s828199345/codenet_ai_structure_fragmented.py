import sys

def set_recursion():
    sys.setrecursionlimit(int(1e5))

def get_graph_info():
    nvertices, nedges = read_two_ints()
    return nvertices, nedges

def read_two_ints():
    return map(int, input().split())

def init_adj_lists(n):
    return [[] for _ in range(n)], [[] for _ in range(n)]

def process_edges(nedges, Adj, AdjRev):
    for _ in range(nedges):
        u, v = read_two_ints()
        add_edge(u, v, Adj, AdjRev)

def add_edge(u, v, Adj, AdjRev):
    Adj[u].append(v)
    AdjRev[v].append(u)

def initialize_visited(n):
    return [False] * n

def dfs_all_vertices(nvertices, Adj, visited, action, lst=None):
    for u in range(nvertices):
        if not visited[u]:
            action(u, Adj, visited, lst)

def dfs_first(u, Adj, visited, lst):
    mark_visited(u, visited)
    for v in Adj[u]:
        if not is_visited(v, visited):
            dfs_first(v, Adj, visited, lst)
    append_to_list(u, lst)

def mark_visited(u, visited):
    visited[u] = True

def is_visited(u, visited):
    return visited[u]

def append_to_list(u, lst):
    lst.append(u)

def reverse_list(lst):
    lst.reverse()

def init_ids(n):
    return [-1] * n

def dfs_assign_ids(lst, AdjRev, visited, ids):
    curr_id = [0]
    for u in lst:
        if not visited[u]:
            dfs_second(u, AdjRev, visited, curr_id[0], ids)
            increment_id(curr_id)
    return

def dfs_second(u, Adj, visited, id, ids):
    set_id(u, id, ids)
    mark_visited(u, visited)
    for v in Adj[u]:
        if not is_visited(v, visited):
            dfs_second(v, Adj, visited, id, ids)

def set_id(u, id, ids):
    ids[u] = id

def increment_id(curr_id):
    curr_id[0] += 1

def process_queries(ids):
    Q = read_query_count()
    for _ in range(Q):
        u, v = read_two_ints()
        print_result(ids, u, v)

def read_query_count():
    return int(input())

def print_result(ids, u, v):
    output_result(1 if ids[u] == ids[v] else 0)

def output_result(res):
    print(res)

def main():
    set_recursion()
    nvertices, nedges = get_graph_info()
    Adj, AdjRev = init_adj_lists(nvertices)
    process_edges(nedges, Adj, AdjRev)
    lst = []
    visited = initialize_visited(nvertices)
    dfs_all_vertices(nvertices, Adj, visited, dfs_first, lst)
    reverse_list(lst)
    ids = init_ids(nvertices)
    visited = initialize_visited(nvertices)
    dfs_assign_ids(lst, AdjRev, visited, ids)
    process_queries(ids)

main()