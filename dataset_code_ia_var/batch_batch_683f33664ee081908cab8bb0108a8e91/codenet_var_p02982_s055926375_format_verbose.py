from itertools import combinations

number_of_points, dimension_of_space = map(int, input().split())

coordinates_of_points = [
    list(map(int, input().split()))
    for _ in range(number_of_points)
]

count_of_integer_distances = 0

for first_point, second_point in combinations(coordinates_of_points, 2):

    squared_distance = 0

    for dimension_index in range(dimension_of_space):
        coordinate_difference = first_point[dimension_index] - second_point[dimension_index]
        squared_distance += coordinate_difference ** 2

    euclidean_distance = squared_distance ** 0.5

    if euclidean_distance % 1 == 0:
        count_of_integer_distances += 1

print(count_of_integer_distances)