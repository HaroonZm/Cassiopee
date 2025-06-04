number_of_points = input()

points_coordinates = [map(int, raw_input().split()) for point_index in range(number_of_points)]

for point_index in range(number_of_points):
    current_x = points_coordinates[point_index][0]
    current_y = points_coordinates[point_index][1]
    points_coordinates[point_index][0] = -current_y
    points_coordinates[point_index][1] = current_x

points_coordinates.sort()

minimum_point_x = points_coordinates[0][1]
minimum_point_y = -points_coordinates[0][0]

print minimum_point_x, minimum_point_y