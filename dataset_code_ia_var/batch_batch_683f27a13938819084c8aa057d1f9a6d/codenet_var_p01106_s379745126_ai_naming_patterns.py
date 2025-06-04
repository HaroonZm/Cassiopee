while True:
    input_line = input()
    param_n, param_i, param_j = map(int, input_line.split())

    if param_n == 0:
        break

    fold_direction_list = [None for _ in range(param_n + 1)]

    total_partitions = 2 ** param_n
    current_fold = param_n
    current_index_vertical = param_i

    while True:
        if total_partitions == 1:
            assert current_fold == 0
            break

        half_partitions = total_partitions // 2
        if current_index_vertical <= half_partitions:
            fold_direction_list[current_fold] = 0
        else:
            fold_direction_list[current_fold] = 1

        current_fold -= 1
        total_partitions = half_partitions

        if half_partitions >= current_index_vertical:
            current_index_vertical = half_partitions - current_index_vertical + 1
        else:
            current_index_vertical = current_index_vertical - half_partitions

    total_partitions = 2 ** param_n
    current_index_horizontal = param_j
    result_sequence = ""

    for fold_index in range(1, param_n + 1):
        half_partitions = total_partitions // 2

        if current_index_horizontal <= half_partitions:
            is_right_half = 0
        else:
            is_right_half = 1

        direction_sum = fold_direction_list[fold_index] + is_right_half

        if direction_sum % 2 == 0:
            result_sequence += "L"
            if half_partitions >= current_index_horizontal:
                current_index_horizontal = half_partitions - current_index_horizontal + 1
            else:
                current_index_horizontal = current_index_horizontal - half_partitions
        else:
            result_sequence += "R"
            if half_partitions < current_index_horizontal:
                current_index_horizontal = total_partitions - current_index_horizontal + 1

        total_partitions = half_partitions

    print(result_sequence)