from collections import deque

# Precompute the maximum space for marking visited color arrangements
visited_color_states = [0] * (3 ** 10)

while True:
    input_string = raw_input()
    if input_string == "0":
        break

    color_count = len(input_string)
    encoded_state = 0

    # Map each character in the string to a number (r:0, g:1, b:2) to generate a unique state
    for character_index in range(color_count):
        encoded_state *= 3
        if input_string[character_index] == "r":
            encoded_state += 0
        if input_string[character_index] == "g":
            encoded_state += 1
        if input_string[character_index] == "b":
            encoded_state += 2

    transformation_found = False

    # Initialize all color arrangements as unvisited for the current string length
    for combination_index in range(3 ** color_count):
        visited_color_states[combination_index] = 0

    current_state_queue = [encoded_state]
    processing_queue = deque(current_state_queue)
    visited_color_states[encoded_state] = 1

    answer_min_steps = -1
    current_steps = 0

    # BFS to find minimum step to reach a uniform colored state
    while len(processing_queue) > 0:
        current_level_length = len(processing_queue)

        for node_index in range(current_level_length):
            current_state = processing_queue.popleft()
            color_values = []

            # Decode integer state to color values array
            temp_state = current_state
            for color_index in range(color_count):
                color_values.append(temp_state % 3)
                temp_state //= 3

            is_uniform = True
            first_color_value = color_values[0]
            for check_index in range(color_count):
                if color_values[check_index] != first_color_value:
                    is_uniform = False
                    break

            if is_uniform:
                transformation_found = True
                answer_min_steps = current_steps
                break

            # Try all operations by changing adjacent differing colors
            for neighbor_index in range(color_count - 1):
                if color_values[neighbor_index] != color_values[neighbor_index + 1]:
                    original_color_left = color_values[neighbor_index]
                    original_color_right = color_values[neighbor_index + 1]
                    new_color = 3 - original_color_left - original_color_right

                    # Change both adjacent colors
                    color_values[neighbor_index] = new_color
                    color_values[neighbor_index + 1] = new_color

                    # Encode the new state
                    new_encoded_state = 0
                    for encode_index in range(color_count - 1, -1, -1):
                        new_encoded_state *= 3
                        new_encoded_state += color_values[encode_index]

                    if visited_color_states[new_encoded_state] == 0:
                        processing_queue.append(new_encoded_state)
                        visited_color_states[new_encoded_state] = 1

                    # Restore the colors back for next iteration
                    color_values[neighbor_index] = original_color_left
                    color_values[neighbor_index + 1] = original_color_right

        if transformation_found:
            break
        else:
            current_steps += 1

    if answer_min_steps == -1:
        print "NA"
    else:
        print answer_min_steps