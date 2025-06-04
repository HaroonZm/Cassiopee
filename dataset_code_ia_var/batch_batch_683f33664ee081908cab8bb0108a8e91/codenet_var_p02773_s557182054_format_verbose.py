number_of_inputs = int(input())

string_occurrence_count = {}

for current_input_index in range(number_of_inputs):
    input_string = str(input())
    if input_string not in string_occurrence_count:
        string_occurrence_count[input_string] = 1
    else:
        string_occurrence_count[input_string] += 1

list_of_most_frequent_strings = []
maximum_occurrence = max(string_occurrence_count.values())

for string_value, occurrence_count in string_occurrence_count.items():
    if occurrence_count == maximum_occurrence:
        list_of_most_frequent_strings.append(string_value)

list_of_most_frequent_strings.sort()

for frequent_string in list_of_most_frequent_strings:
    print(frequent_string)