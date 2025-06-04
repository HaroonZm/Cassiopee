number_of_points, dimensions = map(int, input().split())

points_coordinates = [ [] for point_index in range(number_of_points) ]

for point_index in range(number_of_points):
    points_coordinates[point_index] = list(map(int, input().split()))

count_of_integer_distances = 0

for first_point_index in range(number_of_points - 1):
    for second_point_index in range(first_point_index + 1, number_of_points):
        squared_distance_sum = 0

        for dimension_index in range(dimensions):
            coordinate_difference = points_coordinates[first_point_index][dimension_index] - points_coordinates[second_point_index][dimension_index]
            squared_distance_sum += coordinate_difference ** 2

        distance = squared_distance_sum ** 0.5

        if int(distance) ** 2 == squared_distance_sum:
            count_of_integer_distances += 1

print(count_of_integer_distances)