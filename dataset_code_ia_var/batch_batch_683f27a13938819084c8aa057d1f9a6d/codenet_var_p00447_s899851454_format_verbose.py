def find_translation_vector_for_first_list_size(number_of_first_list_points):

    first_list_of_points = sorted(
        [list(map(int, input().split())) for _ in range(int(number_of_first_list_points))],
        key=lambda coordinate_pair: coordinate_pair[0]
    )

    number_of_second_list_points = int(input())

    second_list_of_points = sorted(
        [list(map(int, input().split())) for _ in range(number_of_second_list_points)],
        key=lambda coordinate_pair: coordinate_pair[0]
    )

    for second_list_x, second_list_y in second_list_of_points:

        first_list_first_x, first_list_first_y = first_list_of_points[0]

        translation_x = second_list_x - first_list_first_x
        translation_y = second_list_y - first_list_first_y

        for point_x, point_y in first_list_of_points:

            translated_point = [point_x + translation_x, point_y + translation_y]

            if translated_point not in second_list_of_points:
                break

        else:
            print(translation_x, translation_y)
            return

for first_list_size_input in iter(input, '0'):
    find_translation_vector_for_first_list_size(first_list_size_input)