input_list_a = [int(value) for value in raw_input().split()]
input_list_b = [int(value) for value in raw_input().split()]

combined_data_list = []
for index in range(len(input_list_a)):
    sum_ab = input_list_a[index] + input_list_b[index]
    if sum_ab > 0:
        fraction_a = input_list_a[index] / 100.0
        fraction_b = input_list_b[index] / 100.0
        total_fraction = sum_ab / 100.0
        proportion_a = input_list_a[index] * 1.0 / sum_ab
        combined_data_list.append((fraction_a, fraction_b, total_fraction, proportion_a))

number_of_items = len(combined_data_list)
combined_data_list.sort(key=lambda element: element[3], reverse=True)

usage_list = [0] * number_of_items
remaining_resource = 1
for usage_index in range(number_of_items):
    max_usage = min(remaining_resource / combined_data_list[usage_index][2], 1)
    usage_list[usage_index] = max_usage
    remaining_resource -= max_usage * combined_data_list[usage_index][2]
    if remaining_resource <= 0:
        break

final_sum = 0
for aggregate_index in range(number_of_items):
    final_sum += combined_data_list[aggregate_index][0] * usage_list[aggregate_index]

print final_sum