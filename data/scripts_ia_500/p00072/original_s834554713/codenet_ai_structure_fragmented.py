def is_edge_crosses_set(vs, edge):
    return (vs[edge[0]] and not vs[edge[1]]) or (not vs[edge[0]] and vs[edge[1]])

def find_min_crossing_edge(vs, edges):
    min_dist = float("inf")
    ind = float("inf")
    pf = None
    pt = None
    for i in range(len(edges)):
        if is_edge_crosses_set(vs, edges[i]) and edges[i][2] < min_dist:
            min_dist, ind, pf, pt = edges[i][2], i, edges[i][0], edges[i][1]
    return min_dist, ind, pf, pt

def append_edge(E, dist):
    E.append(dist)

def mark_vertices_visited(vs, pf, pt):
    vs[pf] = True
    vs[pt] = True

def pop_edge(edges, index):
    edges.pop(index)

def all_vertices_visited(vs):
    return all(vs)

def remove_fully_visited_edges(vs, edges):
    i = 0
    while i < len(edges):
        if vs[edges[i][0]] and vs[edges[i][1]]:
            edges.pop(i)
        else:
            i += 1

def compute_result(E):
    return sum(E)/100.0 - len(E)

def solve(nu, mu, du):
    E = []
    vs = [False]*nu
    vs[0] = True

    while True:
        min_dist, ind, pf, pt = find_min_crossing_edge(vs, du)
        append_edge(E, min_dist)
        mark_vertices_visited(vs, pf, pt)
        pop_edge(du, ind)
        if all_vertices_visited(vs):
            break
        remove_fully_visited_edges(vs, du)

    print compute_result(E)

def read_edges(m):
    data = []
    for _ in range(m):
        line = raw_input()
        edge = map(int, line.split(","))
        data.append(edge)
    return data

def main():
    while True:
        n = input()
        if n == 0:
            exit()
        m = input()
        data = read_edges(m)
        solve(n, m, data)

main()