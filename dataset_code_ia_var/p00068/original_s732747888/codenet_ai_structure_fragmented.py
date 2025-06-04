import sys

def get_input():
    return input()

def parse_input(n):
    return [list(input()) for _ in range(n)]

def convert_input(val):
    return int(val)

def is_zero(n):
    return n == 0

def get_point_coordinates(point):
    return point[0], point[1]

def calculate_differences(p1, p2):
    y1, x1 = get_point_coordinates(p1)
    dy = p2[0] - y1
    dx = p2[1] - x1
    return y1, x1, dy, dx

def side_for_point(p1, p2, D):
    y1, x1, dy, dx = calculate_differences(p1, p2)
    for p3 in reversed(D):
        if is_same_point(p1, p3) or is_same_point(p2, p3):
            continue
        elif side_condition(p3, x1, y1, dx, dy):
            return False
    return True

def is_same_point(p1, p2):
    return p1 == p2

def side_condition(p3, x1, y1, dx, dy):
    return (p3[1] - x1) * dy - dx * (p3[0] - y1) < 0

def get_sorted_points(D):
    return sorted(D)

def get_first_point(D):
    return D[0]

def remove_point(D, p):
    D.remove(p)

def get_copy(D):
    return D[:]

def find_next_point(D1, p1, D):
    for p2 in D1:
        if not is_same_point(p1, p2) and side_for_point(p1, p2, D):
            return p2
    return None

def convex_hull_points(D):
    p = p1 = get_first_point(D)
    D1 = get_copy(D)
    while True:
        p2 = find_next_point(D1, p1, D)
        p1 = p2
        remove_point(D1, p2)
        if is_same_point(p2, p):
            break
    return len(D1)

def main_loop():
    while True:
        n = get_input()
        n = convert_input(n)
        if is_zero(n):
            break
        D = parse_input(n)
        D = get_sorted_points(D)
        print(convex_hull_points(D))

main_loop()