import sys

for input_line in sys.stdin:

    list_of_three_character_substrings = [
        input_line[index:index + 3]
        for index in range(len(input_line) - 3)
    ]

    number_of_occurrences_of_JOI = list_of_three_character_substrings.count('JOI')
    print(number_of_occurrences_of_JOI)

    number_of_occurrences_of_IOI = list_of_three_character_substrings.count('IOI')
    print(number_of_occurrences_of_IOI)