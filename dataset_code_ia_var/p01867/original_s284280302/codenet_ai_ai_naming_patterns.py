from collections import Counter

input_length = input()
input_values = input().split('+')

counter_value_occurrences = Counter(input_values)
counter_occurrence_frequencies = Counter(counter_value_occurrences.values())

result_total = 4 * len(counter_value_occurrences) - 1
for occurrence_count, frequency_count in counter_occurrence_frequencies.items():
    if occurrence_count == 1:
        result_total -= 2 * frequency_count
    elif frequency_count >= 2:
        result_total -= 2 * (frequency_count - 2)

print(result_total)