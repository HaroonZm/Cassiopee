import math
from itertools import combinations

number_of_points, number_of_dimensions = map(int, input().split())

def is_euclidean_distance_integer(point_a, point_b):
    squared_distance_sum = 0

    for coordinate_a, coordinate_b in zip(point_a, point_b):
        squared_distance_sum += (coordinate_a - coordinate_b) ** 2

    for possible_integer in range(1, squared_distance_sum + 1):
        if possible_integer ** 2 == squared_distance_sum:
            return 1

    return 0

points_list = []
for _ in range(number_of_points):
    point_coordinates = list(map(int, input().split()))
    points_list.append(point_coordinates)

all_index_pairs = combinations(range(number_of_points), 2)

count_of_integer_distances = 0
for index_point_one, index_point_two in all_index_pairs:
    if is_euclidean_distance_integer(points_list[index_point_one], points_list[index_point_two]):
        count_of_integer_distances += 1

print(count_of_integer_distances)