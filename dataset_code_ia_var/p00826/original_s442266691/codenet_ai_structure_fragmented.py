def string_to_complex(s):
    a, b, c, d = split_string_to_ints(s)
    return make_complex_pair(a, b, c, d)

def split_string_to_ints(s):
    return map(int, s.split())

def make_complex_pair(a, b, c, d):
    return (make_complex(a, b), make_complex(c, d))

def make_complex(a, b):
    return a + b * 1j

def dot(c1, c2):
    return get_dot_real(c1, c2) + get_dot_imag(c1, c2)

def get_dot_real(c1, c2):
    return c1.real * c2.real

def get_dot_imag(c1, c2):
    return c1.imag * c2.imag

def cross(c1, c2):
    return get_cross_real(c1, c2) - get_cross_imag(c1, c2)

def get_cross_real(c1, c2):
    return c1.real * c2.imag

def get_cross_imag(c1, c2):
    return c1.imag * c2.real

def cross_point(p1, p2, p3, p4):
    crs1 = points_cross(p1, p2, p3)
    crs2 = points_cross(p1, p2, p4)
    if are_points_collinear(crs1, crs2):
        return cross_point_collinear_handler(p1, p2, p3, p4)
    return cross_point_noncollinear_handler(p1, p2, p3, p4, crs1, crs2)

def points_cross(p1, p2, p3):
    return cross(p2 - p1, p3 - p1)

def are_points_collinear(crs1, crs2):
    return crs1 == 0 and crs2 == 0

def cross_point_collinear_handler(p1, p2, p3, p4):
    if p1 == p3 or p1 == p4:
        return p1
    elif p2 == p3 or p2 == p4:
        return p2
    else:
        return None

def cross_point_noncollinear_handler(p1, p2, p3, p4, crs1, crs2):
    crs3 = points_cross(p3, p4, p1)
    crs4 = points_cross(p3, p4, p2)
    if crosses_intersect(crs1, crs2, crs3, crs4):
        return cross_point_calculate(p1, p2, p3, p4)
    else:
        return None

def crosses_intersect(crs1, crs2, crs3, crs4):
    return crs1 * crs2 <= 0 and crs3 * crs4 <= 0

def cross_point_calculate(p1, p2, p3, p4):
    base = p4 - p3
    hypo1 = p1 - p3
    hypo2 = p2 - p3
    d1 = abs(cross(base, hypo1)) / abs(base)
    d2 = abs(cross(base, hypo2)) / abs(base)
    return p1 + d1 / (d1 + d2) * (p2 - p1)

def contain(polygon):
    flag = False
    edge_pairs = get_polygon_edges(polygon)
    for a, b in edge_pairs:
        a, b = ensure_edge_order(a, b)
        if contains_helper(a, b):
            flag = not flag
    return flag

def get_polygon_edges(polygon):
    return zip(polygon[0:], polygon[1:] + [polygon[0]])

def ensure_edge_order(a, b):
    if a.imag > b.imag:
        return b, a
    return a, b

def contains_helper(a, b):
    return a.imag <= 0 and b.imag > 0 and cross(a, b) > 0

def complex_compare_key(c):
    return get_complex_compare_tuple(c)

def get_complex_compare_tuple(c):
    return (c.real, c.imag)

def complex_compare_key2(c):
    return c.real

def pos_phase(base, c1, c2):
    return adjust_phase(phase((c2 - base) / (c1 - base)))

from cmath import phase, pi

def adjust_phase(p):
    if p < 0:
        p += 2 * pi
    return p

def solve():
    import sys
    lines = read_all_lines(sys.stdin)
    from itertools import combinations
    process_lines(lines, combinations)

def read_all_lines(stdin):
    return stdin.readlines()

def process_lines(lines, combinations):
    while True:
        n = parse_int(lines[0])
        if n == 0:
            break
        edge_lines = get_edge_lines(lines, n)
        edges = create_edges(edge_lines)
        adj_edge_cp = create_empty_adj_edge_cp(n)
        adj_cross_point = create_empty_dict()
        process_edge_combinations(edges, combinations, adj_edge_cp, adj_cross_point)
        process_sorting_adj_edge_cp(adj_edge_cp)
        build_adjacency_cross_point(adj_edge_cp, adj_cross_point)
        branch_cut_operation(adj_cross_point)
        remove_empty_adjacents(adj_cross_point)
        if not polygon_trace_check(adj_cross_point):
            print("no")
        del lines[:1+n]

