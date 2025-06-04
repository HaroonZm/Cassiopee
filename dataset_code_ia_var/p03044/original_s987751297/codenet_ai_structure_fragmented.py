def read_n():
    return int(input())

def read_edge():
    u, v, w = map(int, input().split())
    return u, v, w

def ensure_key(d, k):
    from collections import deque
    if k not in d:
        d[k] = deque()

def add_edge(neighbor, u, v, w):
    ensure_key(neighbor, u)
    ensure_key(neighbor, v)
    neighbor[u].append((v, w))
    neighbor[v].append((u, w))

def build_neighbors(n):
    from collections import deque
    neighbor = {}
    for _ in range(n - 1):
        u, v, w = read_edge()
        add_edge(neighbor, u, v, w)
    return neighbor

def init_color():
    return {1: 0}

def init_visited():
    return set([1])

def init_queue():
    from collections import deque
    return deque([(1, 0)])

def visit_node(queue):
    return queue.pop()

def process_neighbors(v, wsum, neighbor, visited, color, queue):
    for u, w in neighbor[v]:
        if skip_visited(u, visited):
            continue
        mark_visited(u, visited)
        assign_color(u, wsum, w, color)
        add_to_queue(u, wsum, w, queue)

def skip_visited(u, visited):
    return u in visited

def mark_visited(u, visited):
    visited.add(u)

def assign_color(u, wsum, w, color):
    color[u] = (wsum + w) % 2

def add_to_queue(u, wsum, w, queue):
    queue.append((u, wsum + w))

def traverse(neighbor, color, visited, queue):
    while not queue_empty(queue):
        v, wsum = visit_node(queue)
        process_neighbors(v, wsum, neighbor, visited, color, queue)

def queue_empty(queue):
    return len(queue) == 0

def print_colors(n, color):
    for i in range(n):
        print(get_color(i + 1, color))

def get_color(i, color):
    return color[i]

def main():
    n = read_n()
    neighbor = build_neighbors(n)
    color = init_color()
    visited = init_visited()
    queue = init_queue()
    traverse(neighbor, color, visited, queue)
    print_colors(n, color)

main()