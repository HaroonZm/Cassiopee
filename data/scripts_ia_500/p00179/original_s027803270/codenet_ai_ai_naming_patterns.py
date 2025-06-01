from collections import deque

def convert_string_to_state(input_string):
    state_value = 0
    for character in input_string:
        state_value *= 3
        if character == "r":
            state_value += 0
        elif character == "g":
            state_value += 1
        elif character == "b":
            state_value += 2
    return state_value

def decode_state_to_list(state_value, length):
    value_list = []
    for _ in range(length):
        value_list.append(state_value % 3)
        state_value //= 3
    value_list.reverse()
    return value_list

def encode_list_to_state(value_list):
    state_value = 0
    for value in value_list:
        state_value = state_value * 3 + value
    return state_value

def main_loop():
    max_length = 10
    max_state_size = 3 ** max_length
    visited_states = [0] * max_state_size

    while True:
        input_string = raw_input()
        if input_string == "0":
            break

        length = len(input_string)
        current_state = convert_string_to_state(input_string)

        # Reset visited states
        for index in range(3 ** length):
            visited_states[index] = 0

        state_queue = deque([current_state])
        visited_states[current_state] = 1

        found_solution = False
        steps = 0
        answer = -1

        while state_queue:
            current_level_size = len(state_queue)
            for _ in range(current_level_size):
                state = state_queue.popleft()
                state_values = decode_state_to_list(state, length)
                if all(value == state_values[0] for value in state_values):
                    found_solution = True
                    answer = steps
                    break

                for i in range(length - 1):
                    if state_values[i] != state_values[i + 1]:
                        original_left = state_values[i]
                        original_right = state_values[i + 1]

                        new_value = 3 - original_left - original_right
                        state_values[i] = new_value
                        state_values[i + 1] = new_value

                        new_state = encode_list_to_state(state_values)
                        if visited_states[new_state] == 0:
                            visited_states[new_state] = 1
                            state_queue.append(new_state)

                        state_values[i] = original_left
                        state_values[i + 1] = original_right
            if found_solution:
                break
            steps += 1

        if answer == -1:
            print "NA"
        else:
            print answer

main_loop()