def parse_int(s):
    return int(s)

def get_edge_lines(lines, n):
    return lines[1:1+n]

def create_edges(edge_lines):
    return list(enumerate(map(string_to_complex, edge_lines)))

def create_empty_adj_edge_cp(n):
    return [[] for _ in range(n)]

def create_empty_dict():
    return {}

def process_edge_combinations(edges, combinations, adj_edge_cp, adj_cross_point):
    for e1, e2 in combinations(edges, 2):
        process_single_edge_pair(e1, e2, adj_edge_cp, adj_cross_point)

def process_single_edge_pair(e1, e2, adj_edge_cp, adj_cross_point):
    n1, t1 = e1
    n2, t2 = e2
    cp = cross_point(*t1, *t2)
    if cp:
        adj_edge_cp[n1].append(cp)
        adj_edge_cp[n2].append(cp)
        adj_cross_point[cp] = (n1, n2)

def process_sorting_adj_edge_cp(adj_edge_cp):
    for cp_list in adj_edge_cp:
        cp_list.sort(key=complex_compare_key)

def build_adjacency_cross_point(adj_edge_cp, adj_cross_point):
    for cp, t in list(adj_cross_point.items()):
        e1, e2 = t
        cp_l = get_adjacents_for_cross_point(cp, e1, e2, adj_edge_cp)
        adj_cross_point[cp] = cp_l

def get_adjacents_for_cross_point(cp, e1, e2, adj_edge_cp):
    cp_l = []
    add_adjacent_points(cp_l, cp, adj_edge_cp[e1])
    add_adjacent_points(cp_l, cp, adj_edge_cp[e2])
    return cp_l

def add_adjacent_points(cp_l, cp, edge_cp):
    if len(edge_cp) == 1:
        return
    if cp == edge_cp[0]:
        cp_l.append(edge_cp[1])
    elif cp == edge_cp[-1]:
        cp_l.append(edge_cp[-2])
    else:
        cp_idx = edge_cp.index(cp)
        cp_l.append(edge_cp[cp_idx - 1])
        cp_l.append(edge_cp[cp_idx + 1])

def branch_cut_operation(adj_cross_point):
    flag = True
    while flag:
        flag = branch_cut_iteration(adj_cross_point)

def branch_cut_iteration(adj_cross_point):
    for cp, cp_list in adj_cross_point.items():
        if len(cp_list) == 1:
            next_cp = cp_list.pop()
            adj_cross_point[next_cp].remove(cp)
            return True
    return False

def remove_empty_adjacents(adj_cross_point):
    del_cp_list = get_empty_cp_list(adj_cross_point)
    for cp in del_cp_list:
        del adj_cross_point[cp]

def get_empty_cp_list(adj_cross_point):
    return [cp for cp, cp_list in adj_cross_point.items() if not cp_list]

def polygon_trace_check(adj_cross_point):
    cp_list = build_cp_list_sorted(adj_cross_point)
    visited = build_visited_dict(cp_list)
    for start in cp_list:
        if start_path_failed(start):
            return False
        if was_visited_cp(visited, start):
            continue
        trace_result = trace_polygon(adj_cross_point, start, visited)
        if trace_result is not None:
            print(trace_result)
            return trace_result == "yes"
    return False

def build_cp_list_sorted(adj_cross_point):
    cp_list = list(adj_cross_point)
    cp_list.sort(key=complex_compare_key2)
    return cp_list

def build_visited_dict(cp_list):
    return dict(zip(cp_list, [False] * len(cp_list)))

def start_path_failed(start):
    return start.real >= 0

def was_visited_cp(visited, cp):
    return visited[cp]

def trace_polygon(adj_cross_point, start, visited):
    visited[start] = True
    path = [start - 1, start]
    while True:
        pre_cp = path[-2]
        cp = path[-1]
        ang = 2 * pi
        next_cp = None
        for p in adj_cross_point[cp]:
            if p == pre_cp:
                continue
            new_ang = pos_phase(cp, pre_cp, p)
            if new_ang < ang:
                next_cp = p
                ang = new_ang
        visited[next_cp] = True
        if next_cp == start:
            if contain(path[1:]):
                return "yes"
            else:
                break
        else:
            path.append(next_cp)
    return None

solve()