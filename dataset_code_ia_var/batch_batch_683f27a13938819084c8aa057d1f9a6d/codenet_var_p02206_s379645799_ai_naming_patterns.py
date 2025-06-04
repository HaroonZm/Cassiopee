num_items, upper_limit = map(int, input().split())

accepted_value, rejected_value = 0, upper_limit + 1
while rejected_value - accepted_value > 1:
    candidate_value = (accepted_value + rejected_value) // 2

    total_sum = 0
    current_value = candidate_value
    for index in range(num_items):
        total_sum += current_value
        current_value //= 2
        if current_value == 0:
            break

    if total_sum <= upper_limit:
        accepted_value = candidate_value
    else:
        rejected_value = candidate_value

print(accepted_value)