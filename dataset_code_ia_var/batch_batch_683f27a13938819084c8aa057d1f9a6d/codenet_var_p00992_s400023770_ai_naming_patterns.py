input_count = int(input())
total_score = 1
value_counts = [0] * 126

for idx_input in range(input_count):
    input_value = int(input())
    if input_value <= 125:
        value_counts[input_value] += 1
    total_score += input_value

cumulative_sum = 0
for idx_value in range(1, 126):
    cumulative_sum += value_counts[idx_value - 1]
    if input_count > cumulative_sum + 4 * idx_value:
        total_score -= input_count - (cumulative_sum + 4 * idx_value)
print(total_score)