import sys
from collections import deque
import itertools as it

def set_recursion_limit():
    sys.setrecursionlimit(1000000)

def get_input():
    return input()

def parse_line():
    return list(map(int, raw_input().split()))

def append_rectangle_info(lst, x_lst, y_lst, rect):
    l, t, r, b = rect
    lst.append((l, t, r, b))
    x_lst.extend([l, r])
    y_lst.extend([t, b])

def get_unique_sorted_list(lst):
    return sorted(list(set(lst)))

def create_coord_map(lst):
    coord_map = {}
    for i in range(len(lst)):
        coord_map[lst[i]] = 2 * i + 1
    return coord_map

def mark_rectangle_edges(lst, mx, my, wall):
    for sq in lst:
        mark_edges_of_one_rect(sq, mx, my, wall)

def mark_edges_of_one_rect(sq, mx, my, wall):
    sx = mx[sq[0]]
    gx = mx[sq[2]]
    sy = my[sq[3]]
    gy = my[sq[1]]
    mark_horizontal_edges(sx, gx, sy, gy, wall)
    mark_vertical_edges(sx, gx, sy, gy, wall)

def mark_horizontal_edges(sx, gx, sy, gy, wall):
    for x in range(sx, gx + 1):
        wall[(x, sy)] = 1
        wall[(x, gy)] = 1

def mark_vertical_edges(sx, gx, sy, gy, wall):
    for y in range(sy, gy + 1):
        wall[(sx, y)] = 1
        wall[(gx, y)] = 1

def flood_fill(x, y, wall, n):
    if not is_valid_cell(x, y, wall, n):
        return
    wall[(x, y)] = 1
    for nx, ny in get_neighbors(x, y):
        flood_fill(nx, ny, wall, n)

def is_valid_cell(x, y, wall, n):
    if (x, y) in wall:
        return False
    if x < 0 or y < 0 or x > 5 * n or y > 5 * n:
        return False
    return True

def get_neighbors(x, y):
    return [
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1)
    ]

def count_regions(n, wall):
    ans = 0
    for y in range(5 * n):
        for x in range(5 * n):
            if (x, y) not in wall:
                ans += 1
                flood_fill(x, y, wall, n)
    return ans

def process_single_case(n):
    lst, x_lst, y_lst = [], [], []
    for _ in range(n):
        rect = parse_line()
        append_rectangle_info(lst, x_lst, y_lst, rect)

    x_lst_sorted = get_unique_sorted_list(x_lst)
    y_lst_sorted = get_unique_sorted_list(y_lst)
    mx = create_coord_map(x_lst_sorted)
    my = create_coord_map(y_lst_sorted)
    wall = {}
    mark_rectangle_edges(lst, mx, my, wall)
    ans = count_regions(n, wall)
    print_result(ans)

def print_result(ans):
    print ans

def main_loop():
    set_recursion_limit()
    while True:
        n = int(get_input())
        if n == 0:
            break
        process_single_case(n)

main_loop()