import sys

def exit_with_no_message():
    print("No")
    sys.exit()

input_string = raw_input()

allowed_directions = ["L", "R", "U", "D"]
allowed_odd_positions = ["R", "U", "D"]
allowed_even_positions = ["L", "U", "D"]

current_position = 1

if not (1 <= len(input_string) <= 100):
    exit_with_no_message()

for current_character in input_string:

    if current_character not in allowed_directions:
        exit_with_no_message()

    if current_position % 2 == 0:
        if current_character not in allowed_even_positions:
            exit_with_no_message()
    else:
        if current_character not in allowed_odd_positions:
            exit_with_no_message()

    current_position += 1

print("Yes")