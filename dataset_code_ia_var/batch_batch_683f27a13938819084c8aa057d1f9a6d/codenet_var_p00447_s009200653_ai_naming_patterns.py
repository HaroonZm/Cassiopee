while True:
    num_targets = int(input())
    if num_targets == 0:
        break
    input_targets = [tuple(map(int, input().split())) for _ in range(num_targets)]
    base_x, base_y = min(input_targets)
    normalized_targets = {(tx - base_x, ty - base_y) for tx, ty in input_targets}

    num_sky_points = int(input())
    sky_points = {tuple(map(int, input().split())) for _ in range(num_sky_points)}
    sorted_sky_points = sorted(sky_points)

    for sky_x, sky_y in sorted_sky_points:
        for norm_dx, norm_dy in normalized_targets:
            if (sky_x + norm_dx, sky_y + norm_dy) not in sky_points:
                break
        else:
            print(sky_x - base_x, sky_y - base_y)
            break