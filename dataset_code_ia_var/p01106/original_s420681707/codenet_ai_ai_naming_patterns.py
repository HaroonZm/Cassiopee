while True:
    seg_count, start_pos, target_pos = map(int, input().split())
    if seg_count == 0:
        break
    curr_history = [start_pos]
    seg_size = 2 ** seg_count
    for idx in range(seg_count):
        last_pos = curr_history[-1]
        quarter = seg_size // 4
        half = seg_size // 2
        three_quarters = 3 * quarter
        if 1 <= last_pos <= quarter:
            curr_history.append(quarter + quarter - last_pos + 1)
        elif quarter + 1 <= last_pos <= half:
            curr_history.append(half - last_pos + 1)
        elif half + 1 <= last_pos <= three_quarters:
            curr_history.append(last_pos - half)
        else:
            curr_history.append(last_pos - three_quarters + quarter)
        seg_size //= 2
    curr_history = curr_history[::-1]
    seg_size = 2 ** seg_count
    movement_seq = ''
    for depth in range(seg_count):
        half = seg_size // 2
        curr_history_next = curr_history[depth + 1]
        bit_mask = 2 ** (depth + 1) // 2
        if 1 <= target_pos <= half:
            if curr_history_next <= bit_mask:
                target_pos = half - target_pos + 1
                movement_seq += 'L'
            else:
                movement_seq += 'R'
        else:
            if curr_history_next <= bit_mask:
                target_pos = seg_size - target_pos + 1
                movement_seq += 'R'
            else:
                target_pos -= half
                movement_seq += 'L'
        seg_size //= 2
    print(movement_seq)