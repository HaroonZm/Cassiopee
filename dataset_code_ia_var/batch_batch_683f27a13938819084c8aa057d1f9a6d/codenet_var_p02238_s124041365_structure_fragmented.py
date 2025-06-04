def get_input_n():
    return int(input())

def create_zero_matrix(n):
    return [[0 for _ in range(n)] for _ in range(n)]

def read_vertex_input():
    return list(map(int, input().split()))

def update_adjacency_matrix(n, A):
    def process_row(_):
        u, k, *v_list = read_vertex_input()
        def set_edge(v):
            A[u-1][v-1] = 1
        for v in v_list:
            set_edge(v)
    for i in range(n):
        process_row(i)

def create_zero_list(n):
    return [0] * n

def increment_time(t):
    return t + 1

def dfs_visit(u, n, A, d, f, t_holder):
    t_holder[0] = increment_time(t_holder[0])
    d[u] = t_holder[0]
    def visit_neighbor(v):
        if A[u][v] == 1 and d[v] == 0:
            dfs_visit(v, n, A, d, f, t_holder)
    for v in range(n):
        visit_neighbor(v)
    t_holder[0] = increment_time(t_holder[0])
    f[u] = t_holder[0]

def perform_dfs(n, A, d, f):
    t_holder = [0]
    def do_dfs(i):
        if d[i] == 0:
            dfs_visit(i, n, A, d, f, t_holder)
    for i in range(n):
        do_dfs(i)

def print_output(n, d, f):
    def print_line(i):
        print(i+1, d[i], f[i])
    for i in range(n):
        print_line(i)

def main():
    n = get_input_n()
    A = create_zero_matrix(n)
    update_adjacency_matrix(n, A)
    d = create_zero_list(n)
    f = create_zero_list(n)
    perform_dfs(n, A, d, f)
    print_output(n, d, f)

main()