for entry_count_str in iter(input, '0'):
    shape_list = [[*map(int, input().split())] for _ in [0] * int(entry_count_str)]
    shape_min_x, shape_min_y = min(shape_list)
    stamp_set = {tuple(map(int, input().split())) for _ in [0] * int(input())}
    placement_offset_x = max(stamp_set)[0] - max(shape_list)[0] + shape_min_x
    for stamp_x, stamp_y in stamp_set:
        if stamp_x <= placement_offset_x:
            for cell_x, cell_y in shape_list:
                if (stamp_x + cell_x - shape_min_x, stamp_y + cell_y - shape_min_y) not in stamp_set:
                    break
            else:
                print(stamp_x - shape_min_x, stamp_y - shape_min_y)
                break