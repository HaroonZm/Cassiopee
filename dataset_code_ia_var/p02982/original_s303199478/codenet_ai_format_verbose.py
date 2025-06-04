import math

number_of_points, number_of_dimensions = map(int, input().split())

coordinates_list = []

number_of_integer_distance_pairs = 0

for point_index in range(number_of_points):
    point_coordinates = list(map(int, input().split()))
    coordinates_list.append(point_coordinates)

for first_point_index in range(number_of_points):
    for second_point_index in range(first_point_index + 1, number_of_points):

        squared_distance_sum = 0

        for dimension_index in range(number_of_dimensions):
            coordinate_difference = coordinates_list[second_point_index][dimension_index] - coordinates_list[first_point_index][dimension_index]
            squared_distance_sum += coordinate_difference ** 2

        euclidean_distance = math.sqrt(squared_distance_sum)

        if euclidean_distance == int(euclidean_distance):
            number_of_integer_distance_pairs += 1

print(number_of_integer_distance_pairs)