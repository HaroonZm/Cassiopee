def read_input_line():
    return input().split()

def parse_n(line):
    return int(line[0])

def parse_m(line):
    return int(line[1])

def initialize_path(n):
    return [[] for _ in range(n)]

def get_edge_input():
    return input().split()

def parse_edge(line):
    a = int(line[0]) - 1
    b = int(line[1]) - 1
    return a, b

def add_edge(path, a, b):
    path[a].append(b)

def build_graph(n, m):
    path = initialize_path(n)
    for _ in range(m):
        line = get_edge_input()
        a, b = parse_edge(line)
        add_edge(path, a, b)
    return path

def is_end_node(i, n):
    return i == n - 1

def is_valid_path_length(s):
    return s == 2

def dfs_util(i, s, n, path):
    if is_end_node(i, n):
        return check_success(s)
    return dfs_explore_neighbors(i, s, n, path)

def check_success(s):
    if is_valid_path_length(s):
        return True
    return False

def dfs_explore_neighbors(i, s, n, path):
    for e in path[i]:
        if dfs_util(e, s + 1, n, path):
            return True
    return False

def check_path_exists(path, n):
    return dfs_util(0, 0, n, path)

def output_result(result):
    if result:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")

def main():
    line = read_input_line()
    n = parse_n(line)
    m = parse_m(line)
    path = build_graph(n, m)
    result = check_path_exists(path, n)
    output_result(result)

main()