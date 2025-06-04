import numpy as np
import math

input_size = int(input())

sequence_values = np.zeros(input_size + 1)
sequence_values[1:] = np.array(list(map(int, input().split())))

difference_total = int(np.abs(np.roll(sequence_values, 1) - sequence_values).sum())

for index in range(1, input_size + 1):
    prev_index = index - 1
    next_index = (index + 1) % (input_size + 1)
    diff_remove = math.fabs(sequence_values[index] - sequence_values[prev_index])
    diff_remove += math.fabs(sequence_values[next_index] - sequence_values[index])
    diff_add = math.fabs(sequence_values[next_index] - sequence_values[prev_index])
    result_value = int(difference_total - diff_remove + diff_add)
    print(result_value)