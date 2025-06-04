input_count = int(input())
string_count_dict = {}
for index in range(input_count):
    input_string = input()
    if input_string not in string_count_dict:
        string_count_dict[input_string] = 1
    else:
        string_count_dict[input_string] += 1

most_frequent_strings = []
maximum_count = max(string_count_dict.values())
for string_key, count_value in string_count_dict.items():
    if count_value == maximum_count:
        most_frequent_strings.append(string_key)

most_frequent_strings.sort()
for string_item in most_frequent_strings:
    print(string_item)