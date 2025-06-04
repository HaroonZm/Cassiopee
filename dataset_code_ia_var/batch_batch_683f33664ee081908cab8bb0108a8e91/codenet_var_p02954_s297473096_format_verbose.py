input_string = input()

length_of_input = len(input_string)

final_counts_per_position = [0] * length_of_input

for index in range(length_of_input - 1):

    if input_string[index:index + 2] == "RL":

        # Count consecutive 'R' leftwards until non-'R' is hit
        for left_position in range(index, -1, -1):

            if input_string[left_position] == "R":

                rightmost_R_or_L_index = index + (index - left_position) % 2
                final_counts_per_position[rightmost_R_or_L_index] += 1

            else:
                break

        # Count consecutive 'L' rightwards until non-'L' is hit
        for right_position in range(index + 1, length_of_input):

            if input_string[right_position] == "L":

                leftmost_R_or_L_index = index + (right_position - index) % 2
                final_counts_per_position[leftmost_R_or_L_index] += 1

            else:
                break

print(" ".join(map(str, final_counts_per_position)))