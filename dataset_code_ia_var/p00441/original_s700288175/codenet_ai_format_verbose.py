while True:

    number_of_points = input()

    if number_of_points == 0:
        break

    point_list = [tuple(map(int, raw_input().split())) for _ in range(number_of_points)]

    point_set = set(point_list)

    largest_square_side_squared = 0

    for first_point_index in range(number_of_points - 1):

        x_first, y_first = point_list[first_point_index]

        for second_point_index in range(first_point_index + 1, number_of_points):

            x_second, y_second = point_list[second_point_index]

            third_point = (x_second - y_second + y_first, y_second + x_second - x_first)
            fourth_point = (x_first - y_second + y_first, y_first + x_second - x_first)

            if third_point in point_set and fourth_point in point_set:

                square_side_squared = (x_first - x_second) ** 2 + (y_first - y_second) ** 2

                largest_square_side_squared = max(largest_square_side_squared, square_side_squared)

    print largest_square_side_squared