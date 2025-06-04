number_of_elements = int(input())

list_of_integers = list(map(int, input().split()))

prefix_sums = [0 for index in range(number_of_elements)]
prefix_sums[0] = list_of_integers[0]

for current_index in range(1, number_of_elements):
    prefix_sums[current_index] = prefix_sums[current_index - 1] + list_of_integers[current_index]

difference_between_two_parts = [0 for index in range(number_of_elements - 1)]

for split_index in range(0, number_of_elements - 1):
    sum_of_first_part = prefix_sums[split_index]
    total_sum = prefix_sums[-1]
    sum_of_second_part = total_sum - sum_of_first_part
    difference_between_two_parts[split_index] = abs(sum_of_first_part - sum_of_second_part)

minimum_difference = min(difference_between_two_parts)

print(minimum_difference)