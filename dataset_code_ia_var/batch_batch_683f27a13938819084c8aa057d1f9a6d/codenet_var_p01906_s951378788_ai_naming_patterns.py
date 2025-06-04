input_size_n, window_size_m = map(int, input().split())
sequence_a = [int(value) for value in input().split()]

current_index = 0
total_difference = 0

while current_index % input_size_n != 0 or current_index == 0:
    window_min = 101
    window_max = -1

    for offset in range(current_index, current_index + window_size_m):
        value = sequence_a[offset % input_size_n]
        window_min = min(window_min, value)
        window_max = max(window_max, value)

    total_difference += window_max - window_min
    current_index += window_size_m

print(total_difference)