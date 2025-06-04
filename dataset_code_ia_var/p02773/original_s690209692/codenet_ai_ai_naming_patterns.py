input_count = int(input())
input_strings = [input() for _ in range(input_count)]

import collections
string_counter = collections.Counter(input_strings)
sorted_strings = sorted(string_counter)

maximum_count = max(string_counter.values())
most_frequent_strings = []
for string, count in string_counter.items():
    if count == maximum_count:
        most_frequent_strings.append(string)

most_frequent_strings_sorted = sorted(most_frequent_strings)
print('\n'.join(most_frequent_strings_sorted))