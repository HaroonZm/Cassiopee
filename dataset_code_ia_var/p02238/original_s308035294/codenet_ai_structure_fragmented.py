def read_input_n():
    return int(input())

def read_input_edges(n):
    return [parse_edge_input() for _ in range(n)]

def parse_edge_input():
    u, k, *v = map(int, input().split())
    return v

def build_field(edge_lists):
    field = [[0, 0]]
    for v in edge_lists:
        field.append(v)
    return field

def initialize_list(size):
    return [0 for _ in range(size + 1)]

def dfs_entry_point(n, field, d, f):
    count = 1
    for i in range(1, n + 1):
        if is_discovered(d, i):
            continue
        count = dfs_dispatch(i, field, d, f, count)
    return count

def is_discovered(d, i):
    return d[i] != 0

def dfs_dispatch(index, field, d, f, count):
    count = dfs_entry(index, d, count)
    count = dfs_explore(index, field, d, f, count)
    count = dfs_exit(index, f, count)
    return count

def dfs_entry(index, d, count):
    d[index] = count
    return count + 1

def dfs_explore(index, field, d, f, count):
    for i in iterate_neighbors(field, index):
        if is_discovered(d, i):
            continue
        count = dfs_dispatch(i, field, d, f, count)
    return count

def iterate_neighbors(field, index):
    return field[index]

def dfs_exit(index, f, count):
    f[index] = count
    return count

def print_results(n, d, f):
    for i in range(1, n + 1):
        show_line(i, d, f)

def show_line(i, d, f):
    print(i, d[i], f[i])

def main():
    n = read_input_n()
    edge_lists = read_input_edges(n)
    field = build_field(edge_lists)
    d = initialize_list(n)
    f = initialize_list(n)
    dfs_entry_point(n, field, d, f)
    print_results(n, d, f)

main()