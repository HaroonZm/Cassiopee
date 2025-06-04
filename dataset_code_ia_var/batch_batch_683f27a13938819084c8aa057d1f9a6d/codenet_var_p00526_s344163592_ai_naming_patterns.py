import sys
from sys import stdin
read_input_line = stdin.readline

num_elements = int(read_input_line())
sequence_values = list(map(int, read_input_line().split()))

segment_lengths = []
current_segment_length = 0

for element_index in range(num_elements):
    if current_segment_length > 0:
        if sequence_values[element_index] == sequence_values[element_index - 1]:
            segment_lengths.append(current_segment_length)
            current_segment_length = 0
    current_segment_length += 1
if current_segment_length > 0:
    segment_lengths.append(current_segment_length)

max_sum = 0
current_sum = 0
for segment_index in range(len(segment_lengths)):
    current_sum += segment_lengths[segment_index]
    if segment_index > 2:
        current_sum -= segment_lengths[segment_index - 3]
    max_sum = max(max_sum, current_sum)

print(max_sum)