from collections import deque

def read_ints():
    return list(map(int, input().split()))

def get_input_sizes():
    return read_ints()

def initialize_graph(n):
    return [[] for _ in range(n)]

def add_edge(graph, l, r, d):
    graph[l-1].append([r-1, d])
    graph[r-1].append([l-1, -d])

def build_graph(m, graph):
    for _ in range(m):
        l, r, d = read_ints()
        add_edge(graph, l, r, d)

def initialize_x(n):
    return [None for _ in range(n)]

def process_queue(q, x, graph, n):
    while not is_queue_empty(q):
        j = dequeue(q)
        if not process_neighbors(j, x, graph, q):
            return False
    return True

def is_queue_empty(q):
    return len(q) == 0

def dequeue(q):
    return q.popleft()

def process_neighbors(j, x, graph, q):
    for neighbor in graph[j]:
        k, d = neighbor
        if x[k] is None:
            enqueue(q, k)
            update_x(x, k, x[j], d)
        elif not check_x_consistency(x, k, x[j], d):
            return False
    return True

def enqueue(q, k):
    q.append(k)

def update_x(x, k, xj, d):
    x[k] = xj + d

def check_x_consistency(x, k, xj, d):
    return x[k] == xj + d

def f(x, graph, n):
    for i in range(n):
        if x[i] is None:
            set_x_initial(x, i)
            q = init_queue_with(i)
            if not process_queue(q, x, graph, n):
                return False
    return True

def set_x_initial(x, i):
    x[i] = 0

def init_queue_with(i):
    return deque([i])

def output_result(result):
    if result:
        print("Yes")
    else:
        print("No")

def main():
    n, m = get_input_sizes()
    graph = initialize_graph(n)
    build_graph(m, graph)
    x = initialize_x(n)
    result = f(x, graph, n)
    output_result(result)

main()