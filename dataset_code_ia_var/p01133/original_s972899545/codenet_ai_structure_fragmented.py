from math import sqrt
from sys import stdin

def read_input():
    return stdin

def parse_case_params(line):
    return map(int, line.split())

def parse_case_points(n, f_i):
    return [tuple(map(int, f_i.readline().split())) for _ in range(n)]

def compute_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def compute_all_distances(points):
    return tuple(tuple(compute_distance(p1, p2) for p2 in points) for p1 in points)

def compute_from_destination_distances(C, dx, dy):
    dest = (dx, dy)
    return tuple(compute_distance(c, dest) for c in C)

def update_next_candidates(remain, elapsed, adj, point, from_d):
    next_c = set()
    for c in remain:
        new_elapsed = elapsed + adj[point][c]
        if new_elapsed >= from_d[c]:
            return None, False
        next_c.add((c, new_elapsed))
    return next_c, True

def find_path(point, remain, elapsed, adj, from_d):
    if not remain:
        return True
    next_c, can_proceed = update_next_candidates(remain, elapsed, adj, point, from_d)
    if not can_proceed:
        return False
    for c, new_elapsed in next_c:
        remain.remove(c)
        if find_path(c, remain, new_elapsed, adj, from_d):
            return True
        remain.add(c)
    return False

def process_case(n, hx, hy, dx, dy, f_i):
    C = parse_case_points(n, f_i)
    from_d = compute_from_destination_distances(C, dx, dy)
    C_with_home = list(C)
    C_with_home.append((hx, hy))
    adj = compute_all_distances(C_with_home)
    start_idx = len(C)
    result = can_solve(start_idx, set(range(n)), adj, from_d)
    print("YES" if result else "NO")

def can_solve(start_idx, points, adj, from_d):
    return find_path(start_idx, points, 0, adj, from_d)

def should_break_case(n):
    return n == 0

def solve():
    f_i = read_input()
    while True:
        line = f_i.readline()
        if not line:
            break
        n, hx, hy, dx, dy = parse_case_params(line)
        if should_break_case(n):
            break
        process_case(n, hx, hy, dx, dy, f_i)

solve()