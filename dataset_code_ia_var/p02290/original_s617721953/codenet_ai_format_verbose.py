from math import hypot

first_point_x, first_point_y, second_point_x, second_point_y = map(int, input().split())

vector_x_difference = second_point_x - first_point_x
vector_y_difference = second_point_y - first_point_y

main_vector_length = hypot(vector_x_difference, vector_y_difference)

number_of_projections = int(input())

for projection_index in range(number_of_projections):

    projection_point_x, projection_point_y = map(int, input().split())

    scalar_projection_coefficient = (
        (projection_point_x - first_point_x) * vector_x_difference +
        (projection_point_y - first_point_y) * vector_y_difference
    ) / (main_vector_length ** 2)

    projected_x_coordinate = first_point_x + vector_x_difference * scalar_projection_coefficient
    projected_y_coordinate = first_point_y + vector_y_difference * scalar_projection_coefficient

    print(projected_x_coordinate, projected_y_coordinate)