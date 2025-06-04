import collections

input_count = int(input())
input_strings = [input() for idx_input in range(input_count)]

string_counter = collections.Counter(input_strings)
counter_items = string_counter.most_common()

max_occurrence = counter_items[0][1]

most_common_strings = []
for idx_counter in range(len(string_counter)):
    if counter_items[idx_counter][1] == max_occurrence:
        most_common_strings.append(counter_items[idx_counter][0])

most_common_strings.sort()

for idx_result in range(len(most_common_strings)):
    print(most_common_strings[idx_result])