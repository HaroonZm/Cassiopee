number_of_items, target_height, max_single_height = map(int, input().split())
modulo = 10**9 + 7

factorials = [1]
cumulative_factorials = [0]  # Will store cumulative sums of factorials from 1! to N!

for current_value in range(1, number_of_items + 1):
    next_factorial = (factorials[-1] * current_value) % modulo
    factorials.append(next_factorial)
    updated_cumulative = (cumulative_factorials[-1] + next_factorial) % modulo
    cumulative_factorials.append(updated_cumulative)

ways_to_reach_height = [0] * (target_height + 1)
cumulative_ways = [0] * (target_height + 1)
ways_to_reach_height[0] = 1
cumulative_ways[0] = 1

for current_height in range(1, target_height + 1):
    total_ways = cumulative_ways[current_height - 1]
    if current_height > max_single_height:
        total_ways -= cumulative_ways[current_height - max_single_height - 1]
    total_ways *= cumulative_factorials[number_of_items]
    total_ways %= modulo
    ways_to_reach_height[current_height] = total_ways
    cumulative_ways[current_height] = (cumulative_ways[current_height - 1] + total_ways) % modulo

final_answer = ways_to_reach_height[target_height]
final_answer *= factorials[number_of_items]
final_answer %= modulo
final_answer *= pow(cumulative_factorials[number_of_items], modulo - 2, modulo)
final_answer %= modulo

print(final_answer)