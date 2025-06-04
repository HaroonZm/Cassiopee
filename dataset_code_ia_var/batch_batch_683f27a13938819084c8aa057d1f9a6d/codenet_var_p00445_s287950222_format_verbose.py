import sys

for input_line in sys.stdin:

    count_joi_substrings = 0
    count_ioi_substrings = 0

    for character_index in range(len(input_line) - 3):
        current_substring = input_line[character_index : character_index + 3]
        if current_substring == 'JOI':
            count_joi_substrings += 1
        if current_substring == 'IOI':
            count_ioi_substrings += 1

    print(count_joi_substrings)
    print(count_ioi_substrings)