import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)

def create_default_dict():
    return defaultdict(lambda: None)

def read_int():
    return int(sys.stdin.readline())

def read_edge():
    return [int(x) for x in sys.stdin.readline().split()]

def initialize_state(n):
    return [0] * n

def initialize_adjacency_matrix(n):
    matrix = [[1] * n for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 0
    return matrix

def process_existing_edges(m, s, f):
    for _ in range(m):
        x, y = read_edge()
        x -= 1
        y -= 1
        s[x] += 1
        f[x][y] = 0
        f[y][x] = 0

def get_remaining_pairs(n, f):
    return [(i, j) for i in range(n) for j in range(i+1, n) if f[i][j]]

def get_half_n(n):
    return n >> 1

def is_terminal_depth(d, l):
    return d == l

def as_tuple(s):
    return tuple(s)

def check_s_limits(s, half_n):
    for x in s:
        if x > half_n:
            return False
    return True

def dfs_decision_paths(d, s, l, v, dic, n):
    s_tuple = as_tuple(s)
    if dic[(d, s_tuple)] is not None:
        return dic[(d, s_tuple)]
    if is_terminal_depth(d, l):
        dic[(d, s_tuple)] = terminal_case(s, n)
        return dic[(d, s_tuple)]
    else:
        res = 0
        i, j = v[d]
        half_n = get_half_n(n)
        if s[i] < half_n:
            s[i] += 1
            res += dfs_decision_paths(d + 1, s, l, v, dic, n)
            s[i] -= 1
        if s[j] < half_n:
            s[j] += 1
            res += dfs_decision_paths(d + 1, s, l, v, dic, n)
            s[j] -= 1
        dic[(d, s_tuple)] = res
        return res

def terminal_case(s, n):
    half_n = get_half_n(n)
    if check_s_limits(s, half_n):
        return 1
    return 0

def solve(n):
    dic = create_default_dict()
    m = read_int()
    s = initialize_state(n)
    f = initialize_adjacency_matrix(n)
    process_existing_edges(m, s, f)
    v = get_remaining_pairs(n, f)
    l = len(v)
    print(run_dfs(n, s, l, v, dic))

def run_dfs(n, s, l, v, dic):
    return dfs_decision_paths(0, s, l, v, dic, n)

def main_loop():
    while True:
        n = read_int()
        if stop_condition(n):
            break
        solve(n)

def stop_condition(n):
    return n == 0

main_loop()