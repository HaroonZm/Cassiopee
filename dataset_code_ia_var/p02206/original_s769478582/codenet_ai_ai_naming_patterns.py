num_items, max_sum = map(int, input().split())
lower_bound = 0
upper_bound = max_sum + 1

while upper_bound - lower_bound > 1:
    mid_value = (lower_bound + upper_bound) // 2
    current_sum = 0
    current_value = mid_value

    for idx in range(num_items):
        current_sum += current_value
        current_value //= 2
        if current_value == 0:
            break

    if current_sum <= max_sum:
        lower_bound = mid_value
    else:
        upper_bound = mid_value

print(lower_bound)