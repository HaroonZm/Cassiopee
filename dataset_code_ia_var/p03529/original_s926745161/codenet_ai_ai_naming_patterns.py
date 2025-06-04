total_stones, selection_limit = map(int, input().split())
modulus_value = 10**9 + 7
state_count = [0] * 3300
state_count[0] = 1

for stone_value in range(total_stones, 0, -1):
    next_state_count = [0] * 3300
    for selection_count in range(selection_limit + 1):
        for previous_sum in range(3300):
            if stone_value < selection_count:
                next_state_count[previous_sum] += state_count[previous_sum]
                next_state_count[previous_sum] %= modulus_value
            elif (previous_sum + selection_count) // stone_value + previous_sum < 3300:
                increment = (previous_sum + selection_count) // stone_value
                next_state_count[previous_sum + increment] += state_count[previous_sum]
                next_state_count[previous_sum + increment] %= modulus_value
    state_count = next_state_count

final_answer = selection_limit * (selection_limit + 1) // 2
final_answer = final_answer * pow(selection_limit + 1, total_stones - 1, modulus_value)
final_answer = final_answer * total_stones % modulus_value

for sum_index in range(3300):
    final_answer -= state_count[sum_index] * sum_index
    final_answer %= modulus_value
print(final_answer)