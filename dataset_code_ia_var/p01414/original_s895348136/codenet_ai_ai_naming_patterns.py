def solve_problem():
    from sys import stdin as input_stream
    from itertools import combinations as combine_pairs

    cell_count = int(input_stream.readline())
    cell_dimensions = [tuple(map(int, input_stream.readline().split())) for _ in range(cell_count)]
    target_iter = (line.rstrip() for line in input_stream)
    target_string = ''.join(target_iter)

    red_mask = 0
    green_mask = 0
    blue_mask = 0
    shift_value = 1
    for char in target_string[:]:
        if char == 'R':
            red_mask += shift_value
        elif char == 'G':
            green_mask += shift_value
        else:
            blue_mask += shift_value
        shift_value <<= 1

    color_masks = (red_mask, green_mask, blue_mask)
    goal_mask = (1 << 16) - 1

    stamp_candidates = []
    for row_start, row_end in combine_pairs(range(5), 2):
        row_width = row_end - row_start
        for col_start, col_end in combine_pairs(range(5), 2):
            col_width = col_end - col_start
            for pattern_height, pattern_width in cell_dimensions:
                valid_shape = (
                    (row_width == pattern_height and col_width == pattern_width)
                    or ((row_start == 0 or row_end == 4) and row_width < pattern_height and col_width == pattern_width)
                    or ((col_start == 0 or col_end == 4) and col_width < pattern_width and row_width == pattern_height)
                    or ((row_start == 0 or row_end == 4) and (col_start == 0 or col_end == 4) and row_width < pattern_height and col_width < pattern_width)
                )
                if valid_shape:
                    mask_value = 1
                    for _ in range(col_width - 1):
                        mask_value <<= 1
                        mask_value += 1
                    mask_value <<= col_start
                    row_mask = mask_value
                    for _ in range(row_width - 1):
                        mask_value <<= 4
                        mask_value += row_mask
                    mask_value <<= (row_start * 4)
                    for single_color_mask in color_masks:
                        stamp_bits = single_color_mask & mask_value
                        if stamp_bits:
                            stamp_candidates.append((mask_value ^ goal_mask, stamp_bits))
                    break

    state_queue = [0]
    visited_states = [False] * (2 ** 16)
    visited_states[0] = True
    step_counter = 0
    while True:
        current_queue = state_queue[:]
        state_queue = []
        step_counter += 1
        for current_state in current_queue:
            for stamp_mask, stamp_color in stamp_candidates:
                next_state = current_state & stamp_mask | stamp_color
                if visited_states[next_state]:
                    continue
                if next_state == goal_mask:
                    return step_counter
                visited_states[next_state] = True
                state_queue.append(next_state)

print(solve_problem())