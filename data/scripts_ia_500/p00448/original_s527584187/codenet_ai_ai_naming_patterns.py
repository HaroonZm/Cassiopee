while True:
    input_line = input()
    if input_line == '0 0':
        break
    rows_count = int(input_line.split()[0])
    columns_binary_strings = [input().split() for _ in range(rows_count)]
    columns_values = [int(''.join(bits), 2) for bits in zip(*columns_binary_strings)]
    max_score = 0
    total_rows = rows_count
    for mask in range(1 << total_rows):
        current_score = 0
        for column_value in columns_values:
            differing_bits_count = bin(mask ^ column_value).count('1')
            if differing_bits_count > total_rows // 2:
                current_score += differing_bits_count
            else:
                current_score += total_rows - differing_bits_count
        if current_score > max_score:
            max_score = current_score
    print(max_score)