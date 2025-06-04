num_steps, max_value = map(int, input().split())
lower_bound, upper_bound = 0, max_value + 1
while upper_bound - lower_bound > 1:
    mid_value = (lower_bound + upper_bound) // 2
    total_sum = mid_value
    current_value = mid_value
    for step_idx in range(num_steps - 1):
        current_value //= 2
        total_sum += current_value
        if current_value == 0:
            break
    if total_sum > max_value:
        upper_bound = mid_value
    else:
        lower_bound = mid_value
print(lower_bound)