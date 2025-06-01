import sys

def is_point_left_of_line(point_a, point_b, point_c):
    y_a, x_a = point_a
    y_b, x_b = point_b
    y_c, x_c = point_c
    return (x_c - x_a) * (y_b - y_a) - (x_b - x_a) * (y_c - y_a) > 0

while True:
    input_line = input()
    if input_line == '0':
        break
    num_points = int(input_line)
    points_sorted = sorted([list(input()) for _ in range(num_points)])
    current_point = points_sorted[0]
    remaining_points = points_sorted[:]

    while True:
        found_next_point = False
        for candidate_point in remaining_points:
            if current_point == candidate_point:
                continue
            side_counts = [0, 0]
            for test_point in points_sorted[::-1]:
                if test_point == current_point or test_point == candidate_point:
                    continue
                side_counts[is_point_left_of_line(current_point, candidate_point, test_point)] += 1
            if side_counts[0] == 0:
                next_point = candidate_point
                found_next_point = True
                break
        if not found_next_point:
            break

        current_point = next_point
        remaining_points.remove(next_point)
        if next_point == points_sorted[0]:
            break

    print(len(remaining_points))