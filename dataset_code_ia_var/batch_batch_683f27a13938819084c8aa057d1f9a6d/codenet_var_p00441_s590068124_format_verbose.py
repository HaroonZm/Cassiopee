while True:
    number_of_poles = int(input())
    if number_of_poles == 0:
        break

    list_of_pole_coordinates = [
        tuple(map(int, input().split()))
        for _ in range(number_of_poles)
    ]

    set_of_pole_coordinates = set(list_of_pole_coordinates)

    maximum_square_area = 0

    for first_pole_index in range(number_of_poles):
        x_coordinate_first, y_coordinate_first = list_of_pole_coordinates[first_pole_index]

        for second_pole_index in range(first_pole_index, number_of_poles):
            x_coordinate_second, y_coordinate_second = list_of_pole_coordinates[second_pole_index]

            delta_x = x_coordinate_second - x_coordinate_first
            delta_y = y_coordinate_second - y_coordinate_first

            first_candidate_pole = (x_coordinate_second + delta_y, y_coordinate_second - delta_x)
            second_candidate_pole = (x_coordinate_first + delta_y, y_coordinate_first - delta_x)

            third_candidate_pole = (x_coordinate_second - delta_y, y_coordinate_second + delta_x)
            fourth_candidate_pole = (x_coordinate_first - delta_y, y_coordinate_first + delta_x)

            if (
                first_candidate_pole in set_of_pole_coordinates and
                second_candidate_pole in set_of_pole_coordinates
            ) or (
                third_candidate_pole in set_of_pole_coordinates and
                fourth_candidate_pole in set_of_pole_coordinates
            ):
                current_square_area = delta_x ** 2 + delta_y ** 2

                if current_square_area > maximum_square_area:
                    maximum_square_area = current_square_area

    print(maximum_square_area)