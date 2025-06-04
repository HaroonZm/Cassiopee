import sys

def set_recursion_limit():
    sys.setrecursionlimit(1000000)

def read_input():
    return int(input())

def read_rectangle_data(n):
    rects = []
    for _ in range(n):
        rects.append(tuple(map(int, input().split())))
    return rects

def build_points_and_dic(rects):
    points = []
    dic = {}
    for idx, (a, b, x, y) in enumerate(rects):
        dic[(a, b, idx)] = 0
        dic[(x, y, idx)] = 1
        points.append((a, b, idx))
        points.append((x, y, idx))
    return points, dic

def sort_points(points):
    return sorted(points)

def fill_plane_indices(plane, points, dic):
    points_sorted = sort_points(points)
    p = 0
    for i in range(len(points_sorted)):
        idx = points_sorted[i][2]
        pos = 0 if dic[points_sorted[i]] == 0 else 2
        plane[idx][pos] = p
        if i + 1 < len(points_sorted) and points_sorted[i][0] == points_sorted[i + 1][0]:
            continue
        else:
            p += 1

def sort_points_by_y(points):
    return sorted(points, key=lambda q: q[1])

def fill_plane_indices_y(plane, points, dic):
    points_sorted = sort_points_by_y(points)
    p = 0
    for i in range(len(points_sorted)):
        idx = points_sorted[i][2]
        pos = 1 if dic[points_sorted[i]] == 0 else 3
        plane[idx][pos] = p
        if i + 1 < len(points_sorted) and points_sorted[i][1] == points_sorted[i + 1][1]:
            continue
        else:
            p += 1

def create_plane(n):
    return [[-1, -1, -1, -1] for _ in range(n)]

def init_grid(n):
    size = n * 4 + 2
    return [[0 for _ in range(size)] for _ in range(size)]

def fill_edges_on_grid(m, plane, n):
    for p in plane:
        fill_horizontal_edges(m, p)
        fill_vertical_edges(m, p)

def fill_horizontal_edges(m, p):
    for j in range((p[1] - p[3]) * 2 + 1):
        m[p[0] * 2 + 1][p[3] * 2 + j + 1] = 1
        m[p[2] * 2 + 1][p[3] * 2 + j + 1] = 1

def fill_vertical_edges(m, p):
    for j in range((p[2] - p[0]) * 2 + 1):
        m[p[0] * 2 + j + 1][p[3] * 2 + 1] = 1
        m[p[0] * 2 + j + 1][p[1] * 2 + 1] = 1

def grid_dimensions(n):
    return n * 4 + 2

def safe_check(i, j, m, n):
    if m[i][j] == 0:
        m[i][j] = -1
        if i + 1 < grid_dimensions(n):
            safe_check(i + 1, j, m, n)
        if i - 1 >= 0:
            safe_check(i - 1, j, m, n)
        if j + 1 < grid_dimensions(n):
            safe_check(i, j + 1, m, n)
        if j - 1 >= 0:
            safe_check(i, j - 1, m, n)

def count_connected_components(m, n):
    ans = 0
    for i in range(grid_dimensions(n)):
        for j in range(grid_dimensions(n)):
            if m[i][j] == 0:
                ans += 1
                safe_check(i, j, m, n)
    return ans

def process_test_case(n):
    rects = read_rectangle_data(n)
    points, dic = build_points_and_dic(rects)
    plane = create_plane(n)
    fill_plane_indices(plane, points, dic)
    fill_plane_indices_y(plane, points, dic)
    m = init_grid(n)
    fill_edges_on_grid(m, plane, n)
    return count_connected_components(m, n)

def main():
    set_recursion_limit()
    while True:
        n = read_input()
        if n == 0:
            break
        res = process_test_case(n)
        print(res)

main()