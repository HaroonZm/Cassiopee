import operator

for pattern_entry_count in iter(input, '0'):
    normalized_targets = [[*map(int, input().split())] for _ in [0] * int(pattern_entry_count)]
    min_x, min_y = min(normalized_targets)
    normalized_targets = {(x - min_x, y - min_y) for x, y in normalized_targets}
    normalized_targets_max_x = max(coord[0] for coord in normalized_targets)
    background_entry_count = int(input())
    background_coords = {tuple(map(int, input().split())) for _ in [0] * background_entry_count}
    background_max_x = max(operator.itemgetter(0)(coord) for coord in background_coords)
    x_shift_limit = background_max_x - normalized_targets_max_x
    for bg_x, bg_y in background_coords:
        if bg_x > x_shift_limit:
            continue
        for norm_x, norm_y in normalized_targets:
            shifted_coord = (bg_x + norm_x, bg_y + norm_y)
            if shifted_coord not in background_coords:
                break
        else:
            print(bg_x - min_x, bg_y - min_y)
            break