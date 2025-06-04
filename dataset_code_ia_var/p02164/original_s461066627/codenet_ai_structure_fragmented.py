from math import atan2, degrees
from itertools import permutations

def read_num_points():
    return int(input())

def read_points(n):
    return [read_point() for _ in range(n)]

def read_point():
    return list(map(int, input().split()))

def angle_between_points(x0, y0, x1, y1):
    return degrees(atan2(y1 - y0, x1 - x0))

def normalize_delta(deg1, deg2):
    delta = deg1 - deg2
    if delta < 0:
        delta += 360
    if delta > 180:
        delta = 360 - delta
    return delta

def compute_total_angle_for_order(order):
    total_angle = 0
    prev_x, prev_y = 0, 0
    prev_deg = 0
    points = list(order) + [[0, 0]]
    for point in points:
        x, y = point
        curr_deg = angle_between_points(prev_x, prev_y, x, y)
        delta = normalize_delta(prev_deg, curr_deg)
        total_angle += delta
        prev_x, prev_y = x, y
        prev_deg = curr_deg
    return total_angle

def calculate_minimal_angle(points):
    min_angle = float("inf")
    for order in permutations(points):
        total_angle = compute_total_angle_for_order(order)
        if total_angle < min_angle:
            min_angle = total_angle
    return min_angle

def main():
    n = read_num_points()
    points = read_points(n)
    result = calculate_minimal_angle(points)
    print(result)

main()