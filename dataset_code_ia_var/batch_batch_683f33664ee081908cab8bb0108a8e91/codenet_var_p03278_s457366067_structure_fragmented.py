import sys
import numpy as np

def set_recursion_limit():
    sys.setrecursionlimit(10 ** 6)

def mod_value():
    return 10 ** 9 + 7

def get_input():
    return sys.stdin.readline

def create_empty_graph(n):
    return [[] for _ in range(n+1)]

def read_integer(input_func):
    return int(input_func())

def read_edge(input_func):
    return map(int, input_func().split())

def add_edge(graph, x, y):
    graph[x].append(y)
    graph[y].append(x)

def fill_graph(graph, n, input_func):
    for _ in range(n-1):
        x, y = read_edge(input_func)
        add_edge(graph, x, y)

def initialize_fact_2():
    return [1, 0, 1]

def expand_fact_2(fact_2, upper, mod):
    for n in range(3, upper):
        fact_2.append(fact_2[n-2] * (n-1) % mod)
    return fact_2

def numpy_array_int64(l):
    return np.array(l, dtype=np.int64)

def zeros_array(length):
    return np.zeros(length, dtype=np.int64)

def dp_merge_core(data1, data2, len1, len2, mod):
    data = zeros_array(len1+len2)
    for n in range(1, len1+1):
        data[n:n+len2] += data1[n] * data2[1:] % mod
    data %= mod
    return data

def dp_merge(data1, data2, mod):
    N1 = len(data1) - 1
    N2 = len(data2) - 1
    if N1 > N2:
        N1, N2 = N2, N1
        data1, data2 = data2, data1
    return dp_merge_core(data1, data2, N1, N2, mod)

def compute_dp_add_edge_values(data, fact_2, mod):
    N = len(data) - 1
    data1 = zeros_array(N+2)
    data1[1:] = data
    data1[1] = - (data * fact_2[:N+1] % mod).sum() % mod
    return data1

def dp_add_edge(data, fact_2, mod):
    return compute_dp_add_edge_values(data, fact_2, mod)

def process_child(y, v, graph, fact_2, mod, dfs_fn):
    data1 = dfs_fn(y, v, graph, fact_2, mod, dfs_fn)
    data1 = dp_add_edge(data1, fact_2, mod)
    return data1

def process_children(graph, v, parent, fact_2, mod, dfs_fn):
    data = None
    for y in graph[v]:
        if y == parent:
            continue
        data1 = process_child(y, v, graph, fact_2, mod, dfs_fn)
        if data is None:
            data = data1
        else:
            data = dp_merge(data, data1, mod)
    if data is None:
        return numpy_array_int64([0, 1])
    return data

def dfs(v, parent, graph, fact_2, mod, dfs_fn):
    return process_children(graph, v, parent, fact_2, mod, dfs_fn)

def calculate_answer(data, fact_2, N, mod):
    return (data * fact_2[:N+1] % mod).sum() % mod

def main():
    set_recursion_limit()
    mod = mod_value()
    input_func = get_input()
    N = read_integer(input_func)
    graph = create_empty_graph(N)
    fill_graph(graph, N, input_func)
    fact_2_list = initialize_fact_2()
    fact_2 = expand_fact_2(fact_2_list, N+10, mod)
    fact_2 = numpy_array_int64(fact_2)
    dfs_fn = dfs
    data = dfs_fn(1, None, graph, fact_2, mod, dfs_fn)
    answer = calculate_answer(data, fact_2, N, mod)
    print(answer)

main()