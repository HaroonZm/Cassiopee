import sys

def set_recursion_limit():
    sys.setrecursionlimit(10 ** 8)

def input_n():
    return int(raw_input())

def initialize_graph(n):
    return [[] for _ in xrange(n)]

def read_edge():
    a, b = map(int, raw_input().split())
    return a - 1, b - 1

def add_edge(g, a, b):
    g[a].append(b)
    g[b].append(a)

def build_graph(g, n):
    for _ in xrange(n - 1):
        a, b = read_edge()
        add_edge(g, a, b)

def initialize_path():
    return []

def append_to_path(path, node):
    path.append(node)

def reverse_path(path):
    path.reverse()

def is_target_node(now, n):
    return now == n - 1

def find_path(now, par, g, n, path):
    if is_target_node(now, n):
        append_to_path(path, n - 1)
        return True
    for to in g[now]:
        if to == par:
            continue
        if find_path(to, now, g, n, path):
            append_to_path(path, now)
            return True
    return False

def initialize_color(n):
    return ["bl"] * n

def set_start_colors(color, n):
    color[0] = "b"
    color[n - 1] = "w"

def path_indices(path):
    return 1, len(path) - 2

def process_path(path, color):
    j, k = path_indices(path)
    for i in xrange(1, len(path) - 1):
        if i % 2 == 1:
            v = path[j]
            color[v] = "b"
            j += 1
        else:
            v = path[k]
            color[v] = "w"
            k -= 1

def dfs1(now, par, color, g):
    color[now] = "b"
    for to in g[now]:
        if to == par:
            continue
        if color[to] == "w":
            continue
        dfs1(to, now, color, g)

def dfs2(now, par, color, g):
    color[now] = "w"
    for to in g[now]:
        if to == par:
            continue
        if color[to] == "b":
            continue
        dfs2(to, now, color, g)

def count_colors(n, color):
    cntf = 0
    cnts = 0
    for i in xrange(n):
        if color[i] == "b":
            cntf += 1
        else:
            cnts += 1
    return cntf, cnts

def decide_winner(cntf, cnts):
    if cntf > cnts:
        print "Fennec"
    else:
        print "Snuke"

def main():
    set_recursion_limit()
    n = input_n()
    g = initialize_graph(n)
    build_graph(g, n)
    path = initialize_path()
    find_path(0, -1, g, n, path)
    reverse_path(path)
    color = initialize_color(n)
    set_start_colors(color, n)
    process_path(path, color)
    dfs1(0, -1, color, g)
    dfs2(n - 1, -1, color, g)
    cntf, cnts = count_colors(n, color)
    decide_winner(cntf, cnts)

main()