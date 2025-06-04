import collections

number_of_strings = int(input())

list_of_strings = [input() for _ in range(number_of_strings)]

string_occurrences_counter = collections.Counter(list_of_strings)

occurrences_list = string_occurrences_counter.most_common()

maximum_occurrence_count = occurrences_list[0][1]

strings_with_maximum_occurrence = []

for index in range(len(string_occurrences_counter)):
    if occurrences_list[index][1] == maximum_occurrence_count:
        strings_with_maximum_occurrence.append(occurrences_list[index][0])

strings_with_maximum_occurrence.sort()

for string in strings_with_maximum_occurrence:
    print(string)