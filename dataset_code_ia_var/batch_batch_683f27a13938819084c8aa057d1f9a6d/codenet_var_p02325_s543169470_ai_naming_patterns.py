import math
from typing import List, Tuple

def compute_distance(coord_pair_a: Tuple[int, int], coord_pair_b: Tuple[int, int]) -> float:
    delta_x = coord_pair_a[0] - coord_pair_b[0]
    delta_y = coord_pair_a[1] - coord_pair_b[1]
    return math.sqrt(delta_x ** 2 + delta_y ** 2)

if __name__ == "__main__":
    num_points = int(input())
    points_list: List[Tuple[int, int]] = [(0, 0)] * num_points
    for point_idx in range(num_points):
        coordinate_x, coordinate_y = map(int, input().split())
        points_list[point_idx] = (coordinate_x, coordinate_y)

    min_table_a = [float('inf')] * num_points
    min_table_b = [float('inf')] * num_points
    min_table_a[0] = min_table_b[0] = compute_distance(points_list[0], points_list[1])

    for curr_idx in range(2, num_points):
        curr_min_a = float('inf')
        curr_min_b = float('inf')
        for prev_idx in range(curr_idx - 1):
            inter_distance = compute_distance(points_list[curr_idx], points_list[prev_idx])
            curr_min_a = min(curr_min_a, min_table_b[prev_idx] + inter_distance)
            curr_min_b = min(curr_min_b, min_table_a[prev_idx] + inter_distance)
        min_table_a[curr_idx - 1] = curr_min_a
        min_table_b[curr_idx - 1] = curr_min_b
        consecutive_distance = compute_distance(points_list[curr_idx - 1], points_list[curr_idx])
        for update_idx in range(curr_idx - 1):
            min_table_a[update_idx] += consecutive_distance
            min_table_b[update_idx] += consecutive_distance

    final_result = min(
        min(temp_min_a, temp_min_b) + compute_distance(points_list[list_idx], points_list[num_points - 1])
        for list_idx, (temp_min_a, temp_min_b) in enumerate(zip(min_table_a, min_table_b))
    )
    print(final_result)