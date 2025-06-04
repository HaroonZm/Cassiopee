row_count, col_count = map(int, input().split())
min_steps = [0] + [300] * col_count
for row_index in range(row_count):
    row_string = input()
    if row_index == 0:
        target_char = row_string[0]
    for col_index in range(col_count):
        is_target = row_string[col_index] == target_char
        flip_needed = is_target ^ (min_steps[col_index] % 2 == 0)
        min_steps[col_index] += flip_needed
        if col_index > 0:
            prev_flip_needed = is_target ^ (min_steps[col_index - 1] % 2 == 0)
            min_steps[col_index] = min(min_steps[col_index], min_steps[col_index - 1] + prev_flip_needed)
final_result = (min_steps[-2] + (target_char == "#") + 1) // 2
print(final_result)