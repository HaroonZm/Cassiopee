while True:

    number_of_target_points = int(input())

    if number_of_target_points == 0:
        break

    target_points_list = [
        tuple(map(int, input().split()))
        for _ in range(number_of_target_points)
    ]

    min_target_x, min_target_y = min(target_points_list)

    normalized_target_points = {
        (x - min_target_x, y - min_target_y)
        for x, y in target_points_list
    }

    number_of_sky_points = int(input())

    sky_points_set = {
        tuple(map(int, input().split()))
        for _ in range(number_of_sky_points)
    }

    sorted_sky_points = sorted(sky_points_set)

    for candidate_sky_x, candidate_sky_y in sorted_sky_points:

        for normalized_dx, normalized_dy in normalized_target_points:

            shifted_point = (candidate_sky_x + normalized_dx, candidate_sky_y + normalized_dy)

            if shifted_point not in sky_points_set:
                break

        else:
            print(candidate_sky_x - min_target_x, candidate_sky_y - min_target_y)
            break