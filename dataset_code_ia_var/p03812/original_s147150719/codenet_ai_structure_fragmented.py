def read_n():
    return int(input())

def read_a(n):
    return list(map(int, input().split()))

def initialize_e(n):
    return [[] for _ in range(n)]

def read_edges(n):
    edges = []
    for _ in range(n - 1):
        x, y = map(int, input().split())
        edges.append((x, y))
    return edges

def build_graph(edges, n):
    e = initialize_e(n)
    for x, y in edges:
        add_edge(e, x, y)
    return e

def add_edge(e, x, y):
    add_single_edge(e, x - 1, y - 1)
    add_single_edge(e, y - 1, x - 1)

def add_single_edge(e, from_vertex, to_vertex):
    e[from_vertex].append(to_vertex)

def compare_values(a, v, i):
    return a[v] > a[i]

def not_b(v, i, r, e, a):
    return not b_recursive(v, i, r, e, a)

def b_recursive(r, v, parent, e, a):
    neighbors = get_neighbors(e, v)
    return count_conditions(r, v, neighbors, e, a)

def get_neighbors(e, v):
    return e[v]

def condition(r, v, i, e, a):
    return (r != i) and compare_values(a, v, i) and not_b(v, i, r, e, a)

def count_conditions(r, v, neighbors, e, a):
    cnt = 0
    for i in neighbors:
        if condition(r, v, i, e, a):
            cnt += 1
    return cnt

def b(r, v, e, a):
    return b_recursive(r, v, r, e, a)

def get_indices(n):
    return [i for i in range(n)]

def filter_indices(indices, n, e, a):
    result = []
    for i in indices:
        if b(n, i, e, a):
            result.append(i + 1)
    return result

def output(result):
    print(*result)

def main():
    n = read_n()
    a = read_a(n)
    edges = read_edges(n)
    e = build_graph(edges, n)
    indices = get_indices(n)
    result = filter_indices(indices, n, e, a)
    output(result)

main()