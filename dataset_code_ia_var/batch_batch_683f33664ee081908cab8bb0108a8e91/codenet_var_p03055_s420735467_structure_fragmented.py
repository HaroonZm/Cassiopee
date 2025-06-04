import queue

def get_node_count():
    return int(input())

def initialize_tree(n):
    return {i: [] for i in range(n)}

def read_edge():
    t = input().split()
    return int(t[0]), int(t[1])

def add_edge(tree, u, v):
    tree[u-1].append(v-1)
    tree[v-1].append(u-1)

def build_tree(n):
    tree = initialize_tree(n)
    for _ in range(n-1):
        u, v = read_edge()
        add_edge(tree, u, v)
    return tree

def initialize_visited(n):
    return [0 for _ in range(n)]

def mark_visited(visited, node):
    visited[node] = 1

def create_queue():
    return queue.Queue()

def enqueue(q, item):
    q.put(item)

def dequeue(q):
    return q.get()

def has_children(tree, node):
    return len(tree[node]) > 1

def bfs_first(tree, n):
    a = 0
    q = create_queue()
    enqueue(q, a)
    v = initialize_visited(n)
    mark_visited(v, a)
    while not q.empty():
        a = dequeue(q)
        for b in tree[a]:
            if v[b] == 0 and has_children(tree, b):
                enqueue(q, b)
                mark_visited(v, b)
    return a

def prepare_visits(n, a):
    v = initialize_visited(n)
    mark_visited(v, a)
    return v

def bfs_second(tree, n, a):
    q = create_queue()
    enqueue(q, [a, 1])
    v = prepare_visits(n, a)
    last = None
    while not q.empty():
        a_item = dequeue(q)
        node, depth = a_item[0], a_item[1]
        last = a_item
        for b in tree[node]:
            if v[b] == 0 and has_children(tree, b):
                enqueue(q, [b, depth + 1])
                mark_visited(v, b)
    return last

def compute_l(n, second_bfs_result):
    if n <= 3:
        return n
    else:
        return second_bfs_result[1] + 2

def output_result(l):
    if l % 3 == 2:
        print("Second")
    else:
        print("First")

def main():
    n = get_node_count()
    tree = build_tree(n)
    a = bfs_first(tree, n)
    result = bfs_second(tree, n, a)
    l = compute_l(n, result)
    output_result(l)

main()