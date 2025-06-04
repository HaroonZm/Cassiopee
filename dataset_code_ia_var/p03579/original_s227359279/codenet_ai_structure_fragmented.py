def read_input():
    N, M = map(int, input().split())
    edge_list = []
    for _ in range(M):
        fr, to = map(int, input().split())
        edge_list.append((fr, to))
    return N, M, edge_list

def init_edges(N):
    return [[] for _ in range(N)]

def populate_edges(edge_list, edges):
    for fr, to in edge_list:
        add_edge(edges, fr, to)

def add_edge(edges, fr, to):
    u, v = normalize(fr), normalize(to)
    edges[u].append(v)
    edges[v].append(u)

def normalize(x):
    return x - 1

def get_bipartite_signature(N, edges):
    visited = [-1] * N
    return compute_bipartite_sum(N, edges, visited)

def compute_bipartite_sum(N, edges, visited):
    total = 0
    for start in range(N):
        if visited[start] == -1:
            sig = check_component_bipartite(start, edges, visited)
            if sig == -1:
                return -1
            total += sig
    return total

def check_component_bipartite(start, edges, visited):
    stack = [(start, 0)]
    counts = [0, 0]
    while stack:
        node, color = stack.pop()
        if visited[node] != -1:
            if visited[node] != color:
                return -1
            continue
        visited[node] = color
        counts[color] += 1
        for neighbor in edges[node]:
            stack.append((neighbor, (color + 1) % 2))
    return counts[0]

def calculate_result(N, M, bipartite_sum):
    if bipartite_sum == -1:
        return N * (N - 1) // 2 - M
    else:
        return bipartite_sum * (N - bipartite_sum) - M

def print_result(result):
    print(result)

def main():
    N, M, edge_list = read_input()
    edges = init_edges(N)
    populate_edges(edge_list, edges)
    bipartite_sum = get_bipartite_signature(N, edges)
    result = calculate_result(N, M, bipartite_sum)
    print_result(result)

main()