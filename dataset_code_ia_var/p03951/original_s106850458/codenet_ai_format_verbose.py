length_of_strings = int(input())

first_string = input()

second_string = input()

minimum_length_of_concatenation = 2 * length_of_strings

for overlap_length in range(length_of_strings):

    suffix_of_first_string = first_string[-1 - overlap_length : ]

    prefix_of_second_string = second_string[0 : overlap_length + 1]

    if suffix_of_first_string == prefix_of_second_string:

        minimum_length_of_concatenation = 2 * length_of_strings - overlap_length - 1

print(minimum_length_of_concatenation)