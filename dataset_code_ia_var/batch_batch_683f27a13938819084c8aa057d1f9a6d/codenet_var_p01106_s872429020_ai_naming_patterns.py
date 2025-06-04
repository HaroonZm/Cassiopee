while True:
    num_levels, initial_value, position_index = map(int, input().split())
    if num_levels == 0:
        break
    level_values = [initial_value] * num_levels
    for level_idx in range(num_levels - 2, -1, -1):
        if level_values[level_idx + 1] <= 2 ** (level_idx + 1):
            level_values[level_idx] = 2 ** (level_idx + 1) - level_values[level_idx + 1] + 1
        else:
            level_values[level_idx] = level_values[level_idx + 1] - 2 ** (level_idx + 1)
    result_path = ""
    for step_idx in range(num_levels):
        threshold = 2 ** step_idx
        half_remaining = 2 ** (num_levels - step_idx - 1)
        if level_values[step_idx] > threshold:
            if position_index <= half_remaining:
                result_path += "R"
            else:
                result_path += "L"
                position_index -= half_remaining
        else:
            if position_index <= half_remaining:
                position_index = half_remaining - position_index + 1
                result_path += "L"
            else:
                position_index -= half_remaining
                position_index = half_remaining - position_index + 1
                result_path += "R"
    print(result_path)