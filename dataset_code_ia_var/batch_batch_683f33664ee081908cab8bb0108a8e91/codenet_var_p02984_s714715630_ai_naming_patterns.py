input_count = int(input())
input_values = list(map(int, input().split()))
total_sum = sum(input_values)
values_length = len(input_values)
half_length = values_length // 2
even_index_sum = 0
for even_index in range(1, half_length + 1):
    even_index_sum += 2 * input_values[2 * (even_index - 1)]
second_value = total_sum - even_index_sum
first_value = input_values[-1] * 2 - second_value
result_values = [first_value]
for current_value in input_values:
    previous_value = result_values[-1]
    next_value = current_value * 2 - previous_value
    result_values.append(next_value)
result_values.pop()
print(*result_values)