input_values = list(map(int, input().split()))
event_positions = list(map(int, input().split()))
segment_counts = [0] * input_values[2]
unused_segments = 0

for event_position in event_positions:
    for segment_index in range(input_values[2]):
        if segment_index >= event_position - input_values[1] and segment_index <= event_position + input_values[1] - 1:
            segment_counts[segment_index] += 1

for segment_index in range(input_values[2]):
    if segment_counts[segment_index] == 0:
        unused_segments += 1

print(unused_segments)