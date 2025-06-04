input_count = int(input())
value_list = list(map(int, input().split()))
value_list.append(0)
total_cost = 0
prev_value = 0
for index in range(input_count + 1):
    total_cost += abs(prev_value - value_list[index])
    prev_value = value_list[index]

for step_index in range(input_count):
    adjusted_cost = total_cost - abs(value_list[step_index] - value_list[step_index - 1]) - abs(value_list[step_index + 1] - value_list[step_index]) + abs(value_list[step_index + 1] - value_list[step_index - 1])
    print(adjusted_cost)