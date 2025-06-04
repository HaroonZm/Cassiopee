from collections import deque

MOD = 10**9 + 7

def read_test_case():
    N, M = map(int, input().split())
    return N, M

def is_termination_case(N, M):
    return N == 0 and M == 0

def create_adjacency_list(N, M):
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = read_edge()
        add_edge(G, a, b)
    return G

def read_edge():
    a, b = map(int, input().split())
    return a, b

def add_edge(G, a, b):
    G[a-1].append(b-1)
    G[b-1].append(a-1)

def process_graph(N, G):
    used = [0] * N
    component_count = 0
    multi_node_component_count = 0
    for i in range(N):
        if is_node_used(used, i):
            continue
        component_count = increment(component_count)
        mark_node_used(used, i)
        node_in_component = count_component_nodes(i, G, used)
        if has_multiple_nodes(node_in_component):
            multi_node_component_count = increment(multi_node_component_count)
    return component_count, multi_node_component_count

def is_node_used(used, i):
    return used[i]

def increment(x):
    return x + 1

def mark_node_used(used, i):
    used[i] = 1

def count_component_nodes(start, G, used):
    que = initialize_queue()
    node_count = 1
    add_to_queue(que, start)
    while is_queue_not_empty(que):
        v = dequeue(que)
        for w in adjacency_list_of(G, v):
            if is_node_used(used, w):
                continue
            add_to_queue(que, w)
            mark_node_used(used, w)
            node_count = increment(node_count)
    return node_count

def initialize_queue():
    return deque()

def add_to_queue(que, node):
    que.append(node)

def is_queue_not_empty(que):
    return bool(que)

def dequeue(que):
    return que.popleft()

def adjacency_list_of(G, v):
    return G[v]

def has_multiple_nodes(c):
    return c > 1

def compute_result(N, component_count, multi_node_component_count):
    if has_multi_node_components(multi_node_component_count):
        return result_with_multi_components(component_count)
    else:
        return result_without_multi_components(N)

def has_multi_node_components(multi_node_component_count):
    return multi_node_component_count > 0

def result_with_multi_components(component_count):
    return (pow_mod(2, component_count, MOD) + 1) % MOD

def result_without_multi_components(N):
    return pow_mod(2, N, MOD)

def pow_mod(a, b, mod):
    return pow(a, b, mod)

def print_result(result):
    print(result)

def main():
    while True:
        N, M = read_test_case()
        if is_termination_case(N, M):
            break
        G = create_adjacency_list(N, M)
        component_count, multi_node_component_count = process_graph(N, G)
        result = compute_result(N, component_count, multi_node_component_count)
        print_result(result)

main()