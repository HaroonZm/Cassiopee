import sys
sys.setrecursionlimit(10**9)
standard_input = sys.stdin.readline

def main_process():
    polygon_testcase_count = int(standard_input())
    if polygon_testcase_count == 0:
        exit()
    reference_polygon_vertex_count = int(standard_input())
    reference_polygon_points = [list(map(int, standard_input().split())) for _ in range(reference_polygon_vertex_count)]

    candidate_polygons_list = []
    for _ in range(polygon_testcase_count):
        candidate_vertex_count = int(standard_input())
        candidate_polygons_list.append([list(map(int, standard_input().split())) for _ in range(candidate_vertex_count)])

    matching_polygons_indices = []
    for candidate_index, candidate_polygon in enumerate(candidate_polygons_list):
        if polygon_identity_check(reference_polygon_points, candidate_polygon):
            matching_polygons_indices.append(candidate_index + 1)

    if matching_polygons_indices:
        print("\n".join(map(str, matching_polygons_indices)))
    print("+++++")

def polygon_identity_check(polygon_a, polygon_b):
    if len(polygon_a) != len(polygon_b):
        return False

    polygon_a_turn_pattern = calculate_turn_pattern(polygon_a)
    polygon_a_distance_pattern = calculate_distance_pattern(polygon_a)

    polygon_b_turn_pattern = calculate_turn_pattern(polygon_b)
    polygon_b_distance_pattern = calculate_distance_pattern(polygon_b)
    if all(turn_a == turn_b for turn_a, turn_b in zip(polygon_b_turn_pattern, polygon_a_turn_pattern)) and \
       all(dist_a == dist_b for dist_a, dist_b in zip(polygon_b_distance_pattern, polygon_a_distance_pattern)):
        return True

    polygon_b_reversed_turn_pattern = calculate_turn_pattern(list(reversed(polygon_b)))
    polygon_b_reversed_distance_pattern = calculate_distance_pattern(list(reversed(polygon_b)))
    if all(turn_a == turn_b for turn_a, turn_b in zip(polygon_b_reversed_turn_pattern, polygon_a_turn_pattern)) and \
       all(dist_a == dist_b for dist_a, dist_b in zip(polygon_b_reversed_distance_pattern, polygon_a_distance_pattern)):
        return True

    return False

def calculate_distance(point_a, point_b):
    return sum(abs(coord_a - coord_b) for coord_a, coord_b in zip(point_a, point_b))

def calculate_distance_pattern(polygon_points_sequence):
    return [calculate_distance(point_prev, point_next) for point_prev, point_next in zip(polygon_points_sequence, polygon_points_sequence[1:])]

def calculate_turn_type(point_prev, point_current, point_next):
    if point_prev[0] == point_current[0]:
        if point_prev[1] < point_current[1]:
            if point_next[0] > point_current[0]:
                return 1
            else:
                return 0
        else:
            if point_next[0] > point_current[0]:
                return 0
            else:
                return 1
    else:
        if point_prev[0] < point_current[0]:
            if point_next[1] > point_current[1]:
                return 0
            else:
                return 1
        else:
            if point_next[1] > point_current[1]:
                return 1
            else:
                return 0

def calculate_turn_pattern(polygon_points_sequence):
    return [calculate_turn_type(point_a, point_b, point_c) for point_a, point_b, point_c in zip(polygon_points_sequence, polygon_points_sequence[1:], polygon_points_sequence[2:])]

while True:
    main_process()