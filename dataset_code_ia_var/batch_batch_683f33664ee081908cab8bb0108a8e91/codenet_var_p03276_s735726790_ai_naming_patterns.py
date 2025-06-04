input_count, selection_size = map(int, input().split())
position_list = list(map(int, input().split()))
minimum_distance = float('inf')
for start_index in range(input_count - selection_size + 1):
    left_position = position_list[start_index]
    right_position = position_list[start_index + selection_size - 1]
    travel_distance = right_position - left_position + min(abs(left_position), abs(right_position))
    minimum_distance = min(minimum_distance, travel_distance)
print(minimum_distance)