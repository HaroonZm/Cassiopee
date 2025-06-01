while True:
    input_line = input()
    if input_line == '0 0':
        break
    rows_count = int(input_line.split()[0])
    binary_strings = [input().split() for _ in range(rows_count)]
    columns_decoded = [int(''.join(bits), 2) for bits in zip(*binary_strings)]
    max_score = 0
    max_mask_value = 1 << rows_count
    mask_flags = [1] * max_mask_value
    for mask in range(max_mask_value):
        if mask_flags[mask]:
            mask_flags[~mask & (max_mask_value - 1)] = 0
            current_score = 0
            for col_value in columns_decoded:
                diff_bits = bin(mask ^ col_value).count('1')
                current_score += diff_bits if diff_bits > rows_count // 2 else rows_count - diff_bits
            if current_score > max_score:
                max_score = current_score
    print(max_score)