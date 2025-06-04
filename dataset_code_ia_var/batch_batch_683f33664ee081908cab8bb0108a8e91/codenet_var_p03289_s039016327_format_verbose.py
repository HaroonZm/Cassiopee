import sys

input_string_as_list = list(input())

if input_string_as_list[0] == 'A':

    del input_string_as_list[0]

    substring_middle = input_string_as_list[1:-1]

    count_uppercase_C_in_middle = substring_middle.count('C')

    if count_uppercase_C_in_middle == 1:

        input_string_as_list.remove('C')

        for character_index in range(len(input_string_as_list)):

            if input_string_as_list[character_index].isupper():

                print('WA')
                sys.exit()

        print('AC')

    else:

        print('WA')

else:

    print('WA')