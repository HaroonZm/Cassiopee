while True:

    number_of_points_set_p = input()

    if number_of_points_set_p == 0:
        break

    points_set_p = set(
        [
            tuple(map(int, raw_input().split()))
            for point_index in range(number_of_points_set_p)
        ]
    )

    number_of_points_set_q = input()

    points_set_q = set(
        [
            tuple(map(int, raw_input().split()))
            for point_index in xrange(number_of_points_set_q)
        ]
    )

    has_found_translation = False

    for point_p_x, point_p_y in points_set_p:

        if has_found_translation:
            break

        for point_q_x, point_q_y in points_set_q:

            if has_found_translation:
                break

            translation_dx = point_q_x - point_p_x
            translation_dy = point_q_y - point_p_y

            for current_x, current_y in points_set_p:

                mapped_x = current_x + translation_dx
                mapped_y = current_y + translation_dy

                if (mapped_x, mapped_y) not in points_set_q:
                    break

            else:
                print translation_dx, translation_dy
                has_found_translation = True