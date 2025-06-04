#!/usr/bin/env python3

user_input_string = input()

transition_count = 0

previous_character = user_input_string[0]

for current_character in user_input_string[1:]:

    if current_character != previous_character:

        transition_count += 1

        previous_character = current_character

print(transition_count)