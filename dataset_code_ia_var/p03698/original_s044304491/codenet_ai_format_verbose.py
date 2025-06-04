#!/usr/bin/env python3

import sys

input_string = input().strip()

for first_character_index in range(len(input_string)):

    for second_character_index in range(first_character_index + 1, len(input_string)):

        if input_string[first_character_index] == input_string[second_character_index]:

            print('no')
            sys.exit(0)

print('yes')