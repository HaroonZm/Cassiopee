from bisect import bisect_left

input_count = int(input())
input_list = sorted(list(map(int, input().split())))
max_value = input_list[-1]
mid_value = max_value // 2
mid_index = bisect_left(input_list, mid_value)
padded_list = [input_list[0]] + input_list + [input_list[-1]]
closest_difference = 10**9
selected_value = None
for candidate_value in [padded_list[mid_index - 1], padded_list[mid_index], padded_list[mid_index + 1]]:
    current_difference = abs(candidate_value - mid_value)
    if current_difference <= closest_difference and candidate_value < max_value:
        selected_value = candidate_value
        closest_difference = current_difference
print(max_value, selected_value)