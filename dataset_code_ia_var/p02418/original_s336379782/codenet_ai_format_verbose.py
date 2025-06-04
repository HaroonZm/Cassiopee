import sys

first_input_string = raw_input()
second_input_string = raw_input()

for start_index_in_first_string, current_character_in_first_string in enumerate(first_input_string):

    if second_input_string[0] != current_character_in_first_string:
        continue

    current_index_in_first_string = start_index_in_first_string
    current_index_in_second_string = 0

    while True:
        remaining_first_string = first_input_string[current_index_in_first_string:]
        remaining_second_string = second_input_string[current_index_in_second_string:]

        if len(remaining_first_string) >= len(remaining_second_string):
            if remaining_first_string.startswith(remaining_second_string):
                print "Yes"
                sys.exit(0)
            else:
                break
        else:
            if remaining_second_string.startswith(remaining_first_string):
                current_index_in_first_string = 0
                current_index_in_second_string += len(remaining_first_string)
            else:
                break

print "No"