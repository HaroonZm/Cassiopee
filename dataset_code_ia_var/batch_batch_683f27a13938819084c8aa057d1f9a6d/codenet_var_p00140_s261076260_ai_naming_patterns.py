input_count = int(input())

for iteration_index in range(input_count):
    range_start, range_end = map(int, input().split())

    result_sequence = []
    if range_start <= 5:
        if range_start > range_end:
            [result_sequence.append(current_value) for current_value in range(range_start, range_end - 1, -1)]
        else:
            [result_sequence.append(current_value) for current_value in range(range_start, range_end + 1)]
    elif range_start < range_end:
        [result_sequence.append(current_value) for current_value in range(range_start, range_end + 1)]
    else:
        [result_sequence.append(current_value) for current_value in range(range_start, 10)]
        if range_end <= 5:
            [result_sequence.append(current_value) for current_value in range(5, range_end - 1, -1)]
        else:
            [result_sequence.append(current_value) for current_value in range(5, 0, -1)]
            [result_sequence.append(current_value) for current_value in range(0, range_end + 1)]

    print(' '.join(str(sequence_value) for sequence_value in result_sequence))