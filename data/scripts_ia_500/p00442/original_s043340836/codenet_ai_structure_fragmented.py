def initialize_count_list(V):
    return [0] * V

def increment_counts(V, to, cnt):
    for i in range(V):
        for j in to[i]:
            cnt[j] += 1

def find_zero_count_nodes(V, cnt):
    Q = []
    for i in range(V):
        if cnt[i] == 0:
            Q.append(i)
    return Q

def pop_first_element(Q):
    i = Q[0]
    del Q[0]
    return i

def process_node_counts(to, cnt, node, Q):
    for k in to[node]:
        cnt[k] -= 1
        if cnt[k] == 0:
            Q.append(k)

def print_node_plus_one(node):
    print(node + 1)

def topological_sort(V, to):
    cnt = initialize_count_list(V)
    increment_counts(V, to, cnt)
    Q = find_zero_count_nodes(V, cnt)
    f = 0
    while len(Q) > 0:
        f |= len(Q) > 1
        i = pop_first_element(Q)
        print_node_plus_one(i)
        process_node_counts(to, cnt, i, Q)
    return f

def read_integer():
    return int(input())

def initialize_to_list(n):
    return [[] for _ in range(n)]

def read_edge_and_append_to_list(to):
    a, b = list(map(int, input().split()))
    to[a - 1].append(b - 1)

def read_all_edges(m, to):
    for _ in range(m):
        read_edge_and_append_to_list(to)

def main():
    n = read_integer()
    to = initialize_to_list(n)
    m = read_integer()
    read_all_edges(m, to)
    print(1 if topological_sort(n, to) else 0)

main()