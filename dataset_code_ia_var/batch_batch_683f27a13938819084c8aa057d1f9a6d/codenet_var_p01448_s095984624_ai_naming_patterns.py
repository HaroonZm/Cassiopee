import itertools

input_count = int(input())
frequency_table = [0 for _ in range(100003)]
frequency_table[0] = 1

for event_index in range(input_count):
    start_index, end_index = map(int, input().split())
    frequency_table[start_index] += 1
    frequency_table[end_index + 1] -= 1

cumulative_frequency_table = list(itertools.accumulate(frequency_table))
maximum_valid_index = -1

for current_index in range(len(cumulative_frequency_table)):
    if cumulative_frequency_table[current_index] >= current_index:
        maximum_valid_index = current_index

print(maximum_valid_index - 1)