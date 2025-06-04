num_elements, window_size = map(int, input().split())
sequence_elements = list(map(int, input().split()))
min_total_distance = float('inf')

for window_start_index in range(0, num_elements - window_size + 1):
    window_first_element = sequence_elements[window_start_index]
    window_last_element = sequence_elements[window_start_index + window_size - 1]
    if window_last_element <= 0:
        min_total_distance = min(min_total_distance, abs(window_first_element))
    elif window_first_element >= 0:
        min_total_distance = min(min_total_distance, abs(window_last_element))
    else:
        min_total_distance = min(
            min_total_distance,
            abs(window_last_element) + abs(window_first_element) * 2,
            abs(window_last_element) * 2 + abs(window_first_element)
        )

print(min_total_distance)