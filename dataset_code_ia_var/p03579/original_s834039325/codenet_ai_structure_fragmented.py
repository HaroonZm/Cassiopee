def read_input():
    return map(int, input().split())

def init_graph(n):
    return [[] for _ in range(n)]

def add_edge(graph, a, b):
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

def build_graph(n, m):
    graph = init_graph(n)
    for _ in range(m):
        a, b = read_input()
        add_edge(graph, a, b)
    return graph

def init_queue():
    from collections import deque
    return deque()

def enqueue(queue, elem):
    queue.append(elem)

def dequeue(queue):
    return queue.popleft()

def queue_empty(queue):
    return len(queue) == 0

def init_colors(n):
    return [-1] * n

def set_color(colors, idx, color):
    colors[idx] = color

def get_color(colors, idx):
    return colors[idx]

def is_unvisited(colors, idx):
    return colors[idx] == -1

def is_same_color(color1, color2):
    return color1 == color2

def other_color(color):
    return 1 - color

def color_component(graph, colors, queue):
    bipartite = True
    while not queue_empty(queue):
        node = dequeue(queue)
        pc = get_color(colors, node)
        for neighbor in graph[node]:
            if is_unvisited(colors, neighbor):
                set_color(colors, neighbor, other_color(pc))
                enqueue(queue, neighbor)
                continue
            if is_same_color(get_color(colors, neighbor), pc):
                bipartite = False
    return bipartite

def count_colors(colors, c):
    return colors.count(c)

def total_possible_edges(n):
    return n * (n - 1) // 2

def print_result_not_bipartite(n, m):
    print(total_possible_edges(n) - m)

def print_result_bipartite(colors, m):
    w = count_colors(colors, 0)
    b = count_colors(colors, 1)
    print(w * b - m)

def main():
    n, m = read_input()
    graph = build_graph(n, m)
    queue = init_queue()
    enqueue(queue, 0)
    colors = init_colors(n)
    set_color(colors, 0, 0)
    bipartite = color_component(graph, colors, queue)
    if not bipartite:
        print_result_not_bipartite(n, m)
    else:
        print_result_bipartite(colors, m)

main()