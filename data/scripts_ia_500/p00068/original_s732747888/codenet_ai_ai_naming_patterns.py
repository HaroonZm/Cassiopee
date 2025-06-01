import sys

def is_point_on_left_side(point1, point2, points_list):
    global points_sorted
    y1, x1 = point1
    dy = point2[0] - y1
    dx = point2[1] - x1
    for point3 in points_sorted[::-1]:
        if point1 == point3 or point2 == point3:
            continue
        elif (point3[1] - x1) * dy - dx * (point3[0] - y1) < 0:
            return False
    return True

while True:
    n_points = input()
    if n_points == 0:
        break
    n_points = int(n_points)
    points_sorted = sorted([list(map(int, input().split())) for _ in range(n_points)])
    start_point = current_point = points_sorted[0]
    remaining_points = points_sorted[:]
    while True:
        for next_point in remaining_points:
            if current_point != next_point and is_point_on_left_side(current_point, next_point, points_sorted):
                break
        current_point = next_point
        remaining_points.remove(next_point)
        if next_point == start_point:
            break
    print(len(remaining_points))