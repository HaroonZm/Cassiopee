from collections import Counter

input_length = int(input())
input_string = input()
even_index_counter = Counter(input_string[::2])
value_frequency_counter = Counter(even_index_counter.values())
result_sum = 0

for frequency, count in value_frequency_counter.items():
    if frequency == 1:
        result_sum += 2 * count
    else:
        if count == 1:
            result_sum += 4
        else:
            result_sum += 4 + count * 2

print(result_sum - 1)