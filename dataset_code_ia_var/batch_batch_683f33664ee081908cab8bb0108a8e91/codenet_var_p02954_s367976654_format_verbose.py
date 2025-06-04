user_input_string = str(input())

string_length = len(user_input_string)

final_positions_counts = [1] * string_length

for current_index in range(string_length):

    is_right_move = user_input_string[current_index] == 'R'
    next_index_exists = current_index + 1 < string_length
    is_next_right_move = next_index_exists and user_input_string[current_index + 1] == 'R'

    if is_right_move and is_next_right_move:
        next_next_index = current_index + 2
        if next_next_index < string_length:
            final_positions_counts[next_next_index] += final_positions_counts[current_index]
        final_positions_counts[current_index] = 0


for current_index in range(string_length - 1, -1, -1):

    is_left_move = user_input_string[current_index] == 'L'
    previous_index_exists = current_index - 1 >= 0
    is_previous_left_move = previous_index_exists and user_input_string[current_index - 1] == 'L'

    if is_left_move and is_previous_left_move:
        previous_previous_index = current_index - 2
        if previous_previous_index >= 0:
            final_positions_counts[previous_previous_index] += final_positions_counts[current_index]
        final_positions_counts[current_index] = 0

print(' '.join(map(str, final_positions_counts)))