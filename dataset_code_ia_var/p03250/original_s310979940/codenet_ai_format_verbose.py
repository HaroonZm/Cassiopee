input_strings_list = list(map(str, input().split()))

input_strings_list.sort(reverse=True)

largest_string = str(input_strings_list[0])
second_largest_string = str(input_strings_list[1])

concatenated_largest_strings = largest_string + second_largest_string

concatenated_number = int(concatenated_largest_strings)

smallest_number = int(input_strings_list[2])

final_sum = concatenated_number + smallest_number

print(final_sum)