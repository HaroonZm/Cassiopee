user_input = input()
number_strings = input().split('+')
unique_numbers = set(number_strings)
occurrences_list = [number_strings.count(number) for number in unique_numbers]
unique_occurrences = set(occurrences_list)
result_sum = sum(min(3 * occurrences_list.count(occurrence), occurrences_list.count(occurrence) + 4)
                 for occurrence in unique_occurrences if occurrence != 1)
result_sum += len(unique_occurrences) - 1 + occurrences_list.count(1)
print(result_sum)