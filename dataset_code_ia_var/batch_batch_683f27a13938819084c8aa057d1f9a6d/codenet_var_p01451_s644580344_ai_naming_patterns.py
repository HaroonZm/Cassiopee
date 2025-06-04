import sys
import math
import heapq

input_stream = sys.stdin.buffer
output_stream = sys.stdout

def read_line():
    return input_stream.readline()

def write_output(text):
    output_stream.write(text)

num_points_P, num_points_Q = map(int, read_line().split())
points_P_list = [list(map(int, read_line().split())) for _ in range(num_points_P)]
points_Q_list = [list(map(int, read_line().split())) for _ in range(num_points_Q)]

def compute_dot_product_3_points(origin, point_a, point_b):
    origin_x, origin_y = origin
    a_x, a_y = point_a
    b_x, b_y = point_b
    return (a_x - origin_x) * (b_x - origin_x) + (a_y - origin_y) * (b_y - origin_y)

def compute_cross_product_3_points(origin, point_a, point_b):
    origin_x, origin_y = origin
    a_x, a_y = point_a
    b_x, b_y = point_b
    return (a_x - origin_x) * (b_y - origin_y) - (b_x - origin_x) * (a_y - origin_y)

def compute_squared_distance(point_x, point_y):
    x1, y1 = point_x
    x2, y2 = point_y
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

def check_segment_intersection(p_start, p_end, q_start, q_end):
    cross_p_qstart = compute_cross_product_3_points(p_start, p_end, q_start)
    cross_p_qend = compute_cross_product_3_points(p_start, p_end, q_end)
    cross_q_pstart = compute_cross_product_3_points(q_start, q_end, p_start)
    cross_q_pend = compute_cross_product_3_points(q_start, q_end, p_end)
    if cross_p_qstart == 0 and cross_p_qend == 0:
        dot_e0 = compute_dot_product_3_points(p_start, p_end, q_start)
        dot_e1 = compute_dot_product_3_points(p_start, p_end, q_end)
        if not (dot_e0 < dot_e1):
            dot_e0, dot_e1 = dot_e1, dot_e0
        return dot_e0 <= compute_squared_distance(p_start, p_end) and 0 <= dot_e1
    return cross_p_qstart * cross_p_qend <= 0 and cross_q_pstart * cross_q_pend <= 0

def compute_path_candidates(num_points, segment_points, query_point_start, query_point_end):
    yield 10 ** 18
    seg_point_start = segment_points[0]
    seg_point_end = segment_points[1]
    if not check_segment_intersection(seg_point_start, seg_point_end, query_point_start, query_point_end):
        yield math.sqrt(compute_squared_distance(seg_point_start, seg_point_end))
        return
    valid_indices_start = [idx for idx in range(2, num_points) if not check_segment_intersection(seg_point_start, segment_points[idx], query_point_start, query_point_end)]
    valid_indices_end = [idx for idx in range(2, num_points) if not check_segment_intersection(seg_point_end, segment_points[idx], query_point_start, query_point_end)]
    distance_from_start = [math.sqrt(compute_squared_distance(seg_point_start, segment_points[idx])) for idx in range(num_points)]
    distance_from_end = [math.sqrt(compute_squared_distance(seg_point_end, segment_points[idx])) for idx in range(num_points)]
    for idx_start in valid_indices_start:
        for idx_end in valid_indices_end:
            if idx_start != idx_end:
                if check_segment_intersection(segment_points[idx_start], segment_points[idx_end], query_point_start, query_point_end):
                    continue
                yield distance_from_start[idx_start] + distance_from_end[idx_end] + math.sqrt(compute_squared_distance(segment_points[idx_start], segment_points[idx_end]))
            else:
                yield distance_from_start[idx_start] + distance_from_end[idx_end]

final_result = min(
    math.sqrt(compute_squared_distance(points_Q_list[0], points_Q_list[1])) + min(compute_path_candidates(num_points_P, points_P_list, points_Q_list[0], points_Q_list[1])),
    math.sqrt(compute_squared_distance(points_P_list[0], points_P_list[1])) + min(compute_path_candidates(num_points_Q, points_Q_list, points_P_list[0], points_P_list[1]))
)
if final_result < 10 ** 9:
    write_output("%.16f\n" % final_result)
else:
    write_output("-1\n")